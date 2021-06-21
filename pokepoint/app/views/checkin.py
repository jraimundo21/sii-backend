from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import TimeCard, CheckIn
from ..serializers import CheckInSerializer


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