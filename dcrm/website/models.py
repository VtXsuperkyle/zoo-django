from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class zoo_user(AbstractUser):


    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class zoo_booking(models.Model):
    creation_data = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    Date = models.DateField()
    Time = models.TimeField()
    Price = models.FloatField(max_length = 5)