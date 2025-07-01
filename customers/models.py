from django.db import models
from profiles.models import Organization
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="customers",default= "no_headshot.png")
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

