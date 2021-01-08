import {Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import { TableDataService } from 'src/app/service/tableData/table-data.service';
import { ShareService } from 'src/app/service/share/share.service';
import { Subscription } from 'rxjs';

const text = '{\n' +
  '    "ok": true,\n' +
  '    "result": {\n' +
  '        "lexical": [],\n' +
  '        "messages": [\n' +
  '            "Select ejecutado con exito."\n' +
  '        ],\n' +
  '        "postgres": [],\n' +
  '        "querys": [\n' +
  '            [\n' +
  '                [\n' +
  '                    "productos.nombre",\n' +
  '                    "categoria.nombre"\n' +
  '                ],\n' +
  '                [\n' +
  '                    [\n' +
  '                        "Escoba",\n' +
  '                        "Abarrotes"\n' +
  '                    ],\n' +
  '                    [\n' +
  '                        "Set de cubiertos",\n' +
  '                        "Abarrotes"\n' +
  '                    ]\n' +
  '                ]\n' +
  '            ]\n' +
  '        ],\n' +
  '        "semantic": [],\n' +
  '        "symbols": [],\n' +
  '        "syntax": []\n' +
  '    }\n' +
  '}\n' +
  '\n' +
  '  \n';


@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})

export class DataComponent implements OnInit, OnDestroy {

  message: string;
  subscription: Subscription;

  constructor(private servicio: TableDataService, private data: ShareService) { }

  @ViewChild(MatPaginator) paginator: MatPaginator;


  headers: string[]; // = ['ID', 'Name', 'Age', 'Gender', 'Country']
  rows: string[]; // = [[**,**],[**,**]]

  //
  // const Squery = {query: 'SHOW DATABASES;'};

  ngOnInit(): void {
    this.subscription = this.data.currentMessage.subscribe(message => this.message = message);
  }

  // tslint:disable-next-line:typedef
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  // tslint:disable-next-line:typedef
  fillData(){
    this.servicio.create({query: 'SHOW DATABASES;'}).subscribe((response) => {
      const body = response.body;
      const msg = body.result.messages;
      console.log(msg);
    }, err => console.log(err));

    // const obj = JSON.parse(text);
    // const arreglo = obj.result.querys;
    // this.headers = arreglo[0][0];
    // this.rows = arreglo[0][1];

  }

}
