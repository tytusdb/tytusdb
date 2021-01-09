import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';

import { MDBBootstrapModule } from 'angular-bootstrap-md'
import { AngularFontAwesomeModule } from 'angular-font-awesome';

import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { TooltipModule } from 'ngx-bootstrap/tooltip';
import { ModalModule } from 'ngx-bootstrap/modal';
import { DashboardComponent } from './dashboard/dashboard.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


import { BsDatepickerModule } from 'ngx-bootstrap/datepicker';
import { AccordionModule } from 'ngx-bootstrap/accordion';

import {HttpClientModule} from '@angular/common/http';
import { FormsModule,  FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

//servicios
import {UsersService} from './services/users.service';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component'
import { StorageService } from './services/storage.service';
import { AuhorizatedGuardGuard } from './auhorizated-guard.guard';
import {  FileSelectDirective,FileUploader } from 'ng2-file-upload';
import { ProductosService } from './services/productos.service';
import { ApiService } from './services/api.service';
//dropdown
import { NgMultiSelectDropDownModule } from 'ng-multiselect-dropdown';

import { CommonModule } from '@angular/common';
import { NewdatabaseComponent } from './newdatabase/newdatabase.component';
import { DeletedatabaseComponent } from './deletedatabase/deletedatabase.component';
import { RenamedatabaseComponent } from './renamedatabase/renamedatabase.component';
import { RenametableComponent } from './renametable/renametable.component';
import { DeletetableComponent } from './deletetable/deletetable.component';
import { BotongetComponent } from './boton/botonget/botonget.component';

import {MatTreeModule,MatIconModule,MatButtonModule} from '@angular/material';
 

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    DashboardComponent,
    PageNotFoundComponent,

    //FileUploader,
    NewdatabaseComponent,
    DeletedatabaseComponent,
    RenamedatabaseComponent,
    RenametableComponent,
    DeletetableComponent,
    BotongetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MDBBootstrapModule.forRoot(),
    AngularFontAwesomeModule,
    BsDropdownModule.forRoot(),
    TooltipModule.forRoot(),
    ModalModule.forRoot(),
    BrowserAnimationsModule,
    //NgbModule,
    BsDatepickerModule.forRoot(),
    AccordionModule.forRoot(),
    HttpClientModule,
    ReactiveFormsModule,
    NgMultiSelectDropDownModule.forRoot(),
    CommonModule,
    FormsModule,
    MatTreeModule,
    MatIconModule,
    MatButtonModule,
    //NgModule,
    //FileSelectDirective,
    
  ],
  providers: [
    UsersService,
    StorageService,
    AuhorizatedGuardGuard,
    ProductosService,
    ApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
