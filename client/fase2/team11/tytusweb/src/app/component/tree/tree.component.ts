import { Component, OnInit } from '@angular/core';
import {FlatTreeControl} from '@angular/cdk/tree';
import {MatTreeFlatDataSource, MatTreeFlattener} from '@angular/material/tree';
import { PruebaService } from 'src/app/service/prueba.service';

interface DBNode {
  name: string;
  children?: DBNode[];
}

interface FlatNode {
  expandable: boolean;
  name: string;
  level: number;
}


@Component({
  selector: 'app-tree',
  templateUrl: './tree.component.html',
  styleUrls: ['./tree.component.css']
})

export class TreeComponent implements OnInit {

  datos: DBNode[] = [
    {
      name: 'Server',
      children: [
        {name: 'Tytus',
        children: [
          {name: 'Databases',
          children: []
          },
        ]}
      ]
    }
  ];
  resp: any;

  public update(){
    this.pruebaService.tree_data().subscribe(
      res=>{
        //@ts-ignore
        this.datos[0].children[0].children[0].children = [];
        for (let i in res){
          //@ts-ignore
          this.datos[0].children[0].children[0].children[i] = {name: res[i].name, children:[]}
          //@ts-ignore
          for(let j in res[i].tables){
            //@ts-ignore
            this.datos[0].children[0].children[0].children[i].children[j] = {name: res[i].tables[j].name}
          }
        }
        this.dataSource.data = this.datos;
      },
      err => console.error(err)
    );
  }

  private _transformer = (node: DBNode, level: number) => {
    return {
      expandable: !!node.children && node.children.length > 0,
      name: node.name,
      level: level,
    };
  }

  treeControl = new FlatTreeControl<FlatNode>(
    node => node.level, node => node.expandable
  );

  treeFlattener = new MatTreeFlattener(
    this._transformer, node => node.level, node => node.expandable, node => node.children
  );

  dataSource = new MatTreeFlatDataSource(this.treeControl, this.treeFlattener);

  constructor(
    private pruebaService: PruebaService
  ) {
    this.pruebaService.tree_data().subscribe(
      res=>{
        for (let i in res){
          //@ts-ignore
          this.datos[0].children[0].children[0].children[i] = {name: res[i].name, children:[]}
          //@ts-ignore
          for(let j in res[i].tables){
            //@ts-ignore
            this.datos[0].children[0].children[0].children[i].children[j] = {name: res[i].tables[j].name}
          }
        }
        this.dataSource.data = this.datos;
      },
      err => console.error(err)
    );
  }

  hasChild = (_: number, node: FlatNode) => node.expandable;
  ngOnInit(): void {
  }

  

}
