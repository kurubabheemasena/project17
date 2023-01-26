from django.db import models

# Create your models here.

class Dept(models.Model):
  deptno=models.IntegerField(primary_key=True)
  dname=models.CharField(max_length=100)
  
  def __str__(self):
    return self.dname
  
  
  

class Emp(models.Model):
  ename=models.CharField(max_length=100)
  job=models.CharField(max_length=100)
  sal=models.IntegerField()
  deptno=models.ForeignKey(Dept, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.ename




    
