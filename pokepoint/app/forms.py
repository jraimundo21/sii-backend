from django import forms

from .models import Employee, CheckIn, CheckOut, Workplace, TimeCard, Manager, Company


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id','name', 'nif', 'address', 'email', 'phone', 'worksAtCompany','user']


class CheckinForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['id', 'workplace', 'checkInType', 'timeCard', 'timestamp']


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ['id', 'workplace', 'timeCard', 'timestamp']


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = ['id', 'company', 'address', 'name']


class TimeCardForm(forms.ModelForm):
  class Meta:
        model = TimeCard
        fields = ['id', 'employee']


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['employee', 'company']


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone']


