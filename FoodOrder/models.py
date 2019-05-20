
from django.db import models


class Food(models.Model):
    #Food_id=models.Field(primary_key=True,max_length=20)
    category=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=20)


