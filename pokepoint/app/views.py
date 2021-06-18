from django.contrib.auth import login, logout

from django.shortcuts import get_object_or_404, \
    redirect
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView, Response, status

from .models import Employee, TimeCard, CheckIn, Company, Workplace, CheckOut
from .serializers import EmployeeSerializer, TimeCardSerializer, CheckInSerializer, \
    CheckOutSerializer, CompanySerializer, WorkplaceSerializer
from rest_framework.authtoken.models import Token


# ========== api

class LoginApi(APIView):
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def post(request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(serializer.data)


class LogoutUser(APIView):

    @staticmethod
    def post(request):
        logout(request)
        return redirect('api_login')


class RegisterApi(APIView):
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def post(request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            employee.set_password(employee.password)
            employee.save()
            Token.objects.create(user=employee)
            login(request, employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------- Company

class CompanyList(APIView):
    """List all Companies"""

    @staticmethod
    def get(request):
        if request.user.is_superuser:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)
        return Response(status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request):
        if request.user.has_perm('app.add_company'):
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_401_UNAUTHORIZED)


class CompanyDetail(APIView):
    """Lists a company"""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id

        if request.user.is_superuser or user_company == pk:
            company = get_object_or_404(Company, pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        return Response(status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id

        if request.user.is_superuser or user_company == pk:
            if request.user.has_perm('app.change_company'):
                company = get_object_or_404(Company, pk=pk)
                serializer = CompanySerializer(company, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status.HTTP_401_UNAUTHORIZED)
        return Response(status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.worksAtCompany_id

        if request.user.is_superuser or user_company == pk:
            if request.user.has_perm('app.delete_company'):
                company = get_object_or_404(Company, pk=pk)
                if company:
                    company.delete()
                return Response({})
            return Response(status.HTTP_401_UNAUTHORIZED)
        return Response(status.HTTP_401_UNAUTHORIZED)


# -------------------------------------- Employee

class EmployeeList(APIView):
    """List all employee."""

    @staticmethod
    def get(request):
        user_company = request.user.worksAtCompany_id
        if request.user.is_superuser:
            employees = Employee.objects.all()
        else:
            employees = Employee.objects.filter(worksAtCompany=user_company)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager or request.user.is_superuser:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                employee = serializer.save()
                employee.set_password(employee.password)
                employee.save()
                Token.objects.create(user=employee)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_401_UNAUTHORIZED)


class EmployeeDetail(APIView):
    """Lists a employee."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        if request.user.is_superuser:
            employee = get_object_or_404(Employee, pk=pk)
        else:
            employee = get_object_or_404(Employee, worksAtCompany=user_company, pk=pk)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()

        if is_manager:
            employee = get_object_or_404(Employee, worksAtCompany=user_company, pk=pk)
        if request.user.is_superuser:
            employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            employee.set_password(employee.password)
            employee.save()
            Token.objects.create(user=employee)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            employee = get_object_or_404(Employee, worksAtCompany=user_company, pk=pk)
        if request.user.is_superuser:
            employee = get_object_or_404(Employee, pk=pk)
        if employee:
            employee.delete()
            return Response({})
        return Response(status.HTTP_401_UNAUTHORIZED)


# -------------------------------------- Workplace

class WorkplaceList(APIView):
    """List all workplace."""

    @staticmethod
    def get(request):
        if request.user.is_superuser:
            workplaces = Workplace.objects.all()
        else:
            user_company = request.user.worksAtCompany_id
            if user_company is None:
                return []
            workplaces = Workplace.objects.filter(worksAtCompany=user_company)

        serializer = WorkplaceSerializer(workplaces, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        is_manager = request.user.groups.filter(name='manager').exists()

        if request.user.is_superuser or is_manager:
            serializer = WorkplaceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_401_UNAUTHORIZED)


class WorkplaceDetail(APIView):
    """Lists a Workplace Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        if request.user.is_superuser:
            workplace = get_object_or_404(Workplace, pk=pk)
        else:
            workplace = get_object_or_404(Workplace, company=user_company, pk=pk)
        serializer = WorkplaceSerializer(workplace)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            if request.user.is_superuser:
                workplace = get_object_or_404(Workplace, pk=pk)
            else:
                workplace = get_object_or_404(Workplace, company=user_company, pk=pk)
            serializer = WorkplaceSerializer(workplace, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.employee.worksAtCompany.id
        is_manager = request.user.groups.filter(name='manager').exists()

        if is_manager:
            if request.user.is_superuser:
                workplace = get_object_or_404(Workplace, pk=pk)
            else:
                workplace = get_object_or_404(Workplace, company=user_company, pk=pk)
            if workplace:
                workplace.delete()
            return Response({})
        return Response(status.HTTP_401_UNAUTHORIZED)


# -------------------------------------- Checkin

class CheckInList(APIView):
    """List all checkin."""

    @staticmethod
    def get(request):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkin_list = CheckIn.objects.filter(workplace__company=user_company)
        elif request.user.is_superuser:
            checkin_list = CheckIn.objects.all()
        else:
            checkin_list = CheckIn.objects.filter(workplace__company=user_company, timeCard__employee=request.user)
        serializer = CheckInSerializer(checkin_list, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        # save timeCard with
        time_card = TimeCard()
        time_card.employee = request.user
        time_card.save()
        request.data["timeCard"] = time_card.id
        # add timeCard in dictionary
        serializer = CheckInSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckInDetail(APIView):
    """Lists a CheckIn Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkin = get_object_or_404(CheckIn, pk=pk, workplace__company=user_company)
        elif request.user.is_superuser:
            checkin = get_object_or_404(CheckIn, pk=pk)
        else:
            checkin = get_object_or_404(CheckIn, workplace__company=user_company, timeCard__employee=request.user,
                                        pk=pk)
        serializer = CheckInSerializer(checkin)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkin = get_object_or_404(CheckIn, pk=pk, workplace__company=user_company)
        elif request.user.is_superuser:
            checkin = get_object_or_404(CheckIn, pk=pk)
        else:
            checkin = get_object_or_404(CheckIn, workplace__company=user_company, timeCard__employee=request.user,
                                        pk=pk)
        serializer = CheckInSerializer(checkin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkin = get_object_or_404(CheckIn, pk=pk, workplace__company=user_company)
        elif request.user.is_superuser:
            checkin = get_object_or_404(CheckIn, pk=pk)
        else:
            checkin = get_object_or_404(CheckIn, workplace__company=user_company, timeCard__employee=request.user,
                                        pk=pk)
        if checkin:
            checkin.delete()
            return Response({})


# -------------------------------------- Checkin

class CheckoutList(APIView):
    """List all checkout."""

    @staticmethod
    def get(request):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkout_list = CheckOut.objects.filter(workplace__company=user_company)
        elif request.user.is_superuser:
            checkout_list = CheckOut.objects.all()
        else:
            checkout_list = CheckOut.objects.filter(workplace__company=user_company, timeCard__employee=request.user)
        serializer = CheckOutSerializer(checkout_list, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        # get checkin timecard
        timecard = TimeCard.objects.filter(employee=request.user).last()
        if not timecard:
            return Response(status.HTTP_401_UNAUTHORIZED)
        tc_serialize = TimeCardSerializer(timecard)
        checkout = tc_serialize.data['checkOut']
        if not checkout:
            request.data["timeCard"] = tc_serialize.data['id']
            serializer = CheckOutSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_401_UNAUTHORIZED)


class CheckOutDetail(APIView):
    """Lists a CheckOut Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, pk=pk)
        else:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, timeCard__employee=request.user,
                                         pk=pk)
        if request.user.is_superuser:
            checkout = get_object_or_404(CheckOut, pk=pk)
        serializer = CheckOutSerializer(checkout)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, pk=pk)
        if request.user.is_superuser:
            checkout = get_object_or_404(CheckOut, pk=pk)
        else:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, timeCard__employee=request.user,
                                         pk=pk)
        serializer = CheckOutSerializer(checkout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if request.user.is_superuser:
            checkout = get_object_or_404(CheckOut, pk=pk)
        else:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, timeCard__employee=request.user,
                                         pk=pk)
        if is_manager:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, pk=pk)
        if checkout:
            checkout.delete()
            return Response({})


# -------------------------------------- TimeCard

class TimeCardList(APIView):
    """List all timeCard."""

    @staticmethod
    def get(request):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if request.user.is_superuser:
            time_cards = TimeCard.objects.all()
        else:
            time_cards = TimeCard.objects.filter(checkIn__workplace__company=user_company, employee=request.user)
        if is_manager:
            time_cards = TimeCard.objects.filter(checkIn__workplace__company=user_company)
        serializer = TimeCardSerializer(time_cards, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = TimeCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimeCardDetail(APIView):
    """Lists a timeCard Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if request.user.is_superuser:
            timecard = get_object_or_404(TimeCard, pk=pk)
        else:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, employee=request.user,
                                         pk=pk)
        if is_manager:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, pk=pk)
        serializer = TimeCardSerializer(timecard, many=False)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if request.user.is_superuser:
            timecard = get_object_or_404(TimeCard, pk=pk)
        else:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, employee=request.user,
                                         pk=pk)
        if is_manager:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, pk=pk)
        serializer = TimeCardSerializer(timecard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if request.user.is_superuser:
            timecard = get_object_or_404(TimeCard, pk=pk)
        else:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, employee=request.user,
                                         pk=pk)
        if is_manager:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, pk=pk)
        if timecard:
            timecard.delete()
            return Response({})
        return Response(status.HTTP_401_UNAUTHORIZED)
