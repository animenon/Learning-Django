Kurulum

Atölyede bir blog geliştireceksiniz, eğitim günü kodlamaya hazır olmanız için önceden ayarlamakta fayda olan birkaç kurulum var.

Python Yükleyin

Bu bölüm Geek Girls Carrots tarafından yapılan bir eğitime dayanılarak hazırlanmıştır. (http://django.carrots.pl/)

Django, Python ile yazılmıştır. Django ile bir şey yapmak için Python diline ihtiyacımız var. Hadi Python kurmaya başlayalım! Biz Python 3.4 kurmak istiyoruz, eğer daha düşük bir sürüme sahipseniz, güncellemelisiniz.

Windows

Windows için Python indirmek için resmi siteyi ziyaret edebilirsiniz: https://www.python.org/downloads/release/python-343/. *.msi dosyasını indirdikten sonra, dosyayı çalıştırın (çift tıklayın) ve yönergeleri izleyin. Python kurulumunu yaptığınız dizinin yolunu (dizini) unutmamanız önemli. Daha sonra lazım olacak!

Dikkat: Özelleştir (Customize) olarak seçilmiş kurulum sihirbazının ikinci ekranında seçenekleri aşağıya kaydırın ve "Add python.exe to the Path" (python.exe yolunu ekle) seçeneğinin üzerine gelip "Will be installed on local hard drive" (Lokal hard diske kurulacak) seçeneğini seçin:

Python'u arama yoluna eklemeyi unutmayın

Linux

Muhtemelen sisteminizde Python zaten yüklüdür. Yüklü olup olmadığını (ya da hangi versiyon olduğunu) kontrol etmek için komut satırını açın ve aşağıdaki komutları girin:

$ python3 --version
Python 3.4.3
Python yüklü değilse ya da farklı bir versiyon edinmek istiyorsanız aşağıdaki adımları takip edin:

Debian veya Ubuntu

Terminale bu komutu girin:

$ sudo apt-get install python3.4
Fedora

Terminalde kullanmanız gereken komut:

$ sudo dnf install python3.4
OS X

Python kurulum dosyasını indirmek için resmi siteye gitmelisiniz: https://www.python.org/downloads/release/python-342/:

Mac OS X 64-bit/32-bit yükleyici dosyasını indirin,
python-3.4.3-macosx10.6.pkg dosyasına çift tıklayarak yükleyiciyi çalıştırın.
Kurulumun başarılı olup olmadığını kontrol etmek için Terminal uygulamasını açın ve aşağıdaki python3 komutunu çalıştırın:

$ python3 --version
Python 3.4.3
Herhangi bir şüpheniz varsa, kurulumda bir şeyler ters gittiyse ya da sonrasında ne yapacağınızı bilmiyorsanız eğitmene sorabilirsiniz! Bazen işler düzgün gitmiyor, bu durumda daha fazla deneyime sahip birinden yardım istemelisiniz.

Bir "virtualenv" kurun ve Django'yu yükleyin

Bu bölümün bir kısmı Geek Girls Carrots tarafından hazırlanmış eğitimlere dayanılarak hazırlanmıştır (http://django.carrots.pl/).

Bu bölümün bir parçası Creative Commons Attribution-ShareAlike 4.0 International License ile lisanslı django-marcador tutorial'a dayanılarak hazırlanmıştır. Django-marcador tutorial'ının hakları Markus Zapke-Gründemann'e aittir.

Virtual environment (Sanal ortam)

Django'yu yüklemeden önce kod ortamınızı düzenli tutmak için son derece yararlı bir araç yükleyeceğiz. Bu adımı atlayabilirsiniz, fakat atlamamanızı tavsiye ederiz. En iyi olası kurulum ile başlamanız sizi gelecekteki bir sürü sorundan koruyacaktır!

Öyleyse bir virtual environment(diğer adıyla virtualenv) kuralım. Virtualenv Python/Django kurulumunuzu her proje için ayrı tutup izole eder. Bu, bir websitesine yapacağınız değişikliklerin diğer geliştirdiklerinize yansımayacağı anlamına gelir. Muazzam, değil mi?

Yapmanız gereken tek şey virtualenv oluşturmak için bir dizin bulmak; örneğin giriş dizininiz. Windows'da bu C:\Users\isim olabilir (isim kısmı kullanıcı adınız olacak şekilde).

Bu eğitim için giriş dizininizde yeni açtığımız djangogirls adlı bir klasör kullanacağız:

mkdir djangogirls
cd djangogirls
myvenv adında bir virtualenv oluşturacağız. Genel komut aşağıdaki şekilde olacak:

python3 -m venv myvenv
Windows

Yeni bir virtualenv oluşturmak için konsolu açıp (nasıl yapıldığını birkaç adım önce anlatmıştık - hatırlıyorsunuz değil mi?) C:\Python34\python -m venv myvenv komutunu çalıştırın. Şöyle görünmeli:

C:\Users\isim\djangogirls> C:\Python34\python -m venv myvenv
C:\Python34\python dizini önceden Python'u kurduğunuz dizin ve myvenv ise virtualenv'inizin ismi olacaktır. İstediğiniz herhangi bir ismi kullanabilirsiniz, ama küçük harfle yazılmasına ve boşluk, aksan karakterleri (örn: å) ve özel karakterleri kullanmamaya dikkat edin. Ayrıca ismi kısa tutmak iyi bir fikir olabilir, zira bu ismi çok kullanıyor olacaksınız!

GNU/Linux ve OS X

Linux ve OS X işletim sistemlerinde virtualenv oluşturmak için python3 -m venv myvenv komutunu çalıştırmak yeter. Komut şu şekilde görünecektir:

~/djangogirls$ python3 -m venv myvenv
Burada myvenv sizin virtualenv'inizin ismi. Dilerseniz istediğiniz herhangi bir isim kullanabilirsiniz, ama büyük harf ve boşluk kullanmamaya dikkat edin. İsmi çok fazla kullanacağınız için kısa tutmak da işinize yarayacaktır.

NOT: Ubuntu 14.04 işletim sisteminde sanal ortam yaratmaya çalışırken şu hatayla karşılaşabilirsiniz:

Error: Command '['/home/zeynep/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
Bu sorunu çözmek için virtualenv komutunu kullanabilirsiniz.

~/djangogirls$ sudo apt-get install python-virtualenv
~/djangogirls$ virtualenv --python=python3.4 myvenv
Virtualenv ile çalışmak

Yukarıdaki komutlar myvenv (veya seçtiğiniz isimde) bir klasör oluşturacaktır. Bu klasörde birçok dosya ve klasör bulunur.

Windows

Şu komutu çalıştırarak virtualenv'i başlatın:

    C:\Users\Name\djangogirls> myvenv\Scripts\activate
GNU/Linux ve OS X

Şu komutu çalıştırarak virtualenv'i başlatın:

    ~/djangogirls$ source myvenv/bin/activate
myvenv yerine kendi seçtiğiniz virtualenv ismini koymayı unutmayın!

NOT: bazen source komutu kullanılamıyor durumda olabilir. Böyle durumlarda onun yerine aşağıdaki komutu da kullanabilirsiniz:

~/djangogirls$ . myvenv/bin/activate
Konsolunuzda şuna benzer bir şey gördüğünüzde virtualenv'in başladığını anlayabilirsiniz:

(myvenv) C:\Users\Name\djangogirls>
ya da:

(myvenv) ~/djangogirls$
En başta beliren (myvenv)'e dikkat edin!

Virtualenv ile çalışırken python otomatik olarak doğru sürümü çalıştıracaktır. Yani python3 yerine python yazabilirsiniz.

Artık bütün gerekli uygulamaları bir araya getirdiğimize göre sonunda Django'yu yükleyebiliriz!

Django'yu yüklemek

virtualenv'i başlattığınız için artık Django'yu pip kullanarak yükleyebiliriz. Konsola pip install django==1.11 komutunu yazın. (İki tane eşittir işareti kullandık: ==).

(myvenv) ~$ pip install django==1.11
Downloading/unpacking django==1.11
Installing collected packages: django
Successfully installed django
Cleaning up...
Windows'ta

Eğer Windows işletim sisteminde pip komutunu kullanırken bir hatayla karşılaştıysanız proje adresinizin boşluk, aksan veya özel karakter içerip içermediğini (C:\Users\User Name\djangogirls gibi) kontrol edin. Eğer durum buysa projenizi boşluk veya özel karakter içermeyen bir adrese taşıyın; önerimiz C:\djangogirls olacaktır. Taşıma işleminden sonra yukarıdaki komutu tekrar deneyin.

Linux'ta

Eğer Ubuntu 12.04 işletim sisteminde pip komutunu çağırırken bir hata iletisiyle karşılaştıysanız python -m pip install -U --force-reinstall pip komutunu çalıştırarak pip kurulumunu onarmayı deneyin.

İşte bu kadar! Sonunda Django uygulamanızı oluşturmaya hazırsınız!

Bir kod düzenleyicisi yükleyin

Birçok farklı kod editörü var, hangi editörü kullanacağınız kişisel tercihinize bağlı. Çoğu Python programcısı PyCharm gibi karmaşık fakat son derece güçlü IDE'leri (Integrated Development Environments-Entegre Geliştirme Ortamları) kullanır. Başlangıç seviyesi için bunlar muhtemelen pek uygun olmayacaktır. Bizim önerdiklerimiz aynı derecede güçlü fakat çok daha basit editörler olacak.

Bizim önerilerimizi aşağıda bulabilirsiniz, fakat eğitmenlerinize onların tercihlerini sormaktan çekinmeyin - onlardan yardım almak daha kolay olacaktır.

Gedit

Gedit açık kaynaklı, ücretsiz bir editördür. Tüm işletim sistemlerinde kullanılabilir.

Buradan indirin

Sublime Text 2

Sublime Text ücretsiz deneme sürümüne sahip oldukça popüler bir editördür. Kurulumu ve kullanımı basittir, tüm işletim sistemlerinde kullanılabilir.

Buradan indirin

Atom

Atom GitHub tarafından geliştirilen oldukça yeni bir editör. Atom ücretsiz, açık kaynak kodlu, kurulumu ve kullanımı basit bir editördür. Windows, OSX ve Linux işletim sistemlerinde kullanılabilir.

Buradan indirin

Neden bir kod editörü kuruyoruz?

Neden Word ya da Notepad kullanmak yerine, özel bir kod editörü yazılımı kurduğumuzu merak ediyor olabilirsiniz.

Birinci nedeni, kodun düz metin olması gerekliliği. Word ve TextEdit gibi programlar RTF (Rich Text Format) gibi özel formatları kullanarak düz metin yerine zengin metin (fontlu ve formatlı metin) üretiyorlar.

İkinci neden, kod editörleri kod düzenlemek için özelleşmişlerdir, dolayısıyla kodu anlamına göre renklerle öne çıkarma (highlighting) veya tırnakları otomatik kapama gibi yararlı özellikler sağlar.

Bütün bunları ileride uygulama içerisinde göreceğiz. Yakında güvenilir ihtiyar kod editörünü favori araçlarınız arasında görmeye başlayacaksınız :)

Git yükleyin

Windows

Git'i git-scm.com adresinden indirebilirsiniz. 5. adıma kadar "next"e basarak geçebilirsiniz. 5. adımda "Adjusting your PATH environment" dediği yerde, "Run Git and associated Unix tools from the Windows command-line" (en alttaki opsiyonu) seçin. Onun dışında, varsayılanlar iyi. Kodu çekerken Windows-stili, kodu gönderirken Unix-stili satır sonları iyidir.

MacOS

Git'i git-scm.com'den indirin ve yönergeleri izleyin.

GNU/Linux

Halihazırda yüklü değilse, git'i paket yöneticinizle indirebilirsiniz. Şunlardan birini deneyin:

sudo apt-get install git
# veya
sudo yum install git
GitHub hesabı oluşturun

GitHub.com'a gidin ve ücretsiz yeni bir kullanıcı hesabı oluşturun.

PythonAnywhere hesabı oluşturun

Sırada PythonAnywhere sitesinde bedava bir "Beginner" ( yeni başlayan) hesabı açma işi var.

www.pythonanywhere.com
Not Burada kullanıcı isminizi seçerken bilin ki blogunuzun URL'si kullanıcıadınız.pythonanywhere.com şeklinde olacak. O yüzden ya kendi rumuzunuzu(nickname) seçin ya da blogunuzun konusu ile ilgili bir isim seçin.
