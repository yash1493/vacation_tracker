from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def home(request):
    return render(request,'home.html')

def addemployee(request):
    if request.method == 'POST':
        emp_id=request.POST['employeeid']
        emp_name=request.POST['employeename']
        employee=Employee.objects.create(
            EmpName=emp_name,
            EmpId=emp_id
        )
        return redirect('manageEmployee')
    return render(request,'addEmployee.html')

def deleteemployee(request):
    employee=Employee.objects.all()
    if request.method == 'POST':
#        UniqueId=[]
        UniqueId=request.POST['employee']
        if UniqueId != "noselection":
            Employee.objects.get(id=UniqueId).delete()
        return redirect('manageEmployee')
    return render(request,'deleteEmployee.html',{'employee':employee})


def manageEmployee(request):
    employee=Employee.objects.all()
    return render(request,'manageEmployee.html',{'employee':employee})
