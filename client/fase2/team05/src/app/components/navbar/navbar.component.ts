import { Component, OnInit } from '@angular/core';
import { DatabaseService } from 'src/app/service/database/database.service';
// commit 1.3 import { TableService } from 'src/app/service/table/table.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  database = {
    name: ""
  }

  /*commit 1.3 table = {
    name: "",
    bd: "database"/*,
    cols: 
      [
        {
          name: "",
          datatype: "",
          size: 0,
          precision: 0
        }
      ]*
  }*/


  constructor(private dbServs: DatabaseService) { }

  ngOnInit(): void {

  }

  createBD() {
    let dbName = this.database.name.trim()
    if (dbName.length === 0) {
      alert('Especifique nombre para la base de datos');
    } else {
      this.dbServs.create(dbName).subscribe((response)=> {
        const body = response.body;
        // Adaptar el mensaje 'response' para mostrar result.messages

        // result.messages es una lista, pero solo se envía una instrucción
        // se debe recuperar la PRIMERA POSICIÓN de esa lista y mostrar ese mensaje
      }, (err) => {
        // Indicar al usuario que hubo un error al crear la base de datos 'dbName'
        // Por ejemplo:
        //    alert('Error del servidor al intetnar crear la base de datos ' + dbName)
        // Imprimir en consola (con console.log) el error 'err'
      });
    }
  }

 /* commit 1.3 createTable() {
    let tableName = this.table.name.trim()
    let dbName = this.table.bd.trim()
    if (tableName.length === 0) {
      alert('Especifique nombre para la tabla');
    } else {
      this.tbServs.create(tableName, dbName).subscribe((response) => {
        const body = response.body;
        const msg = body.msg;
        alert('El servidor dice: ' + msg);
      })
    }
  }*/
}
