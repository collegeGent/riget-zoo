from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ZooUser(AbstractUser):
    houseNum = models.IntegerField(null=True)
    street = models.CharField(max_length=50)
    postCode = models.CharField(max_length=8)
    phoneNum = models.CharField(max_length=12)
    points = models.IntegerField(default=0)

class zooBooking(models.Model):
    zooID = models.AutoField(primary_key=True)
    custID = models.ForeignKey("rigetZoo.ZooUser", on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    creation_data = models.DateTimeField(auto_now_add=True)

class hotelBooking(models.Model):
    hotelD = models.AutoField(primary_key=True)
    custID = models.ForeignKey("rigetZoo.ZooUser", on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    creation_data = models.DateTimeField(auto_now_add=True)