from django.shortcuts import render, get_object_or_404, \
    redirect

from ..models import Workplace
from django.contrib.auth.decorators import login_required
from ..forms import WorkplaceForm
from django.contrib import messages


# -------------------------------------- Workplace
@login_required(login_url='login')
def listWorkplace(request):
    user_company = request.user.worksAtCompany_id
    workplaces = Workplace.objects.filter(company=user_company)
    template_name = 'app/workplace.html'
    return render(request, template_name, {'workplaces': workplaces})


@login_required(login_url='login')
def addWorkplace(request):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        form = WorkplaceForm(request.POST or None)
        template_name = 'app/form.html'
        page_name = 'Add Workplace'
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'New Workplace ')
                return redirect('list_workplace')
        return render(request, template_name, {'form': form, 'pageName': page_name})
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_workplace')


@login_required(login_url='login')
def editWorkplace(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
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
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_workplace')


@login_required(login_url='login')
def deleteWorkplace(request, pk):
    is_manager = request.user.groups.filter(name='manager').exists()
    if is_manager:
        workplace = get_object_or_404(Workplace, pk=pk)
        workplace.delete()
        messages.success(request, 'Workplace deleted')
        return redirect('list_workplace')
    messages.error(request, 'Não tem permissão para aceder a pagina')
    return redirect('list_workplace')
