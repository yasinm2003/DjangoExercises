from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addnews/', views.addnews, name="addnews"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
]