from django.db import models
from django.contrib.auth.models import User


class moshina(models.Model):
    car_name=models.CharField(max_length=60)
    car_model=models.CharField(max_length=40)
    car_price=models.IntegerField()
    car_company=models.CharField(max_length=60)



# Create your models here.
