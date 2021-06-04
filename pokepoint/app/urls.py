from django.urls import path

from . import views

urlpatterns = [
   # ------- Employee
    path('api/employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('api/employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
   # ------- Company
    path('api/companies/', views.CompanyList.as_view(), name='company_list'),
    path('api/companies/<int:pk>/', views.CompanyDetail.as_view(), name='companies_detail'),
    # ------- TimeCard
    path('api/timecards/', views.TimeCardList.as_view(), name='timecard_list'),
    path('api/timecards/<int:pk>/', views.TimeCardDetail.as_view(), name='employee_detail'),
  # ------- WorkPlace
    path('api/workplaces/', views.WorkplaceList.as_view(), name='workplace_list'),
    path('api/workplace/<int:pk>/', views.CheckInDetail.as_view(), name='workplace_detail'),
    # ------- checkIn
    path('api/checkin/', views.CheckInList.as_view(), name='checkin_list'),
    path('api/checkin/<int:pk>/', views.CheckInDetail.as_view(), name='checkin_detail'),
    # ------- checkOut
    path('api/checkout/', views.CheckOutList.as_view(), name='checkout_list'),
    path('api/checkout/<int:pk>/', views.CheckOutDetail.as_view(), name='checkout_detail'),

]

