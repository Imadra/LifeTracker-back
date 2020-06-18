from django.urls import path
from .views import GetDay, EditDay, AddTask, GetAllTasks, GetTask, DeleteTask, UpdateTask, FinishTask, UnFinishTask

urlpatterns = [
    path('days/get/', GetDay.as_view()),
    path('days/edit/', EditDay.as_view()),
    path('tasks/get/', GetTask.as_view()),
    path('tasks/delete/', DeleteTask.as_view()),
    path('tasks/add/', AddTask.as_view()),
    path('tasks/update/', UpdateTask.as_view()),
    path('tasks/getall/', GetAllTasks.as_view()),
    path('tasks/finish/', FinishTask.as_view()),
    path('tasks/unfinish/', UnFinishTask.as_view()),
]