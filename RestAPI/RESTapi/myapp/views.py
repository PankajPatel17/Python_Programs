from django.shortcuts import render
from rest_framework import generics
from .models import Department,Employee
from .serializers import DepartmentSerializers,EmployeeSerializers

# Create your views here.
class DepartmentList(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializers

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Department
    serializer_class=DepartmentSerializers

class EmployeeList(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee
    serializer_class=EmployeeSerializers