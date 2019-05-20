from django.db import models
import datetime

# Create your models here.

def genrate():
    if booktable.objects.all()!="":
        id ='D'+ str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2)
        temp=booktable.objects.all().count()
        temp="{0:0=3d}".format(temp)
        id=id+temp
        return id
    else:
        return 'D201803000'

class booktable(models.Model):
    id=models.CharField(max_length=20,default=genrate,editable=False,primary_key=True)
    type=models.CharField(max_length=50)
    people=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
