from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import Employee
from django.contrib.auth.decorators import login_required
from ..forms import EmployeeForm
from django.contrib import messages
from rest_framework.authtoken.models import Token


# -------------------------------------- Employee
@login_required(login_url='login')
def listEmployee(request):
    employees = Employee.objects.all()
    template_name = 'app/employee.html'
    return render(request, template_name, {'employees': employees})


@login_required(login_url='login')
def addEmployee(request):
    form = EmployeeForm(request.POST or None)
    template_name = 'app/form.html'
    page_name = 'Add Employee'
    if request.method == 'POST':
        if form.is_valid():
            form.set_password(form.password)
            employee = form.save()
            employee.set_password(employee.password)
            Token.objects.create(user=employee)
            employee.save()
            messages.success(request, 'New Employee')
            return redirect('list_employee')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def editEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    template_name = 'app/form.html'
    page_name = 'Employee Edited '
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            employee.set_password(employee.password)
            Token.objects.create(user=employee)
            employee.save()
            return redirect('list_employee')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteEmployee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'Employee Deleted ')
    return redirect('list_employee')
