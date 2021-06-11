from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, \
    HttpResponseRedirect, reverse, redirect

from rest_framework.views import APIView, Response, status

#from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

# Auth
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from .models import Employee, TimeCard, CheckIn, Company, Workplace, CheckOut
from .serializers import EmployeeSerializer, TimeCardSerializer, CheckInSerializer, \
    CheckOutSerializer, CompanySerializer, WorkplaceSerializer, UserSerializer
from django.contrib.auth.decorators import login_required


from .forms import EmployeeForm, CheckinForm, WorkplaceForm, CheckOutForm, CompanyForm
from django.contrib import messages


# =======App  ======
# _______Login

def logoutUser(request):
    logout(request)
    return redirect('login')


# _________________________________________________________________Companies
@login_required(login_url='login')
def index(request):
    # employee =Employee.objects.get(user= request.user.id )
    # if(request.user.id==
    # company = Company.objects.get(id=pk)
    template_name = 'app/index.html'
    return render(request, template_name)


@login_required(login_url='login')
def listCompany(request):
    companies = Company.objects.all()
    template_name = 'app/company.html'
    return render(request, template_name, {'companys': companies})


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
    pageName = 'Adcionar Employee'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Employee')
            return redirect('list_employee')
    return render(request, template_name, {'form': form, 'pageName': pageName})


@login_required(login_url='login')
def editEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    template_name = 'app/form.html'
    pageName = 'Employee Edited '
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
    return render(request, template_name, {'form': form, 'pageName': pageName})


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
    pageName = 'Adicionar Workpalce'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Workplace ')
            return redirect('list_workplace')
    return render(request, template_name, {'form': form, 'pageName': pageName})


@login_required(login_url='login')
def editWorkplace(request, pk):
    workplace = Workplace.objects.get(id=pk)
    form = WorkplaceForm(instance=workplace)
    template_name = 'app/form.html'
    pageName = 'Editar Workplace'
    if request.method == 'POST':
        form = WorkplaceForm(request.POST, instance=workplace)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workplace Edited')
            return redirect('list_workplace')
    return render(request, template_name, {'form': form, 'pageName': pageName})


@login_required(login_url='login')
def deleteWorkplace(request, pk):
    workplace = get_object_or_404(Workplace, pk=pk)
    workplace.delete()
    messages.success(request, 'Workplace deleted')
    return redirect('list_workplace')


# -------------------------------------- Checkin

@login_required(login_url='login')
def listCheckin(request):
    checkList = CheckIn.objects.all()
    template_name = 'app/checkin.html'
    return render(request, template_name, {'checkList': checkList})


@login_required(login_url='login')
def addCheckin(request):
    form = CheckinForm(request.POST or None)
    template_name = 'app/form.html'
    pageName = 'Adicionar Checkin'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-in ')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': pageName})


@login_required(login_url='login')
def editCheckin(request, pk):
    checkin = CheckIn.objects.get(id=pk)
    form = CheckinForm(instance=checkin)
    template_name = 'app/form.html'
    pageName = 'Adicionar Checkin'
    if request.method == 'POST':
        form = CheckinForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check-in Edited')
            return redirect('list_checkin')
    return render(request, template_name, {'form': form, 'pageName': pageName})


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
    pageName = 'Adicionar Checkout'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New Check-out')
            return redirect('list_checkOut')
    return render(request, template_name, {'form': form, 'pageName': pageName})


@login_required(login_url='login')
def editCheckout(request, pk):
    checkOut = CheckOut.objects.get(id=pk)
    form = CheckOutForm(instance=checkOut)
    template_name = 'app/form.html'
    pageName = 'Editar Checkin'
    if request.method == 'POST':
        form = CheckOutForm(request.POST, instance=checkOut)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check-outEdited')
            return redirect('list_checkOut')
    return render(request, template_name, {'form': form, 'pageName': pageName})


@login_required(login_url='login')
def deleteCheckout(request, pk):
    checkOut = get_object_or_404(CheckOut, pk=pk)
    checkOut.delete()
    messages.success(request, 'Check-out deleted ')
    return redirect('list_checkOut')


# -------------------------------------- TimeCard


# === API ===
class LoginApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(serializer.data)

class RegisterApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------- Company

class CompanyList(APIView):
    """List all Companies"""

    # authentication_classes = (TokenAuthentication,)
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.hashers import make_password
class CompanyDetail(APIView):
    """Lists a company"""

    def get(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        if company:
            company.delete()
        return Response({})


# --------------------------------------- Users
class UserList(APIView):
    """List all users."""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """ Users Details."""
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, pk):
        user = get_object_or_404(Employee, pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(Employee, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user:
            user.delete()
        return Response({})


# -------------------------------------- Employee

class EmployeeList(APIView):
    """List all employee."""

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """Lists a employee."""

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        if employee:
            employee.delete()
        return Response({})


# -------------------------------------- Workplace

class WorkplaceList(APIView):
    """List all workplace."""

    def get(self, request):
        workplaces = Workplace.objects.all()
        serializer = WorkplaceSerializer(workplaces, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkplaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkplaceDetail(APIView):
    """Lists a Workplace."""

    def get(self, request, pk):
        workplace = get_object_or_404(Workplace, pk=pk)
        serializer = WorkplaceSerializer(workplace)
        return Response(serializer.data)

    def put(self, request, pk):
        workplace = get_object_or_404(Workplace, pk=pk)
        serializer = WorkplaceSerializer(workplace, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workplace = get_object_or_404(Workplace, pk=pk)
        if workplace:
            workplace.delete()
        return Response({})


# -------------------------------------- Checkin

class CheckInList(APIView):
    """List all checkin."""

    def get(self, request):
        checkinList = CheckIn.objects.all()
        serializer = CheckInSerializer(checkinList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckInSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckInDetail(APIView):
    """Lists a CheckIn."""

    def get(self, request, pk):
        checkin = get_object_or_404(CheckIn, pk=pk)
        serializer = CheckInSerializer(checkin)
        return Response(serializer.data)

    def put(self, request, pk):
        checkin = get_object_or_404(CheckIn, pk=pk)
        serializer = CheckInSerializer(checkin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checkin = get_object_or_404(CheckIn, pk=pk)
        if checkin:
            checkin.delete()
        return Response({})


# -------------------------------------- Checkin

class CheckOutList(APIView):
    """List all checkin."""

    def get(self, request):
        checkoutList = CheckOut.objects.all()
        serializer = CheckOutSerializer(checkoutList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckOutDetail(APIView):
    """Lists a CheckOut."""

    def get(self, request, pk):
        checkout = get_object_or_404(CheckOut, pk=pk)
        serializer = CheckOutSerializer(checkout)
        return Response(serializer.data)

    def put(self, request, pk):
        checkout = get_object_or_404(CheckOut, pk=pk)
        serializer = CheckOutSerializer(checkout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checkout = get_object_or_404(CheckOut, pk=pk)
        if checkout:
            checkout.delete()
        return Response({})


# -------------------------------------- TimeCard

class TimeCardList(APIView):
    """List all timeCard."""

    def get(self, request):
        timeCards = TimeCard.objects.all()
        serializer = TimeCardSerializer(timeCards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimeCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimeCardDetail(APIView):
    """Lists a timeCard."""

    def get(self, request, pk):
        timeCard = get_object_or_404(TimeCard, pk=pk)
        serializer = TimeCardSerializer(timeCard, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        timeCard = get_object_or_404(TimeCard, pk=pk)
        serializer = TimeCardSerializer(timeCard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = get_object_or_404(TimeCard, pk=pk)
        if author:
            author.delete()
        return Response({})
