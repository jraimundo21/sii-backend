from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import CheckOut, TimeCard, Employee
from django.contrib.auth.decorators import login_required
from ..forms import CheckOutForm
from django.contrib import messages


# -------------------------------------- Checkout

@login_required(login_url='login')
def listCheckout(request):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        checklist = CheckOut.objects.all()
    else:
        checklist = CheckOut.objects.filter(timeCard__employee=request.user)
    template_name = 'app/checkout.html'
    return render(request, template_name, {'checklist': checklist})


@login_required(login_url='login')
def addCheckout(request):
    form = CheckOutForm(request.POST or None)
    template_name = 'app/form.html'
    page_name = 'Adicionar Checkout'
    timecard = TimeCard.objects.filter(employee=request.user).last()
    if not timecard:
        messages.error(request, 'Não é permitido adcionar um check-out ')
        return redirect('list_checkout')
    checkout = CheckOut.objects.filter(timeCard=timecard).last()
    if checkout:
        messages.error(request, 'Não é permitido adcionar um check-out ')
        return redirect('list_checkout')
    if request.method == 'POST':
        form.set_timeCard(timecard.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-out')
            return redirect('list_checkout')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def addCheckOutByManager(request, pk):
    form = CheckOutForm(request.POST or None)
    employee = Employee.objects.get(id=pk)
    template_name = 'app/form.html'
    page_name = 'Adicionar Checkout'
    timecard = TimeCard.objects.filter(employee=employee).last()
    if not timecard:
        messages.error(request, 'Não é permitido adcionar um check-out ')
        return redirect('list_checkout')
    checkout = CheckOut.objects.filter(timeCard=timecard).last()
    if checkout:
        messages.error(request, 'Não é permitido adcionar um check-out ')
        return redirect('list_checkout')
    if request.method == 'POST':
        form.set_timeCard(timecard.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-out')
            return redirect('list_checkout')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteCheckout(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        check_out = get_object_or_404(CheckOut, pk=pk)
        check_out.delete()
        messages.success(request, 'Check-out Deleted ')
        return redirect('list_checkout')
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_checkout')
