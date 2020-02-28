import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TelephoneListComponent } from './telephone-list/telephone-list.component';
import { WatchListComponent } from './watch-list/watch-list.component';
import { TabletListComponent } from './tablet-list/tablet-list.component';
import { HeadphoneListComponent } from './headphone-list/headphone-list.component';


const routes: Routes = [
  {path:'telephone', component: TelephoneListComponent},
  {path: 'watches', component: WatchListComponent},
  {path: 'tablets', component: TabletListComponent},
  {path: 'headphone', component: HeadphoneListComponent},
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [ TelephoneListComponent,WatchListComponent,TabletListComponent,HeadphoneListComponent]
