from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import Employee
from ..serializers import EmployeeSerializer
from rest_framework.authtoken.models import Token


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
