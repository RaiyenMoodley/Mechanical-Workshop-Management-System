from django.urls import path
from . import views

app_name = 'absentees'

urlpatterns = [
    path('', views.absence_calendar, name='absence_calendar'),
    path('events/', views.absence_events_api, name='absence_events_api'),
    path('create/', views.absence_create, name='absence_create'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]

