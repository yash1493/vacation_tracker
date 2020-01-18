from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
from calen.models import Vacation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.

@login_required
def home(request):
    return render(request,'home.html')

def addemployee(request):
    if request.method == 'POST':
        emp_id=request.POST['employeeid']
        print(Employee.objects.filter(EmpId=emp_id).count())
        if Employee.objects.filter(EmpId=emp_id).count() != 0:
            return render(request,'addEmployee.html',{'errorCode':'Employee with Id ( %s ) already exists !!' % (emp_id)})
        emp_name=request.POST['employeename']
        employee=Employee.objects.create(
            EmpName=emp_name,
            EmpId=emp_id
        )
        return redirect('manageEmployee')
    return render(request,'addEmployee.html')

@permission_required("board.delete_employee")
def deleteemployee(request):
    employee=Employee.objects.all()
    if request.method == 'POST':
        UniqueId=request.POST.get('employeeid')
        Employee.objects.get(EmpId=UniqueId).delete()
        return redirect('manageEmployee')
    return render(request,'deleteEmployee.html',{'employee':employee})

@login_required
def manageEmployee(request):
    employee=Employee.objects.all()
    return render(request,'manageEmployee.html',{'employee':employee})

def deleteVacation(request):
    employee=Employee.objects.all()
    if request.method == 'POST' and request.POST.get('employee') != None:
        UniqueId=request.POST.get('employee')
        vacation=Vacation.objects.filter(EmpId=UniqueId)
        return render(request,'deleteVacation.html',{'employee':employee,'vacation':vacation})
    if request.method == 'POST' and request.POST.get('deleteid') != None:
        UniqueId=request.POST.get('deleteid')
        Vacation.objects.get(VacationId=UniqueId).delete()
        return render(request,'deleteVacation.html',{'employee':employee})
    return render(request,'deleteVacation.html',{'employee':employee})
