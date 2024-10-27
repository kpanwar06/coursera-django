from django.db import models

# Create your models here.
class cake_order(models.Model):
    flavours=((1,"Chocolate"),(2,"Strawberry"),(3,"Vanilla"))
    f_name=models.CharField(max_length=100)
    order_date=models.DateField()
    cake_flavour=models.IntegerField(choices=flavours)

    def __str__(self):
        return self.f_name

class customer_details(models.Model):
    f_name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    customer_id=models.ForeignKey(cake_order,on_delete=models.PROTECT,default=None)
    def __str__(self):
        return self.f_name