from django.db import models
from datetime import datetime, timedelta

class User(models.Model):
	SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	fname = models.CharField(max_length=255,verbose_name=u"First Name")
	lname= models.CharField(max_length=255)
	email=models.EmailField(max_length=255)
	mobile= models.CharField(max_length=20)
	skype= models.CharField(max_length=20,null=True,blank=True)
	gender = models.CharField(max_length=1,choices=SEX,blank=False,default="")
	dob = models.DateField()
	qualification = models.ForeignKey('Qualification')
	website = models.URLField(max_length=200,null=True,blank=True)
	address = models.TextField(null=True,blank=True)
	skills = models.ForeignKey('Skills')
	experience = models.IntegerField(null=True,blank=True,choices=((int(x), x) for x in range(1,7)))
	remarks = models.TextField(null=True,blank=True)
	join_date=models.DateTimeField(editable=False,default=datetime.now())
	profile_pic = models.ImageField(upload_to = 'user/',null=True,blank=True)
	thumb_pic = models.ImageField(upload_to = 'user/thumb/',null=True,blank=True)
	
	def delete(self, *args, **kwargs):
		storage, path = self.profile_pic.storage, self.profile_pic.path
		storage1, path1 = self.thumb_pic.storage, self.thumb_pic.path
		super(User, self).delete(*args, **kwargs)
		storage.delete(path)
		storage1.delete(path1)

	def save(self, *args, **kwargs):
		try:
			this = User.objects.get(id=self.id)
			create_thumbnail(self)
			if this.profile_pic != self.profile_pic:
				this.profile_pic.delete(save=False)
				this.thumb_pic.delete(save=False)
		except: pass
		super(User, self).save(*args, **kwargs)
 
class Qualification(models.Model):
	qualification_name= models.CharField(max_length=200)
	def __str__(self):
		return '%s' % (self.qualification_name)

class Skills(models.Model):
    skills= models.CharField(max_length=200)
    def __str__(self):
		return '%s' % (self.skills)

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

def create_thumbnail(obj):
	if not obj.profile_pic:
		return
	from PIL import Image
	from cStringIO import StringIO
	from django.core.files.uploadedfile import SimpleUploadedFile
	import os
	THUMBNAIL_SIZE = (200,200)
	DJANGO_TYPE = obj.profile_pic.file.content_type
	if DJANGO_TYPE == 'image/jpeg':
		PIL_TYPE = 'jpeg'
		FILE_EXTENSION = 'jpg'
	elif DJANGO_TYPE == 'image/png':
		PIL_TYPE = 'png'
		FILE_EXTENSION = 'png'
	image = Image.open(StringIO(obj.profile_pic.read()))
	image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
	temp_handle = StringIO()
	image.save(temp_handle, PIL_TYPE)
	temp_handle.seek(0)
	suf = SimpleUploadedFile(os.path.split(obj.profile_pic.name)[-1],temp_handle.read(), content_type=DJANGO_TYPE)
	obj.thumb_pic.save('%s.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)
