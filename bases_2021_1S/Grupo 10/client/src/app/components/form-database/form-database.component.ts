import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
@Component({
  selector: 'app-form-database',
  templateUrl: './form-database.component.html',
  styles: [
    `.form-cainter{
      width: 100%;
    }
    .mat-form-field{
      display: block;
    }
    `
  ]
})
export class FormDatabaseComponent {

  constructor(
    public dialogRef: MatDialogRef<FormDatabaseComponent>,
    @Inject(MAT_DIALOG_DATA) public data: string) {}

  onNoClick(): void {
    this.dialogRef.close();
  }

}
