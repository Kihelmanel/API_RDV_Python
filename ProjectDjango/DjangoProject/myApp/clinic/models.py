from django.db import models


# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField(null=True)



