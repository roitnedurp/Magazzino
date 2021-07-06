from django.shortcuts import render, redirect  
from magazzino.forms import MagazzinoForm  
from magazzino.models import Magazzino  

# Create your views here.  
def maga(request):  
	if request.method == "POST":  
		form = MagazzinoForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/show')  
			except:  
				pass  
	else:  
		form = MagazzinoForm()  
	return render(request,'index.html',{'form':form})  

def show(request):  
	magazzinos = Magazzino.objects.all()  
	return render(request,"show.html",{'magazzinos':magazzinos})  

def edit(request, id):  
	magazzino = Magazzino.objects.get(id=id)  
	return render(request,'edit.html', {'magazzino':magazzino})  

def update(request, id):  
	magazzino = Magazzino.objects.get(id=id)  
	form = MagazzinoForm(request.POST, instance = magazzino)  
	if form.is_valid():  
		form.save()  
		return redirect("/show")  
	return render(request, 'edit.html', {'magazzino': magazzino})  

# old destroy def - doesn't ask for a confirmation
#def destroy(request, id):  
	#magazzino = Magazzino.objects.get(id=id)  
	#magazzino.delete()  
	#return redirect("/show")  
	
# new destroy def -  ask for a confirmation	!!! ( confirm_delete.html extend edit.html )
def destroy(request, id, template_name='confirm_delete.html'):  
    magazzino = Magazzino.objects.get(id=id)  
    form = MagazzinoForm(request.POST, instance = magazzino)  
    if request.method=='POST':
	    magazzino.delete()
	    return redirect("/show")
    return render(request, 'confirm_delete.html', {'magazzino': magazzino})  

  
