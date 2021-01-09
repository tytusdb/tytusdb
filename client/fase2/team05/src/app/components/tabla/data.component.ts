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


  constructor(private servicio: TableDataService, private data: ShareService) { }

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

    this.anuncio = this.message.result.messages[0];

    const arreglo = this.message.result.querys;
    this.headers = arreglo[0][0];
    this.rows = arreglo[0][1];


  }

}
