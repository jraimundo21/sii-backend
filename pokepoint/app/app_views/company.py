from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import Company
from django.contrib.auth.decorators import login_required
from ..forms import CompanyForm
from django.contrib import messages


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
