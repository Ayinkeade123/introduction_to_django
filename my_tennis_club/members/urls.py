# from django.urls import path
# from . import views

# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path ('myfirst_html/', views.myfirst_html,  name= 'myfirst_html'),
    path('login/', views.login, name='login')
]

