from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def keyboard(request):

    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['학식', '내일의 학식', '도서관']
        }
    )


# @csrf_exempt
def message(request):
    return JsonResponse(
    {
        'message':{
            'text': 'Input the sentence'
        },

        'keyboard':{
            'type': 'buttons',
            'buttons': ['학식', '내일의 학식', '도서관']
            }
        }
    )
