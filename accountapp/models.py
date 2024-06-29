from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=60)
    user_last_name=models.CharField(max_length=60)
    user_phone_number=models.CharField(max_length=60)
    user_email=models.CharField(max_length=60)


class clent(models.Model):
    clent_name=models.CharField(max_length=70)
    clent_last_name=models.CharField(max_length=70)

