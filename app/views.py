from django.shortcuts import render
from app.models import *

# Create your views here.
def display_emp(request):
    QST=Emp.objects.all()
    d={'emp':QST}

    return render(request,'display emp.html',d)

    
def dept(request):
    qst=Dept.objects.all()
    d={'dpt':qst}

    return render(request,'dpt.html',d)