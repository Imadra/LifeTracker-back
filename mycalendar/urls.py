from django.urls import path
from .views import GetInfo, EditDay

urlpatterns = [
    path('getinfo/', GetInfo.as_view()),
    path('edit/', EditDay.as_view()),
]