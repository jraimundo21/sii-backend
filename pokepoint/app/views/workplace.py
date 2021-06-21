from django.contrib.auth import login, logout

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import Workplace
from ..serializers import WorkplaceSerializer


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
