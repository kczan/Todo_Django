from django.urls import path
from django.contrib import admin
from tasks import views as tasks_views


urlpatterns = [
    path('home/', tasks_views.list_homepage, name='list'),
    path('', tasks_views.list_homepage, name='list'),
    path('admin/', admin.site.urls),
    path('update_task/<str:pk>/', tasks_views.update_task, name='update_task'),
    path('delete_task/<str:pk>/', tasks_views.delete_task, name='delete_task'),
]
