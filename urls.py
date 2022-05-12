from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('Packages', views.Packages, name='Packages'),
    path('Reviews', views.Reviews, name='Reviews'), 
    path('AboutUs', views.AboutUs, name='AboutUs'),
    path('Tourdetails', views.Tourdetails, name='Tourdetails'),
    path('Gallery', views.Gallery, name='Gallery'),
    path('book', views.book, name='book'),
    path('Info', views.Info, name='Info'),
    path('Payment', views.Payment, name='Payment'),
    path('paynow', views.paynow, name='paynow'),
    path('Display', views.Display, name='Display'),
]