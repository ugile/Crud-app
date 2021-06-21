from django.db import models

# Create your models here.


class Hospital(models.Model):
    name=models.CharField(max_length=200)
    owner=models.CharField(max_length=300)
    noofdoctors=models.IntegerField()
    noofpatients=models.IntegerField()
    city=models.CharField(max_length=50)
    helplineno=models.IntegerField()

