from django.db import models
from profiles.models import Staff,Organization 
from django.urls import reverse

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='reports',blank=True)
    remark = models.TextField()
    author = models.ForeignKey(Staff,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        
        return str(self.name)

    def get_absolute_url(self):

        return reverse("reports:detail",kwargs={'pk':self.pk})
