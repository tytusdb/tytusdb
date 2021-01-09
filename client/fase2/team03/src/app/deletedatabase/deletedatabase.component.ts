import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'
import { Mandar } from 'src/app/model/mandar';

@Component({
  selector: 'app-deletedatabase',
  templateUrl: './deletedatabase.component.html',
  styleUrls: ['./deletedatabase.component.scss']
})
export class DeletedatabaseComponent implements OnInit {
  publicar:Mandar={
    codigo: ''
  };
  constructor( private apiService: ApiService ) { }

  ngOnInit() {
  }

  deletedatabase(name: string, event:Event)
  {
    this.publicar.codigo="DROP DATABASE IF EXISTS "+name+";";
    this.apiService.postquery(this.publicar)
      .subscribe(
        res => {
          console.log(res)
        },
        err => console.log(err)
      )
    alert("Base de datos "+name+" eliminada");
  }
}
