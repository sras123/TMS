from django.db import models



# class userInfo(models.Model):
#     username= models.CharField(max_length=200)
#     first_name= models.CharField(max_length=200)
#     last_name= models.CharField(max_length=200)
#     email= models.EmailField(max_length=254)
#     password= models.CharField(max_length=200)

class Image(models.Model):
    caption = models.CharField(max_length=50)
    image= models.ImageField(upload_to="Images/%y")

    def __str__(self):
        return self.caption