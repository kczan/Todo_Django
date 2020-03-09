from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display_homepage(request):
    context = {
        'page_title': 'Main home page',
    }
    return render(request, 'main_home.html', context)
