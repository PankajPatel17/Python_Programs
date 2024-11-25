from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_register, name='doctor_register'),
    path('patient/', views.patient_register, name='patient_register'),
    path('login/', views.login_view, name='login'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient/book_appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
]
