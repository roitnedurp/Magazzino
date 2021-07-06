from django import forms  
from magazzino.models import Magazzino  

class MagazzinoForm(forms.ModelForm):  
	class Meta:  
		model = Magazzino  
		fields = "__all__"  
