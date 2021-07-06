from django.contrib import admin  
from django.urls import path  
from magazzino import views  
urlpatterns = [  
	path('admin/', admin.site.urls),  
	path('maga', views.maga),  
	path('show',views.show),  
	path('edit/<int:id>', views.edit),  
	path('update/<int:id>', views.update),  
	path('delete/<int:id>', views.destroy),  
]  
