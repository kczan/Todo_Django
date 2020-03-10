from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('home', views.list_homepage, name='list'),
    path('', views.list_homepage, name='list'),
    path('admin', admin.site.urls),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
]
