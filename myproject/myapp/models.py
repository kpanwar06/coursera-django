from django.db import models

# Create your models here.
class cake_order(models.Model):
    f_name=models.CharField(max_length=100)
    order_date=models.DateField()
    cake_flavour=models.CharField(max_length=100)