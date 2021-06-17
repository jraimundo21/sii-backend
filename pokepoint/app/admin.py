from django.contrib import admin

from .models import Employee, Company, Workplace, TimeCard, CheckIn, CheckOut, CheckInType


class EmployeeInline(admin.TabularInline):
    model = Employee


class CheckInInline(admin.TabularInline):
    model = CheckIn


class CheckOutInline(admin.TabularInline):
    model = CheckOut


class CheckInTypeAdmin(admin.ModelAdmin):
    model = [
        CheckInInline
    ]


class WorkplaceInline(admin.TabularInline):
    model = Workplace


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        EmployeeInline, WorkplaceInline
    ]


class TimeCardAdmin(admin.ModelAdmin):
    inlines = [
        CheckInInline, CheckOutInline
    ]


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(TimeCard, TimeCardAdmin)
admin.site.register(CheckInType, CheckInTypeAdmin)
admin.site.register(Employee)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Workplace)
