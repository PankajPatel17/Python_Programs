from django.urls import path
from . import views
from .views import DepartmentList,DepartmentDetail,EmployeeList,EmployeeDetail

urlpatterns = [
    path('department/',views.DepartmentList.as_view()),
    path('department/<int:pk>/',views.DepartmentDetail.as_view()),
    path('employee/',views.EmployeeList.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetail.as_view()),

]