from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html') 

def add_department(request):
    return render(request,'add_department.html') 

def add_employee(request):
    return render(request,'add_employee.html') 