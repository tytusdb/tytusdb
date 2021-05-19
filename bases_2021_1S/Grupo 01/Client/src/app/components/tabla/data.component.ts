import {Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import { TableDataService } from 'src/app/service/tableData/table-data.service';
import { ShareService } from 'src/app/service/share/share.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})

export class DataComponent implements OnInit, OnDestroy {

  message: any;
  subscription: Subscription;


  constructor(private servicio: TableDataService, private data: ShareService) {
    this.subscription =    this.data.getClickEvent().subscribe(() => {
      this.refresh();
    });

  }

  @ViewChild(MatPaginator) paginator: MatPaginator;


  headers: string[]; // = ['ID', 'Name', 'Age', 'Gender', 'Country']
  rows: string[]; // = [[**,**],[**,**]]
  anuncio: any;

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
  refresh(){
    console.log(this.message.result);
    this.anuncio = '';/*
    // tslint:disable-next-line:triple-equals
    if (this.message.result.messages.length > 0){
      let comodin = '';
      // tslint:disable-next-line:only-arrow-functions typedef
      this.message.result.messages.forEach(function(elemento, indice, array) {
        comodin += elemento + '\n';
      });
      this.anuncio = comodin;
      // tslint:disable-next-line:triple-equals
    }else if (this.message.result.lexical.length > 0){
      let comodin = '';
      // tslint:disable-next-line:only-arrow-functions typedef
      this.message.result.lexical.forEach(function(elemento, indice, array) {
        comodin += elemento + '\n';
      });
      this.anuncio = comodin;
      // tslint:disable-next-line:triple-equals
    }else if (this.message.result.postgres.length > 0){
      let comodin = '';
      // tslint:disable-next-line:only-arrow-functions typedef
      this.message.result.postgres.forEach(function(elemento, indice, array) {
        comodin += elemento + '\n';
      });
      this.anuncio = comodin;
      // tslint:disable-next-line:triple-equals
    }else if (this.message.result.semantic.length > 0){
      let comodin = '';
      // tslint:disable-next-line:only-arrow-functions typedef
      this.message.result.semantic.forEach(function(elemento, indice, array) {
        comodin += elemento + '\n';
      });
      this.anuncio = comodin;
      // tslint:disable-next-line:triple-equals
    }*/

    this.anuncio = this.message.result.salida;
    const arreglo = this.message.result.querys;
    const consulta = this.message.result.query;
    
    if (consulta[0] != null){
      this.headers = consulta[0][0];
      this.rows = consulta[0][1];
    }
    
  }

}
