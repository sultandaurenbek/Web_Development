from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.companies_list),
    path('companies/<int:company_id>/', views.company_detail),
    path('companies/<int:company_id>/vacancies/', views.vacancy_by_company),
    path('vacancies/', views.vacancies_list),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail),
    path('vacancies/top_ten/', views.top_ten_vac),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]