from datetime import datetime

from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import Company, Employee, TimeCard, CheckIn, CheckOut
from django.contrib.auth.decorators import login_required
from ..forms import CompanyForm
from django.contrib import messages

# _________________________________________________________________Companies


@login_required(login_url='login')
def index(request):
    user_company = request.user.worksAtCompany_id
    company = Company.objects.get(id=user_company)
    company.cor = 'color'
    print(company)
    employee = Employee.objects.get(id=request.user.id)
    timecards = time_work(employee)
    data = {'company': company, 'timecards': timecards}
    template_name = 'app/index.html'
    return render(request, template_name, data)


def time_work(employee):
    timecards = TimeCard.objects.filter(employee=employee)
    for timecard in timecards:
        if hasattr(timecard, 'checkIn'):
            check_in_time = timecard.checkIn.timestamp
            if hasattr(timecard, 'checkOut'):
                check_out_time = timecard.checkOut.timestamp
                dif = check_out_time - check_in_time
                timecard.timeWork = dif
    return timecards


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
            messages.success(request, 'New Company  ')
            return redirect('index')
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
            messages.success(request, 'Edited company ')
            return redirect('index')
    return render(request, template_name, {'form': form, 'pageName': 'Company'})


@login_required(login_url='login')
def deleteCompany(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    messages.success(request, 'deleted  Company')
    return redirect('index')
