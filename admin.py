from django.contrib import admin
from .models import  Booking, Destinations
from .models import  Review


# Register your models here.

class users(admin.ModelAdmin):
    list_display= ('firstname', 'lastname','username', 'email','gender', 'province')


    
admin.site.register(Destinations)
admin.site.register(Review)
admin.site.register(Booking)

