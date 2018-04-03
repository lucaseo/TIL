from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation



# Create your views here.
# function base view


# django template
def restaurants_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__icontains=slug) |
                Q(category__iexact=slug)
            )
        else:
            queryset = RestaurantLocation.objects.none
        return queryset

#
# class JapaneseListView(ListView):
#     queryset = RestaurantLocation.objects.filter(category__iexact='Japanese')
#     template_name = 'restaurants/restaurants_list.html'
#
# class ChineseListView(ListView):
#     queryset = RestaurantLocation.objects.filter(category__iexact='Chinese')
#     template_name = 'restaurants/restaurants_list.html'
