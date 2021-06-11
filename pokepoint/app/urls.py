from django.urls import path

from . import views
from rest_framework.authtoken import views as views_auth


urlpatterns = [
# ========= API
    # ------- Auth
    path('logout/', views.logoutUser, name='logout_user'),

    path('', views.index, name='index'),

    path('api/employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    # ----------Employee
    path('employees/', views.listEmployee, name='list_employee'),
    path('add/employee/', views.addEmployee, name='add_employee'),
    path('edit/employee/<int:pk>/', views.editEmployee, name='employee'),
    path('delete/employee/<int:pk>/', views.deleteEmployee, name='delete_employee'),
    # ------- Company
    path('companies/', views.listCompany, name='list_company'),
    path('add/company/', views.addCompany, name='add_company'),
    path('edit/company/<int:pk>/', views.editCompany, name='company'),
    path('delete/company/<int:pk>/', views.deleteCompany, name='delete_company'),
    # ------- TimeCard
    #path('timecards/', views.listTimecard, name='list_timecard'),
    #path('add/timecard/', views.addTimecard, name='add_timecard'),
    #path('edit/timecard/<int:pk>/', views.editTimecard, name='timecard'),
    #path('delete/timecard/<int:pk>/', views.deleteTimecard, name='delete_timecard'),
    # ------- WorkPlace
    path('workplaces/', views.listWorkplace, name='list_workplace'),
    path('add/workplace/', views.addWorkplace, name='add_workplace'),
    path('edit/workplace/<int:pk>/', views.editWorkplace, name='workplace'),
    path('delete/workplace/<int:pk>/', views.deleteWorkplace, name='delete_workplace'),
    # ------- checkIn
    path('checkins/', views.listCheckin, name='list_checkin'),
    path('add/checkin/', views.addCheckin, name='add_checkin'),
    path('edit/checkin/<int:pk>/', views.editCheckin, name='checkin'),
    path('delete/checkin/<int:pk>/', views.deleteCheckin, name='delete_checkin'),
    # ------- checkOut
    path('checkouts/', views.listCheckout, name='list_checkout'),
    path('add/checkout/', views.addCheckout, name='add_checkout'),
    path('edit/checkout/<int:pk>/', views.editCheckout, name='checkout'),
    path('delete/checkout/<int:pk>/', views.deleteCheckout, name='delete_checkout'),


    # ======++++++++++++++++++++++++++++=== API

    # ----------User
    path('api/login/', views.LoginApi.as_view(), name='api_login'),
    path('api/register/', views.RegisterApi.as_view(), name='api_login'),
    path('api/users/', views.UserList.as_view(), name='api_user_list'),
    path('api/user/<int:pk>/', views.UserDetail.as_view(), name='api_user_detail'),
    # ----------Employee
    path('api/employees/', views.EmployeeList.as_view(), name='api_employee_list'),
    path('api/employee/<int:pk>/', views.EmployeeDetail.as_view(), name='api_employee_detail'),
    # ------- Company
    path('api/companies/', views.CompanyList.as_view(), name='api_company_list'),
    path('api/company/<int:pk>/', views.CompanyDetail.as_view(), name='api_company_detail'),
    # ------- TimeCard
    path('api/timecards/', views.TimeCardList.as_view(), name='api_timecard_list'),
    path('api/timecard/<int:pk>/', views.TimeCardDetail.as_view(), name='api_employee_detail'),
    # ------- WorkPlace
    path('api/workplaces/', views.WorkplaceList.as_view(), name='api_workplace_list'),
    path('api/workplace/<int:pk>/', views.CheckInDetail.as_view(), name='api_workplace_detail'),
    # ------- checkIn
    path('api/checkin/', views.CheckInList.as_view(), name='api_checkin_list'),
    path('api/checkin/<int:pk>/', views.CheckInDetail.as_view(), name='api_checkin_detail'),
    # ------- checkOut
    path('api/checkout/', views.CheckOutList.as_view(), name='api_checkout_list'),
    path('api/checkout/<int:pk>/', views.CheckOutDetail.as_view(), name='api_checkout_detail'),

]

