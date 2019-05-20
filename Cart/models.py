from django.db import models
from login.models import register
#from FoodOrder.models import Food

class OrderDetails(models.Model):
    username = models.ForeignKey(register, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(max_length=10)
    date = models.DateField('date published')

