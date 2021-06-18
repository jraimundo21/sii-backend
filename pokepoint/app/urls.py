from django.urls import path, include

from . import views, app_views

urlpatterns = [

    # ------- Auth
    path('', include('django.contrib.auth.urls')),
    path('logout/', app_views.logoutUser, name='logout_user'),
    path('index', app_views.index, name='index'),

    # ----------Employee
    path('employees/', app_views.listEmployee, name='list_employee'),
    path('add/employee/', app_views.addEmployee, name='add_employee'),
    path('edit/employee/<int:pk>/', app_views.editEmployee, name='employee'),
    path('delete/employee/<int:pk>/', app_views.deleteEmployee, name='delete_employee'),
    # ------- Company
    path('companies/', app_views.listCompany, name='list_company'),
    path('add/company/', app_views.addCompany, name='add_company'),
    path('edit/company/<int:pk>/', app_views.editCompany, name='company'),
    path('delete/company/<int:pk>/', app_views.deleteCompany, name='delete_company'),
    # ------- TimeCard
    # path('timecards/', app_views.listTimecard, name='list_timecard'),
    # path('add/timecard/', app_views.addTimecard, name='add_timecard'),
    # path('edit/timecard/<int:pk>/', app_views.editTimecard, name='timecard'),
    # path('delete/timecard/<int:pk>/', app_views.deleteTimecard, name='delete_timecard'),
    # ------- WorkPlace
    path('workplaces/', app_views.listWorkplace, name='list_workplace'),
    path('add/workplace/', app_views.addWorkplace, name='add_workplace'),
    path('edit/workplace/<int:pk>/', app_views.editWorkplace, name='workplace'),
    path('delete/workplace/<int:pk>/', app_views.deleteWorkplace, name='delete_workplace'),
    # ------- checkIn
    path('checkins/', app_views.listCheckin, name='list_checkin'),
    path('add/checkin/', app_views.addCheckin, name='add_checkin'),
    path('edit/checkin/<int:pk>/', app_views.editCheckin, name='checkin'),
    path('delete/checkin/<int:pk>/', app_views.deleteCheckin, name='delete_checkin'),
    # ------- checkOut
    path('checkouts/', app_views.listCheckout, name='list_checkout'),
    path('add/checkout/', app_views.addCheckout, name='add_checkout'),
    path('edit/checkout/<int:pk>/', app_views.editCheckout, name='checkout'),
    path('delete/checkout/<int:pk>/', app_views.deleteCheckout, name='delete_checkout'),

    # ================Api===================
    path('api/login/', views.LoginApi.as_view(), name='api_login'),
    path('api/logout/', views.LogoutUser.as_view(), name='api_logout'),

    # path('api/register/', views.RegisterApi.as_view(), name='api_login'),
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
    path('api/workplace/<int:pk>/', views.WorkplaceDetail.as_view(), name='api_workplace_detail'),
    # ------- checkIn
    path('api/checkin/', views.CheckInList.as_view(), name='api_checkin_list'),
    path('api/checkin/<int:pk>/', views.CheckInDetail.as_view(), name='api_checkin_detail'),
    # ------- checkOut
    path('api/checkout/', views.CheckoutList.as_view(), name='api_checkout_list'),
    path('api/checkout/<int:pk>/', views.CheckOutDetail.as_view(), name='api_checkout_detail'),

]
