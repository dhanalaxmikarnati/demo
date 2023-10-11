from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class Destination(models.Model):
    dscrp=models.TextField()
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    