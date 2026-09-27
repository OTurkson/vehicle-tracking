from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicle = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=12, unique=True)
    chassis_number = models.CharField(max_length=50, unique=True)
    tyre_size = models.CharField(max_length=20)
    tyre_quantity = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True)

    # Timestamps for admin to track but not for user view
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
