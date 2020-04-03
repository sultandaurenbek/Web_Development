from django.urls import path

from api.views import companies_list, company_detail, vacancy_by_company, vacancies_list, vacancy_detail, top_ten_vac

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', vacancy_by_company),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top_ten_vac),
]