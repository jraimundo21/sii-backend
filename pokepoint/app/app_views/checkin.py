from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import CheckIn
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
    template_name = 'app/form.html'
    page_name = 'Add Checkin'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-in ')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': page_name})


@login_required(login_url='login')
def deleteCheckin(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        checkin = get_object_or_404(CheckIn, pk=pk)
        checkin.delete()
        return redirect('list_checkin')
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_checkin')
