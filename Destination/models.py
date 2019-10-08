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
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Camp(models.Model):
    name = models.CharField(max_length=150)
    destination = models.ForeignKey(
        Destination, related_name='llink', on_delete=models.CASCADE)
    place = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    LocationImage = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default="noimage.png")
    overview = HTMLField()
    checkin = models.TimeField()
    discountprice = models.IntegerField()
    originalprice = models.IntegerField()
    Food = HTMLField()
    Activities = HTMLField()
    Amenities = HTMLField()
    Details = HTMLField()
    Near = models.CharField(max_length=150, default="Free Meals")
    Meal = models.CharField(max_length=150, default="Free Meals")
    Activities = models.CharField(max_length=150, default="Activites")

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.ForeignKey(
        Destination, related_name='link', on_delete=models.CASCADE)
    ttype = models.CharField(max_length=150)
    Detail = HTMLField()

    def __str__(self):
        return self.ttype


class Explore(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name
