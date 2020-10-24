from django.urls import path
from .views import Add, GetAll, Delete

urlpatterns = [
	path('add/', Add.as_view(), name="add_log"),
	path('getall/', GetAll.as_view(), name="get_all_logs"),
	path('delete/', Delete.as_view(), name="delete_log"),
]