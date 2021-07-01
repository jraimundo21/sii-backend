from django.shortcuts import render, get_object_or_404, \
    redirect
from rest_framework import status
from rest_framework.response import Response

from . import time_work
from ..models import Employee
from django.contrib.auth.decorators import login_required
from ..forms import EmployeeForm, MonthForm
from django.contrib import messages
from rest_framework.authtoken.models import Token


# -------------------------------------- Employee
@login_required(login_url='login')
def listEmployee(request):
    user_company = request.user.worksAtCompany_id
    employees = Employee.objects.filter(worksAtCompany=user_company)
    is_manager = request.user.groups.filter(name='manager').exists()
    template_name = 'app/employee.html'
    return render(request, template_name, {'employees': employees, 'ismanager':is_manager})


@login_required(login_url='login')
def addEmployee(request):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        form = EmployeeForm(request.POST or None)
        page_name = 'Add Employee'
        template_name = 'app/form.html'
        if request.method == 'POST':
            if form.is_valid():
                employee = form.save()
                employee.set_password(employee.password)
                Token.objects.create(user=employee)
                employee.save()
                messages.success(request, 'New Employee')
                return redirect('list_employee')
        return render(request, template_name, {'form': form, 'pageName': page_name})
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_employee')


@login_required(login_url='login')
def showEmployee(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager or pk == request.user.id:
        employee = Employee.objects.get(id=pk)
        query = request.GET.get("months_Year")
        monthForm = MonthForm(initial={'months_Year': query})
        (timecards, workHours) = time_work(query, employee)
        data = {'employee': employee, 'timecards': timecards, 'monthForm': monthForm, 'workHours': workHours}
        template_name = 'app/showEmployee.html'
        return render(request, template_name, data)
    messages.error(request, 'Não tem permissão para aceder a página')
    return redirect('list_employee')

@login_required(login_url='login')
def editEmployee(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager or pk == request.user.id:
        employee = Employee.objects.get(id=pk)
        form = EmployeeForm(instance=employee)
        template_name = 'app/form.html'
        page_name = 'Employee Edited '
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                employee = form.save()
                employee.set_password(employee.password)
                employee.save()
                return redirect('list_employee')
        return render(request, template_name, {'form': form, 'pageName': page_name})
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_employee')


@login_required(login_url='login')
def deleteEmployee(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        messages.success(request, 'Employee Deleted ')
        return redirect('list_employee')
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_employee')
