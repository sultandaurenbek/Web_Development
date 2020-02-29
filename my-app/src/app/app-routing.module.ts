import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FilmsComponent } from './films/films.component';
import { FilmsdetailsComponent } from './filmsdetails/filmsdetails.component';


const routes: Routes = [

  {path: 'films', component: FilmsComponent },

  {path: 'films/:id', component: FilmsdetailsComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
