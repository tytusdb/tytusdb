import { Component, OnInit } from '@angular/core';
import { DatabaseService } from 'src/app/service/database/database.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  database = {
    name: ""
  }

  constructor(private dbServs: DatabaseService) { }

  ngOnInit(): void {

  }

  createBD() {
    let dbName = this.database.name.trim()
    if (dbName.length === 0) {
      alert('Especifique nombre para la base de datos');
    } else {
      this.dbServs.create(dbName).subscribe((response) => {
        const body = response.body;
        alert(body.result.messages[0]);
        this.database.name = "";
      }, (err) => {
        alert('Error del servidor al intentar crear la base de datos ' + dbName);
        console.log(err);
      });
    }
  }
}