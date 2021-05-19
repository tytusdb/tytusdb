import { Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
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
    this.subscription = this.data.getClickEvent().subscribe(() => {
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
    this.subscription = this.data.currentMessage.subscribe(message => {
      console.log(message);
      this.message = message
    });
  }

  // tslint:disable-next-line:typedef
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  // tslint:disable-next-line:typedef
  refresh() {
    this.anuncio = [];
    this.headers = [];
    this.rows = [];

    // tslint:disable-next-line:triple-equals
    if (this.message.result.messages.length > 0) {
      const array1 = this.anuncio;
      const array2 = this.message.result.messages;
      this.anuncio = array1.concat(array2);
      // tslint:disable-next-line:triple-equals
    }

    if (this.message.result.lexical.length > 0) {
      const array1 = this.anuncio;
      const array2 = this.message.result.lexical;
      this.anuncio = array1.concat(array2);
      // tslint:disable-next-line:triple-equals
    }

    const arreglo = this.message.result.querys;

    if (arreglo[0] != null) {
      this.headers = arreglo[0][0];
      this.rows = arreglo[0][1];
    }

  }

}
