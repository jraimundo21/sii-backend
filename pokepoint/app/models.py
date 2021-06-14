from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class EmployeeManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Employee(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # employeefields
    name = models.CharField(max_length=100, blank=True, null=True)
    nif = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    worksAtCompany = models.ForeignKey('Company', on_delete=models.DO_NOTHING, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = EmployeeManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Company(models.Model):
    name = models.CharField(max_length=100)
    nif = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)


class Workplace(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)


class CheckInType(models.Model):
    name = models.CharField(max_length=100)


class TimeCard(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='timeCards')


class CheckIn(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.DO_NOTHING)
    checkInType = models.ForeignKey(CheckInType, on_delete=models.DO_NOTHING)
    timeCard = models.ForeignKey(TimeCard, on_delete=models.DO_NOTHING, related_name='checkIn')
    timestamp = models.DateTimeField("time of checkin")


class CheckOut(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.DO_NOTHING)
    timeCard = models.ForeignKey(TimeCard, on_delete=models.DO_NOTHING, related_name='checkOut')
    timestamp = models.DateTimeField("time of checkout")
