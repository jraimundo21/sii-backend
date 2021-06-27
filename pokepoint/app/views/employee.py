from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import Employee, Company
from ..serializers import EmployeeSerializer, EmployeeTimeCardSerializer
from rest_framework.authtoken.models import Token


# -------------------------------------- Employee

class EmployeeList(APIView):
    """List all employee."""

    @staticmethod
    def get(request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = EmployeeSerializer(company.employees, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, pk):
        is_manager = request.user.groups.filter(name='manager').exists()
        company = get_object_or_404(Company, pk=pk)
        if is_manager:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                employee = serializer.save(worksAtCompany=company)
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
        employee = get_object_or_404(Employee, worksAtCompany=user_company, pk=pk)
        serializer = EmployeeTimeCardSerializer(employee, many=False)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        employee = get_object_or_404(Employee, worksAtCompany=user_company, pk=pk)
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
        if employee:
            employee.delete()
            return Response({})
        return Response(status.HTTP_401_UNAUTHORIZED)
