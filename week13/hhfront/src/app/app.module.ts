import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompaniesComponent } from './companies/companies.component';
import { Company_detailsComponent } from './company_details/company_details.component';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { FormsModule } from '@angular/forms';
import {AuthInterceptor} from "./AuthInterceptor";

@NgModule({
   declarations: [
      AppComponent,
      CompaniesComponent,
      Company_detailsComponent,
      VacanciesComponent,
   ],
   imports: [
      BrowserModule,
      AppRoutingModule,
      HttpClientModule,
      FormsModule,
   ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
