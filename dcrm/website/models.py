from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class zoo_user(AbstractUser):
    points = models.IntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    city = models.CharField(max_length=50, blank=True)
    
class zoo_booking(models.Model):
    creation_data = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    Date = models.DateField()
    Time = models.TimeField()
    Price = models.FloatField(max_length = 5)
    
class HotelBooking(models.Model):
    booking_id = models.AutoField(primary_key=True, editable=False)
    hotel_user_id = models.ForeignKey(zoo_user, on_delete=models.CASCADE)
    hotel_booking_date = models.DateField(auto_now_add=True)
    hotel_booking_date_arrive = models.DateField()
    hotel_booking_date_leave = models.DateField()
    hotel_booking_adults = models.IntegerField(default=0)
    hotel_booking_children = models.IntegerField(default=0)
    hotel_booking_oap = models.IntegerField(default=0)
    hotel_total_cost = models.FloatField(default=0)
    hotel_points = models.IntegerField(default=0)

