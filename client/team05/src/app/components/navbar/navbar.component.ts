import { Component, OnInit } from '@angular/core';
import { DatabaseService } from 'src/app/service/database/database.service';
import { TableService } from 'src/app/service/table/table.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  database = {
    name: ""
  }

  table = {
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
      ]*/
  }


  constructor(private dbServs: DatabaseService, private tbServs : TableService) { }

  ngOnInit(): void {

  }

  createBD() {
    let dbName = this.database.name.trim()
    if (dbName.length === 0) {
      alert('Especifique nombre para la base de datos');
    } else {
      this.dbServs.create(dbName).subscribe((response)=> {
        const body = response.body;
        const msg = body.msg;
        alert('El servidor dice: ' + msg);
      });
    }
  }

  createTable() {
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
  }
}
