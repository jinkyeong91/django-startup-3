from django.db import models
from django.forms import CharField
from django.db  import  models
# Create your models here.

class Inquiry(models.Model):
    fullname=models.CharField(max_length=64, blank=True, null=True)
    email_adress=models.CharField(max_length=64, blank=True, null=True)
    phone_number=models.CharField(max_length=32, blank=True, null=True)
    message=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at=models.DateTimeField(auto_now=True)



