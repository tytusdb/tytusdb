import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';//se instalo para el modal

@Component({
  selector: 'app-componente-navbar',
  templateUrl: './componente-navbar.component.html',
  styleUrls: ['./componente-navbar.component.css']
})
export class ComponenteNavbarComponent implements OnInit {

  nuevobd={
    nombrebd:""
  }


  constructor(private modalService:NgbModal) { }

  ngOnInit(): void {

  }


  ver(modal){

    this.modalService.open(modal);
  }

  crearBD(){
    
  }



}
