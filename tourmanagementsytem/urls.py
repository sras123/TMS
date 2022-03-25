from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('index', views.index, name='index'),
    
]