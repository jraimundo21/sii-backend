from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, \
    HttpResponseRedirect, reverse, redirect

from rest_framework.views import APIView, Response, status

from .models import Employee, TimeCard, CheckIn
from .serializers import EmployeeSerializer, EmployeeTimeCardSerializer, TimeCardSerializer, TimeCardDetailSerializer, CheckInSerializer


# === API ===

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
        author = get_object_or_404(Employee, pk=pk)
        if author:
            author.delete()
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
# -------------------------------------- Checkin

class CheckInList(APIView):
    """List all checkin."""

    def get(self, request):
        checkIn = CheckIn.objects.all()
        serializer = CheckInSerializer(checkIn, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckInSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
