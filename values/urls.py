from django.urls import path
from .views import Add, GetAll

urlpatterns = [
    path('add/', Add.as_view()),
    path('getall/', GetAll.as_view())
]