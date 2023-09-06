"""
The module for all url paths for the user_auth application.
"""
from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('login/', views.user_login, name='login'),# The url path to the login page.
    path('register/user_auth/login/', views.user_login, name='login_on_after_registration'),# The url path which takes you to the login page after registration.
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),# The url path to authenticate user but is not rendered.
    path('authenticate_user/show_user', views.show_user, name='show_user'),# The url path to user page.
    path('register/', views.register_request, name="register"),# The url path to registration page.
    path('logout/', views.user_logout, name="logout"),# The url path to logout page. 
    
]
