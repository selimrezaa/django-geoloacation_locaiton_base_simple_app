from django.db import models

# Create your models here.

class Mesurment(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} to {self.destination} distance {self.distance} Km "


class UserForm(models.Model):
    name = models.CharField(max_length=222)

    def __str__(self):
        return self.name
