from django.db import models

# Create your models here.
    
class Department(models.Model):
    deptno=models.PositiveIntegerField()
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    
    salary=models.PositiveIntegerField()

    def __str__(self):
        return self.ename