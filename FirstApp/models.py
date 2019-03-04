from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=25)
    def __str__(self):
        return self.dept_name  


class Employee(models.Model):
    first_name=models.CharField(max_length=25) 
    position=models.CharField(max_length=25)
    Depart=models.ForeignKey(Department,on_delete=models.CASCADE) 
    objects=models.Manager()

    def __str__(self):
        return self.first_name      
