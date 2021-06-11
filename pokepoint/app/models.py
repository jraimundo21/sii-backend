from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    nif = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    worksAtCompany = models.ForeignKey('Company', on_delete=models.DO_NOTHING)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)


class Company(models.Model):
    name = models.CharField(max_length=100)
    nif = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)


class Manager(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING,related_name='manager')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='manager')


class Workplace(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class CheckInType(models.Model):
    name = models.CharField(max_length=100)


class TimeCard(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING,related_name='timeCards')


class CheckIn(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.DO_NOTHING)
    checkInType = models.ForeignKey(CheckInType, on_delete=models.DO_NOTHING)
    timeCard = models.ForeignKey(TimeCard, on_delete=models.DO_NOTHING, related_name='checkIn')
    timestamp = models.DateTimeField("time of checkin")


class CheckOut(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.DO_NOTHING)
    timeCard = models.ForeignKey(TimeCard, on_delete=models.DO_NOTHING, related_name='checkOut')
    timestamp = models.DateTimeField("time of checkout")
