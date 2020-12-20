import { Component, OnInit, ViewChild } from '@angular/core';
import {MatTableDataSource} from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator';
import {MatPaginatorModule} from '@angular/material/paginator';


export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
  {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
  {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
  {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
  {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
];

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnInit {
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  data: PeriodicElement[] = ELEMENT_DATA;
  dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);
  columnsToDisplay: string[] = this.displayedColumns.slice();

  @ViewChild(MatPaginator) paginator: MatPaginator;


  // tslint:disable-next-line:typedef
  addColumn() {
    const randomColumn = Math.floor(Math.random() * this.displayedColumns.length);
    this.columnsToDisplay.push(this.displayedColumns[randomColumn]);
  }

  // tslint:disable-next-line:typedef
  removeColumn() {
    if (this.columnsToDisplay.length) {
      this.columnsToDisplay.pop();
    }
  }


  constructor() { }

  ngOnInit(): void {
  }

}
