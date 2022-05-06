from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.models import Group

from .models import Destinations, Review
from .decorators import unauthenticated_user, allowed_users, admin_only



# Create your views here.
# @allowed_users(allowed_roles=['users','admins'])
def home(request):
    return render(request, 'home.html')

@unauthenticated_user   
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        
    else:
        return render(request,'login.html')



@unauthenticated_user
def createAccount(request):


    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        gender = request.POST['gender']
        province = request.POST['province']

        print(gender)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('createAccount')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('createAccount')
            else:
               user = User.objects.create_user(username,password=password1,email=email,first_name=first_name,last_name=last_name, gender=gender, province=province)
               user.save()
               print(request,'user created')
               return redirect('login')
        else:
            messages.info(request,'password not matching..')
            return redirect('createAccount')
        return redirect('/')

    else: 
      return render(request, 'createAccount.html')

def forgotpass(request):
    return render(request, 'forgotpass.html')



def logout(request):
    auth.logout(request)
    return redirect('login')

def review(request):
    
    return render(request, 'review')


@admin_only
def admin(request):
    
    return render(request, 'admin')


def packages(request):
    dests = Destinations.objects.all()
    
    return render(request, 'packages.html', {'dests': dests})
   

def review(request):
    # Review = Review.objects.all()
    
    return render(request, 'review.html', {'Review': Review})


def booking(request):
    Booking = Review.objects.all()
    
    return render(request, 'booking.html', {'Booking': Booking})