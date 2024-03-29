from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models

class User(BaseUser):
    objects = BaseUserManager()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
   
class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="contact", null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    relationship = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    notes = models.CharField(max_length=30)
   