from django.urls import path, include

from .app_views import *
from .views import *

urlpatterns = [

    # ------- Auth
    #path('', include('django.contrib.auth.urls')),
    path('logouts/', logoutUser, name='logout_user'),
    path('index', index, name='index'),

    # ----------Employee
    path('employees/', listEmployee, name='list_employee'),
    path('add/employees/', addEmployee, name='add_employee'),
    path('edit/employees/<int:pk>/', editEmployee, name='employee'),
    path('delete/employees/<int:pk>/', deleteEmployee, name='delete_employee'),
    # ------- Company
    path('companies/', listCompany, name='list_company'),
    path('add/company/', addCompany, name='add_company'),
    path('edit/company/<int:pk>/', editCompany, name='edit_company'),
    path('delete/company/<int:pk>/', deleteCompany, name='delete_company'),
    # ------- WorkPlace
    path('workplaces/', listWorkplace, name='list_workplace'),
    path('add/workplace/', addWorkplace, name='add_workplace'),
    path('edit/workplace/<int:pk>/', editWorkplace, name='workplace'),
    path('delete/workplace/<int:pk>/', deleteWorkplace, name='delete_workplace'),
    # ------- checkIn
    path('checkins/', listCheckin, name='list_checkin'),
    path('add/checkin/', addCheckin, name='add_checkin'),
    path('delete/checkin/<int:pk>/', deleteCheckin, name='delete_checkin'),
    path('add/checkin/<int:pk>/', addCheckinByManager, name='add_checkin_by_manager'),

    # ------- checkOut
    path('checkouts/', listCheckout, name='list_checkout'),
    path('add/checkout/', addCheckout, name='add_checkout'),
    path('delete/checkout/<int:pk>/', deleteCheckout, name='delete_checkout'),
    path('add/checkout/<int:pk>/', addCheckOutByManager, name='add_checkout_by_manager'),

    # ================Api===================
    path('api/login/', LoginApi.as_view(), name='api_login'),
    path('api/logout/', LogoutUser.as_view(), name='api_logout'),

    # path('api/register/', views.RegisterApi.as_view(), name='api_login'),
    # ----------Employee
    path('api/employees/<int:pk>/', EmployeeDetail.as_view(), name='api_employee_detail'),
    path('api/companies/<int:pk>/employees', EmployeeList.as_view(), name='api_employee_detail'),

    # ------- Company
    path('api/companies/', CompanyList.as_view(), name='api_company_list'),
    path('api/companies/<int:pk>/', CompanyDetail.as_view(), name='api_company_detail'),
    # ------- TimeCard
    path('api/timecards/<int:pk>/', TimeCardDetail.as_view(), name='api_employee_detail'),
    path('api/employees/<int:pk>/timecards/', TimeCardList.as_view(), name='api_timecard_list'),

    # ------- WorkPlace
    path('api/workplaces/<int:pk>/', WorkplaceDetail.as_view(), name='api_workplace_detail'),
    path('api/companies/<int:pk>/workplaces/', WorkplaceList.as_view(), name='api_workplace_list'),
    # ------- checkIn
    path('api/checkins/<int:pk>/', CheckInDetail.as_view(), name='api_checkin_detail'),
    path('api/employees/<int:pk>/checkins/', CheckInList.as_view(), name='api_checkin_list'),

    # ------- checkOut
    path('api/checkouts/<int:pk>/', CheckOutDetail.as_view(), name='api_checkout_detail'),
    path('api/employees/<int:pk>/checkouts/', CheckoutList.as_view(), name='api_checkin_list'),

]
