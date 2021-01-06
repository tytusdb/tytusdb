import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-newdatabase',
  templateUrl: './newdatabase.component.html',
  styleUrls: ['./newdatabase.component.scss']
})
export class NewdatabaseComponent implements OnInit {
  message: string;
  constructor() {
  
   }

  ngOnInit() {
  }

  createdatabase(name: string, event:Event)
  {
    console.log(`Nombre: ${name}`); 
    this.message = "Se creo la base de datos";
    alert(`Creando base de datos: ${name}`);
  }

}
