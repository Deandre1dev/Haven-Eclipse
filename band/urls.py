from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name="home"),# Url path to the home page.
    path('music/', views.music, name="music"),# Url path to the music page.
    path('tours/', views.tours, name="tours")# Url path to the tours page.
]