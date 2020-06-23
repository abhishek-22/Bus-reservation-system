from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class BusDet(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    seats = models.IntegerField(default=35,
                                validators=[
                                    MaxValueValidator(35),
                                    MinValueValidator(0)
                                ])
    cost = models.IntegerField(default=400)
class Bookingdets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(BusDet, on_delete=models.CASCADE)
    nos = models.IntegerField()
    
    

     
