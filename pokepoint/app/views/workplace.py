from django.contrib.auth import login, logout

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import Workplace, Company
from ..serializers import WorkplaceSerializer


# -------------------------------------- Workplace

class WorkplaceList(APIView):
    """List all workplace."""

    @staticmethod
    def get(request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = WorkplaceSerializer(company.workplaces, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, pk):
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            company = get_object_or_404(Company, pk=pk)
            serializer = WorkplaceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(company=company)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class WorkplaceDetail(APIView):
    """Lists a Workplace Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        workplace = get_object_or_404(Workplace, company=user_company, pk=pk)
        serializer = WorkplaceSerializer(workplace)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
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
            workplace = get_object_or_404(Workplace, company=user_company, pk=pk)
            if workplace:
                workplace.delete()
                return Response({})
        return Response(status.HTTP_401_UNAUTHORIZED)
