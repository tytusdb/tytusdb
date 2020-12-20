import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DataComponent } from './components/tabla/data.component';
import { MaterialModule } from './material/material.module';
import { MatButtonModule } from '@angular/material/button'
import { EditorComponent } from './editor/editor.component';
import { FormsModule } from '@angular/forms';
import { CodemirrorModule } from '@ctrl/ngx-codemirror';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { ComponenteNavbarComponent } from './componente-navbar/componente-navbar.component';

@NgModule({
  declarations: [
    AppComponent,
    DataComponent,
    EditorComponent,
    ComponenteNavbarComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    MatButtonModule,
    FormsModule,
    CodemirrorModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
