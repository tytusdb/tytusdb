import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';//se instalo para el modal
import { DatabaseService } from 'src/app/service/database/database.service';
import { TableService } from 'src/app/service/table/table.service';

@Component({
  selector: 'app-componente-navbar',
  templateUrl: './componente-navbar.component.html',
  styleUrls: ['./componente-navbar.component.css']
})
export class ComponenteNavbarComponent implements OnInit {

  nuevobd = {
    nombrebd: ""
  }

  nuevaTabla = {
    nombre: "",
    bd: "database"
  }


  constructor(private modalService: NgbModal, private dbServs: DatabaseService, private tbServs : TableService) { }

  ngOnInit(): void {

  }


  ver(modal) {

    this.modalService.open(modal);
  }

  createBD() {
    if (this.nuevobd.nombrebd.trim().length === 0) {
      alert('Especifique nombre para la base de datos');
    } else {
      this.dbServs.create(this.nuevobd.nombrebd).subscribe((response)=> {
        const body = response.body;
        const msg = body.msg;
        alert('El servidor dice: ' + msg);
      });
    }
  }

  createTable() {
    if (this.nuevaTabla.nombre.trim().length === 0) {
      alert('Especifique nombre para la tabla');
    } else {
      this.tbServs.create(this.nuevaTabla.nombre, this.nuevaTabla.bd).subscribe((response) => {
        const body = response.body;
        const msg = body.msg;
        alert('El servidor dice: ' + msg);
      })
    }
  }
}
