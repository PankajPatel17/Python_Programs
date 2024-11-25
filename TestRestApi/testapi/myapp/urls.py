from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add-department/',views.add_department,name='add-department'),
    path('add-employee/',views.add_employee,name='add-employee'),
    
]