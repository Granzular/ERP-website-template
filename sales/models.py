from django.db import models
from products.models import Product
from profiles.models import Staff,Organization
from customers.models import Customer
from django.utils import timezone
from .utils import generate_code
from django.urls import reverse

# Create your models here.

class Position(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)

    def save(self,*args,**kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"id: {self.id} product: {self.product.name} quantity: {self.quantity}"

    def get_sales_id(self):
        sales_id = self.sale_set.first().id
        return sales_id


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12,blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    salesman = models.ForeignKey(Staff,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"sales for the amount of ${self.total_price}"

    def save(self,*args,**kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args,**kwargs)

    def get_positions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse("sales:detail",kwargs={'pk':self.id})


class CSV(models.Model):
   file_name = models.FileField(upload_to="csvs")
   activated = models.BooleanField(default=False)
   organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   def __str__(self):
       return str(self.file_name)
