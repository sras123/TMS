from distutils.command.upload import upload
from statistics import mode
from django.db import models



class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    # offer = models.BooleanField(default=False)

    
class ClientReview(models.Model):
    desc = models.TextField()
    user = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    

class TourGallery(models.Model):
    img= models.ImageField(upload_to='pics')
    gallerytitle = models.CharField(max_length=100)


     
# class packagedetail(models.Model):
#     img1= models.ImageField(upload_to='pics')
#     # img2= models.ImageField(upload_to='pics')
#     # img3= models.ImageField(upload_to='pics')
#     # img4= models.ImageField(upload_to='pics')
#     destinationtitle = models.CharField(max_length=100)
#     desc= models.TextField()
     


    
       

       


    

    
    