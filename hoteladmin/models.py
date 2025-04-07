from django.db import models

class AdminModel(models.Model):
    hotelname = models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    roomcategory = models.CharField(max_length=100)
    actype=models.CharField(max_length=100)
    uploadimage = models.ImageField()
    amount=models.IntegerField()

