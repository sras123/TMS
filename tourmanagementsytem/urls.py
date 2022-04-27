from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('login', views.login, name='login'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('logout', views.logout, name='logout'),
    
]