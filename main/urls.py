from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('',index, name = 'home'),
    path('login',user_login, name = 'login'),
    path('register',register, name = 'register'),
    path('logout', logout_user, name = 'logout'),  
    path('add_expense', add_expense,  name = 'add_expense'), 
    path('settings', settings, name = "settings")
]
