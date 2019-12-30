from django.urls import path
from .views import GetInfo

urlpatterns = [
    path('getinfo/', GetInfo.as_view()),
]