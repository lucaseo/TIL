from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

import random
# Create your views here.
# function base view


# django template
def home(request):
    num = None
    some_list = [
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0, 100)
    context = {
        # 'bool_item': False,
        'num': num,
        'some_list': some_list
        }
    return render(request, "home.html", context) #request, #contextvariable from base.html


def about(request):
    context ={

    }
    return render(request, "about.html", context) #request, #contextvariable from base.html


def contact(request):
    context = {

    }
    return render(request, "contact.html", context) #request, #contextvariable from base.html


class contactView(View):
    def get(self, request, *args, **kargs):
        context = {}
        return render(request, "contact.html", context)
