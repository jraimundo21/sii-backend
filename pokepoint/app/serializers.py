from rest_framework import serializers

from .models import Employee, Company, Workplace, TimeCard, Manager, CheckIn, CheckOut


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['id', 'workplace', 'checkInType_id', 'timeCard', 'timestamp']


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = ['id', 'workplace', 'timeCard', 'timestamp']


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ['id', 'company_id','address','name'  ]


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
class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['employee', 'company']


class CompanySerializer(serializers.ModelSerializer):
    #employees = EmployeeSerializer(many=True, read_only=True)
    #manager = ManagerSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id','name', 'nif', 'address','email','phone']


class EmployeeTimeCardSerializer(serializers.ModelSerializer):
    timeCards = TimeCardSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone', 'worksAtCompany', 'timeCards']

