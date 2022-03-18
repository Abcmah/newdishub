from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.login_user, name='login-form'),
    path('logout',views.logout_usr, name='logout'),
]