from django.shortcuts import render
from .models import Topic

from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.status import *
from rest_framework.response import Response
from .serializer import TopicSerializer
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Employees, Professions
from .serializer import EmployeeSerializer, ProfessonsSerializer
from rest_framework.decorators import api_view


class TopicView(APIView):
    def get(self, request):
        output = [
            {
                "text": output.text,
            } for output in Topic.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class ProfessionsView(ListCreateAPIView):
    queryset = Professions.objects.all()
    serializer_class = ProfessonsSerializer


class ProfessionsUpdateView(RetrieveUpdateAPIView):
    queryset = Professions.objects.all()
    serializer_class = ProfessonsSerializer

class ProfessionsDestroyView(RetrieveDestroyAPIView):
    queryset = Professions.objects.all()
    serializer_class = ProfessonsSerializer


class EmployeesView(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesUpdateView(RetrieveUpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesDestroyView(RetrieveDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer



# Сотрудники
"""
@api_view(['GET', 'POST'])
def employees(request):
    employees = Employees.objects.order_by()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def employee(request, emp_id):
    sublabel = None
    employee = Employees.objects.get(id=emp_id)
    if request.method == 'GET':
        serializer = EmployeeSerializer(instance=employee)
        sublabel = 'ждем изменений'
    else:
        serializer = EmployeeSerializer(instance=employee, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            sublabel = 'изменения приняты'
    if sublabel is None:
        sublabel = "Похоже, вы неправильно изменили форму"
    return Response(serializer.data)


@api_view(['POST'])
def new_employee(request):
    sublabel = "Вы еще не добавили сотрудников"

    serializer = EmployeeSerializer(request.POST)
    if serializer.is_valid():
        serializer.save()

    if sublabel is None:
        sublabel = "Похоже, вы неправильно изменили форму"


    return Response(serializer.data)


@api_view(['POST'])
def del_employee(request, emp_id):
    employee = Employees.objects.get(id=emp_id)
    employee.delete()
    return Response({'msg' : 'deleted!'})

# Должности

@api_view(['GET'])
def professions(request):
    professions = Professions.objects.all()
    serializer = ProfessonsSerializer(professions, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def new_profession(request):
    serializer = ProfessonsSerializer(data=request.POST)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)


    return Response(serializer.data)

@api_view(['GET', 'POST'])
def profession(request, prof_id):
    sublabel = None
    profession = Professions.objects.get(id=prof_id)
    if request.method == 'GET':
        serializer = ProfessonsSerializer(instance=profession)
        sublabel = 'ждем изменений'
    else:
        serializer = ProfessonsSerializer(instance=profession, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
    if sublabel is None:
        sublabel = "Похоже, вы неправильно изменили форму"

    return Response(status=HTTP_200_OK)
@api_view(['POST'])
def del_profession(request, prof_id):
    profession = Professions.objects.get(id=prof_id)
    sublabel = ""
    if request.method == 'POST':
        try:
            profession.delete()
            return Response(status=HTTP_200_OK)
        except IntegrityError:

            profession_default = Professions.objects.create_profession('без должности')
            profession_default.save()
            profession.delete()
            return Response(status=HTTP_400_BAD_REQUEST)

    else:

        return Response(status=HTTP_200_OK)
"""

# Create your views here.
