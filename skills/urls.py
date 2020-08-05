from django.urls import path
from .views import Add, GetAll, Delete, Get, Update

urlpatterns = [
    path('add/', Add.as_view()),
    path('getall/', GetAll.as_view(), name="get_all_skills"),
    path('get/', Get.as_view()),
    path('update/', Update.as_view()),
    path('delete/', Delete.as_view()),
]