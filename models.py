from django.db import models

from django.forms import CharField


# class userInfo(models.Model):
#     username= models.CharField(max_length=200)
#     first_name= models.CharField(max_length=200)
#     last_name= models.CharField(max_length=200)
#     email= models.EmailField(max_length=254)
#     password= models.CharField(max_length=200)



class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Review(models.Model):
    review_name = models.CharField(max_length=100)
    review = models.CharField(max_length=500)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    booking = models.TextField()
    price = models.IntegerField()

