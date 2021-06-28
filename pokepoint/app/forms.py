from django import forms
from .models import Employee, CheckIn, CheckOut, Workplace, TimeCard, Company


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'name', 'nif', 'address', 'phone', 'worksAtCompany']


class CheckinForm(forms.ModelForm):

    class Meta:
        model = CheckIn
        employee = forms.IntegerField()
        timestamp = forms.DateTimeField()
        fields = ['id', 'workplace', 'checkInType', 'timestamp', 'timeCard']
        widgets = {'timeCard': forms.HiddenInput()}

    def set_timeCard(self, timeCard):
        data = self.data.copy()
        data['timeCard'] = timeCard
        self.data = data


class CheckOutForm(forms.ModelForm):

    class Meta:
        model = CheckOut
        timestamp = forms.DateTimeField()
        fields = ['id', 'workplace', 'timestamp', 'timeCard']
        widgets = {'timeCard': forms.HiddenInput()}

    def set_timeCard(self, timeCard):
        data = self.data.copy()
        data['timeCard'] = timeCard
        self.data = data


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = ['id', 'company', 'address', 'name']


class TimeCardForm(forms.ModelForm):
    class Meta:
        model = TimeCard
        fields = ['id', 'employee']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['id', 'name', 'nif', 'address', 'email', 'phone']
