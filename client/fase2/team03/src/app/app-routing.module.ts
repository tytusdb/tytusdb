import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {DashboardComponent} from './dashboard/dashboard.component';
import {PageNotFoundComponent} from './page-not-found/page-not-found.component';
import { NewdatabaseComponent } from './newdatabase/newdatabase.component';
import { DeletedatabaseComponent } from './deletedatabase/deletedatabase.component';
import { RenamedatabaseComponent } from './renamedatabase/renamedatabase.component';
import { RenametableComponent } from './renametable/renametable.component';
import { DeletetableComponent } from './deletetable/deletetable.component';
import { BotongetComponent } from './boton/botonget/botonget.component';



const routes: Routes = [
  {
    path : 'newdatabase', component : NewdatabaseComponent
  },
  {
    path : 'deletedatabase', component : DeletedatabaseComponent
  },

  {
    path : 'renamedatabase', component : RenamedatabaseComponent
  },
  {
    path : 'renametable', component : RenametableComponent
  },

  {
    path : 'deletetable', component : DeletetableComponent
  },
  {
    path : 'dashboard', component : DashboardComponent
  },
  { 
    path: '', redirectTo: '/dashboard', pathMatch: 'full' 
  },
  {
    path : 'pageNotFound', component : PageNotFoundComponent
  },
  {
    path : 'boton', component : BotongetComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
