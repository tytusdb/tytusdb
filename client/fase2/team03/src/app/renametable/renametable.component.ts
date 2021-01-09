import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'
import { Mandar } from 'src/app/model/mandar';

@Component({
  selector: 'app-renametable',
  templateUrl: './renametable.component.html',
  styleUrls: ['./renametable.component.scss']
})
export class RenametableComponent implements OnInit {

  publicar:Mandar={
    codigo: ''
  };
  constructor( private apiService: ApiService ) {
  
   }

  ngOnInit() {
  }
  renametable(name: string, name2: string, event:Event)
  {
    alert("Cambio de nombre tabla "+name+" por "+ name2);
  }

}
