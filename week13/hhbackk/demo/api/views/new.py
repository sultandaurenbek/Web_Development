from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import CompanySerializer2
from api.serializers import VacancySerializer2
from api.serializers import CompanyWithVacancies

@api_view(['GET', 'POST'])
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def vacancy_by_company(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False)

        vacancies = company.vacancy_set.all()
        serializer = CompanyWithVacancies(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        pass

@api_view(['GET', 'POST'])
def vacancies_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacancySerializer2(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer2(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
