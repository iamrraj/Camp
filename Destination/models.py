from django.db import models
import datetime
from tinymce.models import HTMLField
from django.utils import timezone
from markdown_deux import markdown
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
# Create your models here.

class Destination(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  image = models.ImageField(upload_to='photos/%Y/%m/%d/') 



class Camp(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.ForeignKey(Destination, related_name='llink', on_delete=models.CASCADE)
  Place = models.CharField(max_length=150)
  image = models.ImageField(upload_to='photos/%Y/%m/%d/') 
  price = models.IntegerField()
  originalprice = models.IntegerField()
  Food =HTMLField()
  Activities = HTMLField()
  Amenities = HTMLField()
  Details  = HTMLField()
  Location = HTMLField()
  LocationImage = models.ImageField(upload_to='photos/%Y/%m/%d/', default="noimage.png") 
  Near = models.CharField(max_length=150, default = "Free Meals")
  Meal = models.CharField(max_length=150, default = "Free Meals")
  Activities = models.CharField(max_length=150, default = "Activites")
  Pool = models.CharField(max_length=150, default = "Swimming Pool")
  Music = models.CharField(max_length=150, default = "Dj Music")



  
class Type(models.Model):
  name = models.ForeignKey(Destination, related_name='link', on_delete=models.CASCADE)
  place = models.CharField(max_length=150,default="none")
  price = models.IntegerField()
  Bed = models.CharField(max_length=150)
  Extra = HTMLField()

 
  

