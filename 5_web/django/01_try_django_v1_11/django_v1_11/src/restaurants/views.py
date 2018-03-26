from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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


class homeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):  #overriding method which overriding TemplateView
        context = super(homeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 100)
        context = {
            # 'bool_item': False,
            'num': num,
            'some_list': some_list
        }
        return context

class aboutView(TemplateView):
    template_name = 'about.html'

class contactView(TemplateView):
    template_name = 'contact.html'
