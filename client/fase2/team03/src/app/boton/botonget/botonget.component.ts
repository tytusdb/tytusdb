import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../services/api.service';

@Component({
  selector: 'app-botonget',
  templateUrl: './botonget.component.html',
  styleUrls: ['./botonget.component.scss']
})
export class BotongetComponent implements OnInit {

  bd: any=[];
  po: any;
  constructor(private TempApi : ApiService) {}

  ngOnInit() {
    this.get();
  }
  get(){
   
    this.TempApi.getdb().subscribe(
      
      res=>{
        
        this.bd = res;
      },
      
      err=>console.error(err)
    );
  }
  recibir(){
    
    alert(this.bd.hola);
  }
}



