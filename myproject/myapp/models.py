from django.db import models

# Create your models here.
class cake_order(models.Model):
    flavours=((1,"Chocolate"),(2,"Strawberry"),(3,"Vanilla"))
    f_name=models.CharField(max_length=100)
    order_date=models.DateField()
    cake_flavour=models.IntegerField(max_length=10,choices=flavours)