
# **Django project walkthrough**

youtube tutorial link : <https://youtu.be/yDv5FIAeyoY>

<br>

## 20180319 (00:00:00 ~ 00:31:58)

### Getting Started with Django
#### Django environment setup

#### keywords:
>- `virtualenv`
>- `pip3 freeze`
>- `startproject`
>- manage.py
>- base.py _vs_ local.py _vs_ production.py

_reference_ : <https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/>)

<br>

## 20180320 (00:31:58 ~ 00:45:14)

### What Django Does
#### Creating new Django project and Django app

#### keywords:
>- django app
>- `startapp`
>- view.py
>- url.py
>- runserver

<br>

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

_reference_ :  <https://docs.djangoproject.com/en/1.11/ref/templates/builtins/>

<br>

## 20180323 (01:08:38 ~ 01:22:42)

### Template Inheritance

#### keywords:
>- multiple functions in view.py file -> add corresponding functions into urls
>- http://127.0.0.1:8000/home2, home 3 variation
>- url.py - specifies extensions of url for each fucntions in view.py
>- {% block content %}{% endblock content %} --> {& extends "base.html"&} , {% block content %}{% endblock content %}
>- {{% block.super %}}
>- <title>{% block head_title %}django1.11 tutorial{% endblock head_title %}</title> headline text and block/endblock to other pages

<br>

## 20180324 (01:22:42 ~ 01:28:49)

### Template Tag

#### keywords:
>- create new folder in templates : src/templates/snippets/nav.html
>- nav as navigation. store navigation details
>- {% include 'snippets/nav.html' %} --> now nav bars appears on all pages
>- add more on src/templates/snippets/ --> css.html, js.html
>- getbootstrap.com -> css, html, jquery CDN
>- src/templates/snippets/sidebar.html

<br>

## 20180325 (01:30:02 ~ 01:38:33)

### Class Based View

#### keywords:
>- standard base views

_reference_ : <https://docs.djangoproject.com/en/1.11/ref/class-based-views/>

<br>

## 20180327 (01:57:11 ~ 02:06:13)

### More on Model Fields (ex. CharField, DateTimeField)

#### keywords:
>- max_length=120 --> covers most of the characters
>- null=True --> allowing null in the database
>- blank=True --> allow leaving blank in build-in Django form
>- DateTimeField : non nullable field --> timezone.now

_reference_ : https://docs.djangoproject.com/en/2.0/ref/models/fields/

<br>

## 20180330 (02:06:13 ~ 02:16:04)

### Displaying Saved Data

#### keywords:
>- queryset :
>- ` <ul>
  {% for obj in object_list%}
    <li> {{obj.name}} {{obj.location}} {{obj.category}} {{obj.timestamp}} {{obj.updated}} </li> `

>- tiemzone settings : settings/base.py(& local.py , production.py) --> timezone = "Asia/Seoul"

>- models.py -->
`def __str__(self): return self.name` --> return object name on admin page


<br>


## 20180402 (02:16:04 ~ 02:25:21)

### Understanding Queryset

#### key practice codes:
>- So what exactly is Queryset?  
  - List of objects received when approaching to a data through functions.

<br>

>- on `python3 manage.py shell`
>- `from restaurants.models import RestaurantLocation`
>- `RestaurantLocation.objects.all()` --> Queryset
>- `for object in RestaurantLocation.objects.all():
print(object.name)`
>- `qs = RestaurantLocation.objects.all()
qs.filter(category__iexact='American Pub'`
>>- `<QuerySet [<RestaurantLocation: The Booth Brewary>]>`
>- `qs.update(category='Pizza')` #update all categories at once

>Adding new obj #1
>- `obj=RestaurantLocation()`
>- `obj.name = "Pei Wei"`
>- `obj.location = "Incheon"`
>- `obj.category = "Chinese"`  
>- `obj`
>> `RestaurantLocation: Pei Wei`
>> However, timestamp won't setup itself this way.

>Adding new obj #2 (with timestamp !)
>- `obj = RestaurantLocation.objects.create(name='Suzuran', location='Bundang', category='Japanese')
`
>- `obj.timestamp`
>> `datetime.datetime(2018, 4, 2, 12, 51, 0, 99929, tzinfo=<UTC>)`

>- filtering `qs2 = RestaurantLocation.objects.filter(category__iexact='Beer Pub')`
>- filtering with excluding certain objects `qs = RestaurantLocation.objects.filter(category__iexact='Beer Pub').exclude(name__icontains='Brewary')`

<br>

## 20180403 (02:25:21 ~ 02:34:23)

### Generic List View

#### key concept & practice codes:
>
```
def get_queryset(self):
      print(self.kwargs)
      slug = self.kwargs.get("slug")
      if slug:
          queryset = RestaurantLocation.objects.filter(
              Q(category__icontains=slug) |
              Q(category__iexact=slug)
          )
      else:
          queryset = RestaurantLocation.objects.none
      return queryset
      ```
>- `from django.db.models import Q` on views.py (Q look ups -- queryset lookup)
>- change restaurant/restaurant_list.html template name to default html `restaurantlocation_list.html` (from the model)
<br>