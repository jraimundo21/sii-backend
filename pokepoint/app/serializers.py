from rest_framework import serializers

from .models import Employee, Company, Workplace, TimeCard, Manager, CheckIn, CheckOut


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['id', 'workplace_id', 'checkInType_id', 'timeCard_id', 'timestamp']


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = ['id', 'workplace_id', 'timeCard', 'timestamp']


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ['id', 'company', 'name', 'address']


class TimeCardSerializer(serializers.ModelSerializer):
    checkIn = CheckInSerializer(many=True, read_only=True)
    checkOut = CheckOutSerializer(many=True, read_only=True)
    class Meta:
        model = TimeCard
        fields = ['id', 'checkIn', 'checkOut', 'employee']

class EmployeeSerializer(serializers.ModelSerializer):
    timeCards = TimeCardSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone', 'worksAtCompany', 'timeCards']


class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone', 'manager', 'employees']


class EmployeeTimeCardSerializer(serializers.ModelSerializer):
    timeCards = TimeCardSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone', 'worksAtCompany', 'timeCards']

