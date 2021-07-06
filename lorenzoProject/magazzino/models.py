from django.db import models  
from django import forms

class Magazzino(models.Model):  
	eid     = models.CharField(max_length=20)  
	subkey  = models.CharField(max_length=20)  
	ename   = models.CharField(max_length=100)  
	eefirm  = models.CharField(max_length=100)  
	edescription = models.TextField( blank=True )  
	class Meta:  
		db_table = "magazzino"  

 
