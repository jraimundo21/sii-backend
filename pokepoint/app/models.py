from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    nif = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    worksAtCompany = models.ForeignKey('Company', on_delete=models.DO_NOTHING)


class Company(models.Model):
    name = models.CharField(max_length=100)
    nif = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)


class Manager(models.Model):
    employeeManager = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    companyManager = models.ForeignKey(Company, on_delete=models.CASCADE)


class Workplace(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class CheckInType(models.Model):
    name = models.CharField(max_length=100)


class TimeCard(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class CheckIn(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.DO_NOTHING)
    checkInType = models.ForeignKey(CheckInType, on_delete=models.DO_NOTHING)
    timeCard = models.ForeignKey(TimeCard, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField("time of checkin")


class CheckOut(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.DO_NOTHING)
    timeCard = models.ForeignKey(TimeCard, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField("time of checkout")
