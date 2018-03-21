from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "base.html", context) #request, #contextvariable from base.html



# standard html
# def home_old(request):
#     html_var = 'f strings' #f string available starting python3.6
#     html_ = f"""<!doctype html>
#     <html lang="en">
#     <head>
#     </head>
#     <body>
#     <h1>Hello World!</h1>
#     <p>This is {html_var} coming through</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)
#     # return render(request, "home.html", {}) #request
