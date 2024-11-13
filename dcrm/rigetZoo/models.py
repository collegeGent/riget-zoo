from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ZooUser(AbstractUser):
    houseNum = models.IntegerField(null=True)
    street = models.CharField(max_length=50)
    postCode = models.CharField(max_length=8)
    phoneNum = models.CharField(max_length=12)
    points = models.IntegerField(default=0)
