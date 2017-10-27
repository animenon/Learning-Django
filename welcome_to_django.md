# Creating a project

From the command line, cd into a directory where you’d like to store your code, then run the following command:

```
  $ django-admin startproject mysite
```

`startproject` would create:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Change to the root directory and run:

```
  $ python manage.py runserver
```
This will check the Django Project. By default, the runserver command starts the development server on the internal IP at port 8000. Visit http://127.0.0.1:8000/ on any Web browser and you will see a __“Welcome to Django”__ page.
