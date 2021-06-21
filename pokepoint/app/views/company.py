from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import Company
from ..serializers import CompanySerializer


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