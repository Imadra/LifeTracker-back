from django.urls import path
from .views import GetAll, Add

urlpatterns = [
    # path('add/', Add.as_view()),
    path('getall/', GetAll.as_view()),
    path('add/', Add.as_view())
]