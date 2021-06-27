from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import CheckOut
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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-out')
            return redirect('list_checkOut')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def editCheckout(request, pk):
    checkin = check_out = CheckOut.objects.filter(id=pk, timeCard__employee=request.user)
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager or checkin:
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
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_checkin')


@login_required(login_url='login')
def deleteCheckout(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        check_out = get_object_or_404(CheckOut, pk=pk)
        check_out.delete()
        messages.success(request, 'Check-out Deleted ')
        return redirect('list_checkOut')
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_checkin')
