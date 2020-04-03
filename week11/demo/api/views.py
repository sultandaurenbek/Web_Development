from django.http import JsonResponse
from django.shortcuts import render

from api.models import Company, Vacancy


# Create your views here.
def companies_list(request):
    if request.method == "GET":
        try:
            companies = Company.objects.all()
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False)
        json = [company.to_json() for company in companies]
        return JsonResponse(json, safe=False)
    elif request.method == "POST":
        pass


def company_detail(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False)
        return JsonResponse(company.to_json(), safe=False)
    elif request.method == "POST":
        pass


def vacancy_by_company(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False)

        vacancies = company.vacancy_set.all()
        json_vacancies = [v.to_json() for v in vacancies]
        return JsonResponse(json_vacancies, safe=False)
    elif request.method == "POST":
        pass


def vacancies_list(request):
    if request.method == "GET":
        try:
            vacancies = Vacancy.objects.all()
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False)
        json = [v.to_json() for v in vacancies]
        return JsonResponse(json, safe=False)
    elif request.method == "POST":
        pass

def vacancy_detail(request, vacancy_id):
    if request.method == "GET":
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False)
        return JsonResponse(vacancy.to_json(), safe=False)
    elif request.method == "POST":
        pass


def top_ten_vac(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
        json = [vacancy.to_json() for vacancy in vacancies]
        if (len(json) == 0):
            return JsonResponse({'error': 'no vacancies'})
        else:
            return JsonResponse(json, safe=False)
    elif request.method == "POST":
        pass
