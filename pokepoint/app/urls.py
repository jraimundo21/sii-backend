from django.urls import path

from . import views

urlpatterns = [
    path('api/employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('api/employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
   # path('api/companies/', views.CompanyList.as_view(), name='company_list'),
    path('api/timecards/', views.TimeCardList.as_view(), name='timecard_list'),
    path('api/timecards/<int:pk>/', views.TimeCardDetail.as_view(), name='employee_detail'),
   # path('api/workplaces/', views.WorkplaceList.as_view(), name='workplace_list'),
]

