from datetime import datetime

from rest_framework import serializers
from rest_framework.response import Response

from .models import Employee, Company, Workplace, TimeCard, CheckIn, CheckOut
from django.contrib.auth.models import Group


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['id', 'workplace', 'checkInType', 'timeCard', 'timestamp']


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = ['id', 'workplace', 'timeCard', 'timestamp']


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ['id', 'company_id', 'address', 'latitude', 'longitude', 'name']


class TimeCardSerializer(serializers.ModelSerializer):
    checkIn = CheckInSerializer(read_only=True)
    checkOut = CheckOutSerializer(read_only=True)
    time_work = serializers.SerializerMethodField()

    class Meta:
        model = TimeCard
        fields = ['id', 'checkIn', 'checkOut', 'employee', 'time_work']

        @staticmethod
        def update(time_card, validated_data):
            time_card.employee = validated_data.get('employee', time_card.employee)
            time_card.save()
            return time_card

    def get_time_work(self, instance):
        if hasattr(instance,'checkOut'):
            check_in_time = f'{instance.checkIn.timestamp}'
            check_out_time = f'{instance.checkOut.timestamp}'
            f = '%Y-%m-%d %H:%M:%S'
            dif = int(((datetime.strptime(check_out_time[0:19], f)-datetime.strptime(check_in_time[0:19], f)).total_seconds()*1000))
            return dif
        return 0


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['username', 'email', 'name', 'nif', 'address', 'phone', 'worksAtCompany']


class CompanySerializer(serializers.ModelSerializer):
    # employees = Employ
    # eeSerializer(many=True, read_only=True)
    # manager = ManagerSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone']


class EmployeeTimeCardSerializer(serializers.ModelSerializer):
    timeCards = TimeCardSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone', 'worksAtCompany', 'timeCards']
