from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def list_homepage(request):
    context = {
        'page_title': 'Home page _',
    }
    return render(request, 'tasks/list.html', context)
