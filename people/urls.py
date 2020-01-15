from django.urls import path
from .views import Add, GetAll, Delete, Get

urlpatterns = [
    path('add/', Add.as_view()),
    path('getall/', GetAll.as_view()),
    path('delete/', Delete.as_view()),
    path('get/', Get.as_view()),
]