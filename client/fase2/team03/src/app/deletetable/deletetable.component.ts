import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'
import { Mandar } from 'src/app/model/mandar';

@Component({
  selector: 'app-deletetable',
  templateUrl: './deletetable.component.html',
  styleUrls: ['./deletetable.component.scss']
})
export class DeletetableComponent implements OnInit {

  publicar:Mandar={
    codigo: ''
  };
  constructor( private apiService: ApiService ) {
  
   }


  ngOnInit() {
  }

  deletetable(name: string, event:Event)
  {
    this.publicar.codigo="DROP TABLE "+name+";"
    this.apiService.postquery(this.publicar)
      .subscribe(
        res => {
          console.log(res)
        },
        err => console.log(err)
      )
    alert("Tabla " + name + " eliminada correctamente");
  }

}
