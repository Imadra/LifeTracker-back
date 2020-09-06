from django.urls import path
from .views import AddList, GetAllLists, DeleteList, GetList, UpdateList

urlpatterns = [
    path('add/', AddList.as_view()),
    path('getall/', GetAllLists.as_view(), name="get_all_lists"),
    path('delete/', DeleteList.as_view()),
    path('get/', GetList.as_view()),
    path('update/', UpdateList.as_view()),
]