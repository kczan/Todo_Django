from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('home', views.list_homepage),
    path('admin', admin.site.urls)
]
