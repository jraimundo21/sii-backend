from django.shortcuts import render, get_object_or_404, \
    redirect

from django.contrib.auth import logout
from .models import Employee, TimeCard, CheckIn, Company, Workplace, CheckOut
from django.contrib.auth.decorators import login_required
from .forms import CheckinForm, WorkplaceForm, CheckOutForm, CompanyForm, EmployeeForm
from django.contrib import messages
from rest_framework.authtoken.models import Token


# =======App  ======
# _______Login

def logoutUser(request):
    logout(request)
    return redirect('login')


# _________________________________________________________________Companies
@login_required(login_url='login')
def index(request):
    template_name = 'app/index.html'
    return render(request, template_name)


@login_required(login_url='login')
def listCompany(request):
    companies = Company.objects.all()
    template_name = 'app/company.html'
    return render(request, template_name, {'companies': companies})


@login_required(login_url='login')
def addCompany(request):
    form = CompanyForm(request.POST or None)
    template_name = 'app/form.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New comany ')
            return redirect('list_company')
    return render(request, template_name, {'form': form})


@login_required(login_url='login')
def editCompany(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    template_name = 'app/form.html'
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edited comany ')
            return redirect('list_company')
    return render(request, template_name, {'form': form, 'pageName': 'Workplace'})


@login_required(login_url='login')
def deleteCompany(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    messages.success(request, 'deleted  comany ')
    return redirect('list_company')


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


# -------------------------------------- Workplace
@login_required(login_url='login')
def listWorkplace(request):
    workplaces = Workplace.objects.all()
    template_name = 'app/workplace.html'
    return render(request, template_name, {'workplaces': workplaces})


@login_required(login_url='login')
def addWorkplace(request):
    form = WorkplaceForm(request.POST or None)
    template_name = 'app/form.html'
    page_name = 'Add Workplace'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Workplace ')
            return redirect('list_workplace')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def editWorkplace(request, pk):
    workplace = Workplace.objects.get(id=pk)
    form = WorkplaceForm(instance=workplace)
    template_name = 'app/form.html'
    page_name = 'Editor Workplace'
    if request.method == 'POST':
        form = WorkplaceForm(request.POST, instance=workplace)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workplace Edited')
            return redirect('list_workplace')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteWorkplace(request, pk):
    workplace = get_object_or_404(Workplace, pk=pk)
    workplace.delete()
    messages.success(request, 'Workplace deleted')
    return redirect('list_workplace')


# -------------------------------------- Checkin

@login_required(login_url='login')
def listCheckin(request):
    check_list = CheckIn.objects.all()
    template_name = 'app/checkin.html'
    return render(request, template_name, {'checkList': check_list})


@login_required(login_url='login')
def addCheckin(request):
    form = CheckinForm(request.POST or None)
    template_name = 'app/form.html'
    page_name = 'Add Checkin'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-in ')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def editCheckin(request, pk):
    checkin = CheckIn.objects.get(id=pk)
    form = CheckinForm(instance=checkin)
    template_name = 'app/form.html'
    page_name = 'Add Checkin'
    if request.method == 'POST':
        form = CheckinForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check-in Edited')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteCheckin(request, pk):
    checkin = get_object_or_404(CheckIn, pk=pk)
    checkin.delete()
    return redirect('list_checkin')


# -------------------------------------- Checkin

@login_required(login_url='login')
def listCheckout(request):
    checklist = CheckOut.objects.all()
    template_name = 'app/checkout.html'
    return render(request, template_name, {'checklist': checklist})


@login_required(login_url='login')
def addCheckout(request):
    form = CheckOutForm(request.POST or None)
    template_name = 'app/form.html'
    page_name = 'Adicionar Checkout'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-out')
            return redirect('list_checkOut')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def editCheckout(request, pk):
    check_out = CheckOut.objects.get(id=pk)
    form = CheckOutForm(instance=check_out)
    template_name = 'app/form.html'
    page_name = 'Edit Checkin'
    if request.method == 'POST':
        form = CheckOutForm(request.POST, instance=check_out)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check-out Edited')
            return redirect('list_checkOut')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteCheckout(request, pk):
    check_out = get_object_or_404(CheckOut, pk=pk)
    check_out.delete()
    messages.success(request, 'Check-out Deleted ')
    return redirect('list_checkOut')
