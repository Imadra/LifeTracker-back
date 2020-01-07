from django.urls import path
from .views import CodeforcesGet, CodeforcesAdd, RulesGet, RulesAdd, RulesDelete,CodeforcesDelete

urlpatterns = [
    # path('add/', Add.as_view()),
    path('codeforces/gettree/', CodeforcesGet.as_view()),
    path('codeforces/add/', CodeforcesAdd.as_view()),
    path('codeforces/delete/', CodeforcesDelete.as_view()),
    path('rules/gettree/', RulesGet.as_view()),
    path('rules/add/', RulesAdd.as_view()),
    path('rules/delete/', RulesDelete.as_view())
]