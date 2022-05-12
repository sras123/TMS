from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail

from .models import Destinations, ClientReview, TourGallery






# Create your views here.
def home(request):
    return render(request, 'home.html')



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




def createAccount(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
 
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('createAccount')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('createAccount')
            else:
               user = User.objects.create_user(username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save();
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


def admin(request):
    
    return render(request, 'admin')


def Packages(request):
    dests = Destinations.objects.all()
    
    return render(request, 'Packages.html', {'dests': dests})




def AboutUs(request):
     return render(request, 'AboutUs.html')
    
    
   
def Reviews(request):
    Review = ClientReview.objects.all()

    return render(request, 'Reviews.html', {'Review': Review})

def Gallery(request):

    Image= TourGallery.objects.all()
    return render(request, 'Gallery.html',{'Image':Image})


# def Booking(request):
#      return render(request, 'Booking.html')

def book(request):
    
    return render(request, 'book.html')


def Tourdetails(request):
    
    return render(request, 'Tourdetails.html')


def Payment(request):
    
    return render(request, 'Payment.html')

def paynow(request):
  
    return render(request, 'paynow.html')

def Display(request):
  
    return render(request, 'Display.html')
    
    
   

def Info(request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        address= request.POST['address']
        location= request.POST['location']
        guests= request.POST['guests']
        arrivals= request.POST['arrivals']
        leaving= request.POST['leaving']

        #send an email
        booking= "Name: "+ name+"\n"+ "Phone:"+ phone + "\n"+"Email:" + email +"\n" +"Address:" + address +"\n"+ "Location:"+ location + "\n"+"No of people:" + guests + "\n"+"Arrivals:" +arrivals +"\n"+ "Leaving:" + leaving+"\n"
        
        send_mail(
            'Approve Package',
            booking,
            email,
            ['tourmanagement2001@gmail.com'],
        )
    return render(request, 'Info.html', {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address,
        'location': location,
        'guests':guests,
        'arrivals': arrivals,
        'leaving': leaving
    })

