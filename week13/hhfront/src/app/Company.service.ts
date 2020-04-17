import { Company, Vacancy, LoginResponse } from './Company';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

 

  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]>{
    return this.http.get<Company[]>(`http://127.0.0.1:8000/api/companies/`);
  }

  getCompany(id): Observable<Company> {
    return this.http.get<Company>(`http://127.0.0.1:8000/api/companies/${id}/`);
  }

  getVacanciesOfCompany(id): Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(`http://127.0.0.1:8000/api/companies/${id}/vacancies`);
  }

  getVacancies(): Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(`http://127.0.0.1:8000/api/vacancies/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`http://127.0.0.1:8000/api/login/`, {
      username,
      password
    });
  }

}


