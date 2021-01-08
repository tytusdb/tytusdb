import { Component, OnInit, ViewChild } from '@angular/core';
import {MatTableDataSource} from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator';
import {MatPaginatorModule} from '@angular/material/paginator';
import { TableDataService } from 'src/app/service/tableData/table-data.service';

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

export class DataComponent implements OnInit {

  constructor(private servicio: TableDataService) { }

  @ViewChild(MatPaginator) paginator: MatPaginator;


  headers: string[]; // = ['ID', 'Name', 'Age', 'Gender', 'Country']
  rows: string[]; // = [[**,**],[**,**]]

  ngOnInit(): void {
  }

  // tslint:disable-next-line:typedef
  fillData(){
    // this.servicio.create(this.query).subscribe((response) => {
    //   const body = response.body;
    //   const msg = body.msg;
    // });

    const obj = JSON.parse(text);
    const arreglo = obj.result.querys;
    this.headers = arreglo[0][0];
    this.rows = arreglo[0][1];

  }

}
