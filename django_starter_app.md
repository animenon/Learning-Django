# Django Starter App, MVC
Adapted from: https://docs.djangoproject.com/en/1.11/intro/tutorial01/

## Starting the app

Now that you have completed the "Welcome to Django" example, it's time to create your first app.

A project is a collection of apps. An app is a web application which performs an small task like career options of a website or polling section.

From the command line, cd into `mysite` or whereever `manage.py` is. Then, run:

```
python manage.py startapp polls
```

This command starts a Django app called `polls`. You should thus see a directory called `polls` which should be laid out like this:

```
polls/
  __init__.py
  admin.py
  apps.py
  migrations/
    __init__.py
  models.py
  tests.py
  views.py
```

## Add the apps name in INSTALLED_APPS in settings.py
  ```
  INSTALLED_APPS = [
    'polls.apps.pollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
## MVC framework

Before getting started, let's briefly examine the directory structure. Don't worry too much about the rest of the app, but you'll notice two files `models.py` and `views.py`.

Models and views are two parts of an MVC framework, or model-view-controller framework. If you've already worked with another MVC framework like Ruby on Rails or Node.js, you can skip this section.

The MVC framework has three main parts, the **model**, the **view**, and the **controller**. 

### Model

The model is the core component of the MVC framework. If you've ever worked with OOP (object-oriented programming), the model is the component that most closely resembles an object.

### View

The view is what the user sees on the website. Usually, this will render an HTML file, though for API-only applications, you may return JSON.

### Controller

The controller controls user input, and uses that input to manipulate an instance of a model.

[Wikipedia](https://en.wikipedia.org/wiki/Model–view–controller) has a good diagram of the MVC framework:

![MVC file](https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg)

## Further steps

To proceed further in the polls app, refer to the Django tutorial linked at the beginning of the page.
