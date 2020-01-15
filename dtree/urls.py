from django.urls import path
from .views import CodeforcesGet, CodeforcesAdd, CodeforcesUpdate, CodeforcesDelete, RulesGet, RulesAdd, RulesUpdate, RulesDelete, EconAdd, EconUpdate, EconDelete, EconGet

urlpatterns = [
    # path('add/', Add.as_view()),
    path('codeforces/gettree/', CodeforcesGet.as_view()),
    path('codeforces/add/', CodeforcesAdd.as_view()),
    path('codeforces/update/', CodeforcesUpdate.as_view()),
    path('codeforces/delete/', CodeforcesDelete.as_view()),
    path('rules/gettree/', RulesGet.as_view()),
    path('rules/add/', RulesAdd.as_view()),
    path('rules/update/', RulesUpdate.as_view()),
    path('rules/delete/', RulesDelete.as_view()),
    path('econtree/gettree/', EconGet.as_view()),
    path('econtree/add/', EconAdd.as_view()),
    path('econtree/update/', EconUpdate.as_view()),
    path('econtree/delete/', EconDelete.as_view()),
]