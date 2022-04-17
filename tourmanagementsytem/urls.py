from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('Tourpackages', views.Tourpackages, name='Tourpackages'),
    path('AboutUs', views.AboutUs, name='AboutUs'),
    
]
