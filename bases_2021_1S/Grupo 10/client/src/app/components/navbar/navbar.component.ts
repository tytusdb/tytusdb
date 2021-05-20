import { Component, OnInit, ViewChild } from '@angular/core';
import { DatabaseService } from 'src/app/service/database/database.service';
import { EditorComponent } from '../editor/editor.component';
import { FormDatabaseComponent } from '../form-database/form-database.component';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import {
  MatSnackBar,
  MatSnackBarHorizontalPosition,
  MatSnackBarVerticalPosition,
} from '@angular/material/snack-bar';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {


  @ViewChild(EditorComponent) editor : EditorComponent

  databaseName: string = ''

  constructor(private databaseservice: DatabaseService,
              public dialog: MatDialog,
              private snackBar: MatSnackBar) { }

  ngOnInit(): void {
  
  }

  onOpenFile( event ){
  this.editor.onOpenFile( event ); 
  }

  onSaveFile(){
    this.editor.onSaveFile();
  }

  onCreateDataBase(){
    
    const dialogRef = this.dialog.open(FormDatabaseComponent, {
      width: '400px',
      height: '300px', 
      data: this.databaseName
    } );

    dialogRef.afterClosed().subscribe( result => {
      this.databaseName = result;
      console.log('DB name', this.databaseName);
      this.createBD()
      
    })
  }

  onCreateTable(){
    alert('Create Table, missing..')
  }
  
  onAddTab(){
    this.editor.onAddTab()
  }

  onRunScript(){
    this.editor.onRunScript();
  }

  private createBD() {

    if (this.databaseName.trim().length === 0) {
      alert('Especifique nombre para la base de datos');
    } else {
      this.databaseservice.create(this.databaseName).subscribe((response) => {
        const body = response.body;
        this.showSnackBar(body.result.messages[0]);
        this.databaseName = "";
      }, (err) => {
        this.showSnackBar( 'Error del servidor al intentar crear la base de datos ' + this.databaseName )
        console.log(err);
        this.databaseName = "";
      });
    }
  }

  private showSnackBar( message: string) {
    this.snackBar.open( message, '', {
      duration: 3000,
      horizontalPosition: 'end',
      verticalPosition: 'top',
    });
  }
}