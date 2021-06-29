from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from ..models import TimeCard, CheckOut
from ..serializers import TimeCardSerializer, CheckOutSerializer


# -------------------------------------- Checkout

class CheckoutList(APIView):
    """List all checkout."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkout_list = CheckOut.objects.filter(workplace__company=user_company)
        elif request.user.is_superuser:
            checkout_list = CheckOut.objects.all()
        else:
            checkout_list = CheckOut.objects.filter(workplace__company=user_company, timeCard__employee=request.user)
        serializer = CheckOutSerializer(checkout_list, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, pk):
        # get checkin timecard
        timecard = TimeCard.objects.filter(employee=pk).last()
        if not timecard:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        tc_serialize = TimeCardSerializer(timecard)
        checkout = tc_serialize.data['checkOut']
        if not checkout:
            request.data["timeCard"] = tc_serialize.data['id']
            serializer = CheckOutSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class CheckOutDetail(APIView):
    """Lists a CheckOut Detail."""

    @staticmethod
    def get(request, pk):
        user_company = request.user.worksAtCompany_id
        is_manager = request.user.groups.filter(name='manager').exists()
        if is_manager:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, pk=pk)
        else:
            checkout = get_object_or_404(CheckOut, workplace__company=user_company, timeCard__employee=request.user,
                                         pk=pk)
        if request.user.is_superuser:
            checkout = get_object_or_404(CheckOut, pk=pk)
        serializer = CheckOutSerializer(checkout)
        return Response(serializer.data)
