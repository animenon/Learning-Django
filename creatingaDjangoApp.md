# How to create a Django App

A project is a collection of apps. An app is a web application which performs an small task like career options of a website or polling section.

After creating our project we will `cd` into `mysite` or wherever `manage.py` file is present. Then type in following syntax:

## Syntax for creating an app
```
Unix-python3 manage.py startapp APPNAME
Windows-python manage.py startapp APPNAME
```

## Add the apps name in INSTALLED_APPS in settings.py
  ```
  INSTALLED_APPS = [
    'APPNAME.apps.APPNAMEConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
This will create a directory named `APPNAME`.This directory is laid out in this form:
```
APPNAME/
  __init__.py
  admin.py
  apps.py
  migrations/
    __init__.py
  models.py
  tests.py
  views.py
  ```
## Example: Let's create an app which contains info of users called as Users
```
Unix-python3 manage.py startapp Users
Windows-python manage.py startapp Users

  INSTALLED_APPS = [
    'Users.apps.Users.Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
