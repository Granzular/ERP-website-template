from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to="avartars",default="no_picture.png")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"profile of {self.user.username}"

class Organization(models.Model):

    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="logos",default="no_picture.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"profile of {self.user.username}"    

class Staff(models.Model):

    organization = models.ForeignKey(Organization,models.CASCADE)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to="avartars",default="no_picture.png")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"profile of {self.user.username}"