import { Component, OnInit } from '@angular/core';
import {FlatTreeControl} from '@angular/cdk/tree';

import {NestedTreeControl} from '@angular/cdk/tree';
import {MatTreeNestedDataSource} from '@angular/material/tree';
import {BehaviorSubject, Observable, of as observableOf} from 'rxjs';
import {ApiService} from '../services/api.service';
import { Mandar } from 'src/app/model/mandar';
/**
 * Food data with nested structure.
 * Each node has a name and an optional list of children.
 */
interface FoodNode {
  name: string;
  children?: FoodNode[];
}

export class FileNode {
  children: FileNode[];
  filename: string;
}

/** Flat node with expandable and level information */
interface ExampleFlatNode {
  expandable: boolean;
  name: string;
  level: number;
}


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  nestedTreeControl: NestedTreeControl<FileNode>;
  nestedDataSource: MatTreeNestedDataSource<FileNode>;
  dataChange: BehaviorSubject<FileNode[]> = new BehaviorSubject<FileNode[]>([]);
  mensaje:string="";
  mensaje2:string="";
  listacategorias:any = [];
  publicar:Mandar={
    codigo: ''
  };

  constructor(private TempApi : ApiService) {}

  ngOnInit() {
    this.nestedTreeControl = new NestedTreeControl<FileNode>(this._getChildren);
    this.nestedDataSource = new MatTreeNestedDataSource();

    this.dataChange.subscribe(data => this.nestedDataSource.data = data);

    this.dataChange.next([
      {
        filename: "Data Bases",
        children: [
          {
            filename: "Database_1",
            children: [
              {
                filename: "Table_1",
                children: []
              }
            ],
          },
          {
            filename: "Database_2",
            children: [
              {
                filename: "Table_1",
                children: []
              },
              {
                filename: "Table_2",
                children: []
              },
            ],
          },
          {
            filename: "Database_3",
            children: [
              {
                filename: "Table_1",
                children: []
              },
              {
                filename: "Table_2",
                children: []
              },
              {
                filename: "Table_3",
                children: []
              },
            ],
          }
        ],
      }
    ]);
    
  }
  private _getChildren = (node: FileNode) => { return observableOf(node.children); };
  
  hasNestedChild = (_: number, nodeData: FileNode) => {return !(""); };

  consulta(event:Event)
  {
    this.publicar.codigo=this.mensaje;
    this.TempApi.postquery(this.publicar).subscribe(
      res=>{
        this.listacategorias = res;
        this.mensaje2=this.listacategorias.codigo
      }
    );
    //alert(this.mensaje);
  }

}
