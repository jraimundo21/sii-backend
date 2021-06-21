from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import TimeCard
from ..serializers import TimeCardSerializer


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
