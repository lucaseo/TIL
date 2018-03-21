
# **Django project walkthrough**

youtube tutorial link : https://youtu.be/yDv5FIAeyoY

* * * *

## 20180319 (00:00:00 ~ 00:31:58)

### Getting Started with Django
#### Django environment setup

#### keywords:
>- `virtualenv`
>- `pip3 freeze`
>- `startproject`
>- manage.py
>- base.py _vs_ local.py _vs_ production.py


(reference : https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/)

* * * *

## 20180320 (00:31:58 ~ 00:45:14)

### What Django Does
#### Creating new Django project and Django app

#### keywords:
>- django app
>- `startapp`
>- view.py
>- url.py
>- runserver




* * * *

## 20180321 (00:45:14 ~ 01:08:38)

### Rendering HTML

#### keywords:
>- view.py
>- html string
>- new template folder & base.html
>- f string (available in Python3.6)

### Rendering Django Templates

#### keywords:

>- base.py -> 'DIRS': [os.path.join(BASE_DIR, 'templates')],
>- base.html -> {{}} --> context variable

### Context in Django Templates

#### keywords:

>- {%if...%} , {%endif%}
>- {%for...%} , {%endfor%}
>- {%verbatim%}, {%endverbatim%}  --> rendering out the actual code and variables between verbatim
reference <https://docs.djangoproject.com/en/1.11/ref/templates/builtins/>

* * * *
