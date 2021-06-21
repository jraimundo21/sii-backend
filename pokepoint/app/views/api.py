from django.contrib.auth import login, logout

from django.shortcuts import \
    redirect
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView, Response, status

from rest_framework.authtoken.models import Token
from ..serializers import EmployeeSerializer


# ========== api

class LoginApi(APIView):
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def post(request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(serializer.data)


class LogoutUser(APIView):

    @staticmethod
    def post(request):
        logout(request)
        return redirect('api_login')


class RegisterApi(APIView):
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def post(request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            employee.set_password(employee.password)
            employee.save()
            Token.objects.create(user=employee)
            login(request, employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
