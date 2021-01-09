import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'
import { Mandar } from 'src/app/model/mandar';

@Component({
  selector: 'app-renamedatabase',
  templateUrl: './renamedatabase.component.html',
  styleUrls: ['./renamedatabase.component.scss']
})
export class RenamedatabaseComponent implements OnInit {
  publicar:Mandar={
    codigo: ''
  };
  constructor( private apiService: ApiService ) { }

  ngOnInit() {
  }
  
  renamedatabase(actual: string, nuevo: string,event:Event)
  {
    this.publicar.codigo="ALTER DATABASE "+actual+" RENAME TO "+nuevo+";";
    this.apiService.postquery(this.publicar)
      .subscribe(
        res => {
          console.log(res)
        },
        err => console.log(err)
      )
    alert("Base de datos "+actual+" cambio a "+nuevo);
  }

}
