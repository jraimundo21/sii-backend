from rest_framework import serializers

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

        @staticmethod
        def create(validated_data):
            return CheckOut.objects.create(**validated_data)


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ['id', 'company_id', 'address', 'name']


class TimeCardSerializer(serializers.ModelSerializer):
    checkIn = CheckInSerializer(many=True, read_only=True)
    checkOut = CheckOutSerializer(many=True, read_only=True)

    class Meta:
        model = TimeCard
        fields = ['id', 'checkIn', 'checkOut', 'employee']

        @staticmethod
        def update(time_card, validated_data):
            time_card.employee = validated_data.get('employee', time_card.employee)
            time_card.save()
            return time_card


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):
    timeCards = TimeCardSerializer(many=True, read_only=True)

    # groups = GroupSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'name', 'nif', 'address', 'phone', 'worksAtCompany', 'timeCards']


class CompanySerializer(serializers.ModelSerializer):
    # employees = EmployeeSerializer(many=True, read_only=True)
    # manager = ManagerSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone']


class EmployeeTimeCardSerializer(serializers.ModelSerializer):
    timeCards = TimeCardSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone', 'worksAtCompany', 'timeCards']
