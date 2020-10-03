# How to create a Django App

A project is a collection of apps. An app is a web application which performs an small task like
 Career options of a website or polling section.'''


# Syntax for creating an app
Unix-python3 manage.py startapp APPNAME
Windows-python manage.py startapp APPNAME

# Add the apps name in INSTALLED_APPS in settings.py
  `INSTALLED_APPS = [
    'APPNAME.apps.APPNAMEConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]`

# Example: Let's create an app which contains info of users called as Users
Unix-python3 manage.py startapp Users
Windows-python manage.py startapp Users

  `INSTALLED_APPS = [
    'Users.apps.Users.Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]`
