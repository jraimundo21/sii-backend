from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import TimeCard, Employee
from ..serializers import TimeCardSerializer


# -------------------------------------- TimeCard

class TimeCardList(APIView):
    """List all timeCard."""

    @staticmethod
    def get(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        if request.user.id != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = TimeCardSerializer(employee.timeCards, many=True)
        return Response(serializer.data)


class TimeCardDetail(APIView):
    """Lists a timeCard Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, employee=request.user,
                                     pk=pk)
        if is_manager:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, pk=pk)
        serializer = TimeCardSerializer(timecard, many=False)
        return Response(serializer.data)

    @staticmethod
    def delete(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, employee=request.user,
                                     pk=pk)
        if is_manager:
            timecard = get_object_or_404(TimeCard, checkIn__workplace__company=user_company, pk=pk)
        if timecard:
            timecard.delete()
            return Response({})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
