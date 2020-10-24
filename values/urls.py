from django.urls import path
from .views import Add, GetAll, Delete

urlpatterns = [
    path('add/', Add.as_view()),
    path('getall/', GetAll.as_view(), name="get_all_values"),
    path('delete/', Delete.as_view()),
]