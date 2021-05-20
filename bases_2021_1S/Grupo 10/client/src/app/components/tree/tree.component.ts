import {FlatTreeControl} from '@angular/cdk/tree';
import { Component, OnInit } from '@angular/core';
import {MatTreeFlatDataSource, MatTreeFlattener} from '@angular/material/tree';
import { faSync } from '@fortawesome/free-solid-svg-icons';
import { DatabaseService } from 'src/app/service/database/database.service';

interface Node {
  name: string;
  children?: Node[];
  type: Number;
}

let treeData: Node[] = [
  // {
  //   name: 'db1',
  //   children: [
  //     {name: 'table1'},
  //     {name: 'table2'},
  //     {name: 'table3'},
  //   ]
  // }, {
  //   name: 'db2',
  //   children: [
  //     {name: 'table1'},
  //     {name: 'table2'},
  //     {name: 'table3'},
  //   ]
  // },
];

/** Flat node with expandable and level information */
interface TreeNode {
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


  private _transformer = (node: Node, level: number) => {
    return {
      expandable: !!node.children && node.children.length > 0,
      name: node.name,
      type: node.type,
      level: level,
    };
  }

  treeControl = new FlatTreeControl<TreeNode>(
      node => node.level, node => node.expandable);

  treeFlattener = new MatTreeFlattener(
      this._transformer, node => node.level, node => node.expandable, node => node.children);

  dataSource = new MatTreeFlatDataSource(this.treeControl, this.treeFlattener);

  hasChild = (_: number, node: TreeNode) => node.expandable;
  
  
  json: String = "";
  faSync = faSync
  data: any
  array_database_service: any[]
  array_tabas_service = []

  constructor(private databaseservice: DatabaseService) {
  }
  
  ngOnInit(): void {
    this.refresh();
  }

  refresh() {
    let array_result: []
    treeData = []
    this.databaseservice.getData_treedatabase().subscribe(
      res => {

        this.data = (res)
        array_result = this.data.result

        let tempArray = []
        let tempChildren = []
        
        for (const item in array_result) {
          tempArray = array_result[item]
          
          for (const item2 of tempArray )
             tempChildren.push( {name: item2, type: 1} )

          treeData.push( { name: item, children: tempChildren, type: 0} )
          tempChildren = []
        }
        this.dataSource.data = treeData;        
      });

  }

}