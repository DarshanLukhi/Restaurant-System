from django.db import models

class register(models.Model):
    fName=models.CharField(max_length=20)
    lName=models.CharField(max_length=20)
    username=models.CharField(max_length=20,primary_key=True)
    gmail=models.CharField(max_length=40)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lName