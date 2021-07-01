from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, logout, login
from rest_framework.authtoken.models import Token

# _______Login
from ..forms import CompanyForm, EmployeeForm, EmployeeFormCreate


def home(request):
    template_name = 'app/home.html'
    return render(request, template_name)


def logoutUser(request):
    logout(request)
    return redirect('index')


def register(request):
    template_name = 'registration/register.html'
    page_name = 'Employee Edited '
    form_company = CompanyForm(request.POST or None)
    form_employee = EmployeeFormCreate(request.POST or None)
    if request.method == 'POST':
        if form_company and form_employee:
            company = form_company.save()
            form_employee.set_username(form_employee.data['email'])
            form_employee.set_worksAtCompany(company.id)
            employee = form_employee.save()
            employee.set_password(employee.password)
            employee.save()
            manager = Group.objects.get(name='manager')
            employee.groups.add(manager)
            Token.objects.create(user=employee)
            messages.success(request, 'Conta criada com sucesso')
            user = authenticate(request, username=employee.email, password=form_employee.data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')

    return render(request, template_name,
                  {'form_company': form_company, 'form_employee': form_employee, 'pageName': page_name})
