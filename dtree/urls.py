from django.urls import path
from .views import GetTree, AddNode, DeleteNode, UpdateNode, GetAllTrees

urlpatterns = [
    # path('add/', Add.as_view()),
    path('gettree/', GetTree.as_view(), name="get_tree"),
    path('add/', AddNode.as_view(), name="add_node"),
    path('update/', UpdateNode.as_view(), name="update_node"),
    path('delete/', DeleteNode.as_view(), name="delete_node"),
    path('getall/', GetAllTrees.as_view(), name="get_all_trees"),
]