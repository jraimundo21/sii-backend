from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import CheckIn, TimeCard, CheckOut, Employee
from django.contrib.auth.decorators import login_required
from ..forms import CheckinForm
from django.contrib import messages


# -------------------------------------- Checkin

@login_required(login_url='login')
def listCheckin(request):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        check_list = CheckIn.objects.all()
    else:
        check_list = CheckIn.objects.filter(timeCard__employee=request.user)
    template_name = 'app/checkin.html'
    return render(request, template_name, {'checkList': check_list})


@login_required(login_url='login')
def addCheckin(request):
    form = CheckinForm(request.POST or None)
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        n = 1  # form.employee.hidden_widget
    template_name = 'app/form.html'
    page_name = 'Add Checkin'
    timecard = TimeCard.objects.filter(employee=request.user).last()
    if timecard:
        checkout = CheckOut.objects.filter(timeCard=timecard).last()
        if not checkout:
            messages.error(request, 'Não é permitido fazer o checkIn, porfavor verifique se tem checkOut por realizar')
            return redirect('list_checkin')
    if request.method == 'POST':
        # save timeCard with
        time_card = TimeCard()
        time_card.employee = request.user
        time_card.save()
        # add timeCard in dictionary
        form.set_timeCard(time_card.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-in')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def addCheckinByManager(request, pk):
    form = CheckinForm(request.POST or None)
    template_name = 'app/form.html'
    page_name = 'Add Checkin'
    employee = Employee.objects.get(id=pk)
    timecard = TimeCard.objects.filter(employee=employee).last()
    if timecard:
        checkout = CheckOut.objects.filter(timeCard=timecard).last()
        if not checkout:
            messages.error(request, 'Não é permitido fazer o checkIn, porfavor verifique se tem checkOut por realizar')
            return redirect('list_checkin')
    if request.method == 'POST':
        # save timeCard with
        time_card = TimeCard()
        time_card.employee = employee
        time_card.save()
        # add timeCard in dictionary
        form.set_timeCard(time_card.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-in festito')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteCheckin(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        checkin = get_object_or_404(CheckIn, pk=pk)
        checkin.delete()
        return redirect('list_checkin')
    messages.error(request, 'Não tem permissão para aceder a página')
    return redirect('list_checkin')
