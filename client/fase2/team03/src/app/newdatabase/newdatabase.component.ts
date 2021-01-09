import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'
import { Mandar } from 'src/app/model/mandar';

@Component({
  selector: 'app-newdatabase',
  templateUrl: './newdatabase.component.html',
  styleUrls: ['./newdatabase.component.scss']
})
export class NewdatabaseComponent implements OnInit {
  message: string;
  publicar:Mandar={
    codigo: ''
  };
  constructor( private apiService: ApiService ) {
  
   }

  ngOnInit() {
  }

  createdatabase(name: string, event:Event)
  {
    console.log(`Nombre: ${name}`); 
    this.publicar.codigo="CREATE DATABASE IF NOT EXISTS "+name+"\
    OWNER = 'BD_Grupo3'\
    MODE = 1;";
    this.apiService.postquery(this.publicar)
      .subscribe(
        res => {
          console.log(res)
        },
        err => console.log(err)
      )
    this.message = "Se creo la base de datos";
    alert(`Se creo la base de datos: ${name}`);
  }

}
