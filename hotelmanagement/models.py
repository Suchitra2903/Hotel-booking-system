from django.db import models

# Create your models here.
from hoteladmin.models import AdminModel


class UserRegistration(models.Model):
    firstname = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class RequestModel(models.Model):
    userId=models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
    hotel=models.ForeignKey(AdminModel,on_delete=models.CASCADE)
    requeststatus=models.CharField(default='pending', max_length=200)



