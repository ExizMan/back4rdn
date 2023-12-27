from django.urls import path
from .views import *

from django.urls import re_path as url

urlpatterns = [
    path('',TopicView.as_view(),name='index'),

    # Сотрудники
    # path('employees', employees, name='employees'),
    # path('employees/<int:emp_id>/', employee, name="employee"),
    # path('employees/<int:emp_id>/delete', del_employee, name="del_employee"),
    # path('employees/new_employee/', new_employee, name="new_employee"),
    #
    # # Должности
    # path('professions', professions, name='professions'),
    # path('professions/<int:prof_id>/', profession, name="profession"),
    # path('professions/<int:prof_id>/delete', del_profession, name="del_profession"),
    # path('professions/new_profession/', new_profession, name="new_profession"),

    path('professions/', ProfessionsView.as_view()),
    path('professions/<int:pk>', ProfessionsUpdateView.as_view()),
    path('professions/del/<int:pk>', ProfessionsDestroyView.as_view()),
    path('employees/', EmployeesView.as_view()),
    path('employees/<int:pk>', EmployeesUpdateView.as_view()),
    path('employees/del/<int:pk>', EmployeesDestroyView.as_view()),

]
