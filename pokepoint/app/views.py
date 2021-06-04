from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, \
    HttpResponseRedirect, reverse, redirect

from rest_framework.views import APIView, Response, status

from .models import Employee, TimeCard, CheckIn, Company, Workplace,CheckOut
from .serializers import EmployeeSerializer, TimeCardSerializer, TimeCardDetailSerializer, CheckInSerializer,CheckOutSerializer, CompanySerializer, WorkplaceSerializer


# === API ===
# -------------------------------------- Company

class CompanyList(APIView):
    """List all Companies"""

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """Lists a company"""

    def get(self, request, pk):
        company = get_object_or_404(Employee, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = get_object_or_404(Employee, pk=pk)
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
        serializer = WorkplaceSerializer(workplaces)
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
        checkin = get_object_or_404(Workplace, pk=pk)
        serializer = WorkplaceSerializer(checkin, data=request.data)
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
        serializer = TimeCardDetailSerializer(timeCard, many=False)
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
