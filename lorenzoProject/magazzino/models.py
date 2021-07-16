from django.db import models
from django import forms

class Magazzino(models.Model):
        eid     = models.CharField(max_length=20)
        subkey  = models.CharField(max_length=20)
        ename   = models.CharField(max_length=50)
        quantity = models.IntegerField()
        code_maker  = models.CharField(max_length=20)
        code_vendor  = models.CharField(max_length=20)
        edescription = models.TextField( blank=True )
        progetto  = models.CharField(max_length=20)
        class Meta:
              db_table = "magazzino"

