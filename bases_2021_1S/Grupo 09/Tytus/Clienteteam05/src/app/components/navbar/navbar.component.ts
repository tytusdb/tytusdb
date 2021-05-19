import { Component, OnInit } from '@angular/core';
import { DatabaseService } from 'src/app/service/database/database.service';
import { TableService } from 'src/app/service/table/table.service';
import { graphviz }  from 'd3-graphviz';
import { ServerService } from 'src/app/service/Server/server.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  database = {
    name: ""
  }

  table = {
    name: "",
    bd: "database"/*,
    cols: 
      [
        {
          name: "",
          datatype: "",
          size: 0,
          precision: 0
        }
      ]*/
  }


  constructor(private dbServs: DatabaseService, private tbServs : TableService,private Server:ServerService) { }

  ngOnInit(): void {

  }

  createBD() {
    let dbName = this.database.name.trim()
    if (dbName.length === 0) {
      alert('Especifique nombre para la base de datos');
    } else {
      this.dbServs.create(dbName).subscribe((response)=> {
        const body = response.body;
        const msg = body.msg;
        alert('El servidor dice: ' + msg);
      });
    }
  }

  createTable() {
    let tableName = this.table.name.trim()
    let dbName = this.table.bd.trim()
    if (tableName.length === 0) {
      alert('Especifique nombre para la tabla');
    } else {
      this.tbServs.create(tableName, dbName).subscribe((response) => {
        const body = response.body;
        const msg = body.msg;
        alert('El servidor dice: ' + msg);
      })
    }
  }

  title = 'D3-Graph';
  graph = ""

  d3() {
    graphviz("#graph").renderDot(this.graph);
  }

  async EddDatabases(){
    this.title="DATABASES"
    this.graph=""
    await this.Server.reportDB().then(
      result=>{
        this.graph = result.GRAPH
      }
    )
    console.log(this.graph)
    this.d3()
  }

  async reportAVL(){
    this.title = "REGISTROS"
    this.graph=""
    //pd Tener cuidado con que si exista la tabla
    var database = prompt("Ingrese el nombre de la base de datos");  
    var table = prompt("Ingrese el nombre de la Tabla"); 
    
    await this.Server.reportAVL(database,table).then(
      result=>{
        this.graph = result.GRAPH
      }
    )
    console.log(this.graph)
    this.d3()
  }

  async reportTBL(){
    this.title = "TABLAS"
    this.graph=""
    //pd Tener cuidado con que si exista la tabla
    var database = prompt("Ingrese el nombre de la base de datos");
    
    await this.Server.reportTBL(database).then(
      result=>{
        this.graph = result.GRAPH
      }
    )
    console.log(this.graph)
    this.d3()
  }

  async reportTPL(){
    this.title = "TUPLA"
    this.graph=""
    //pd Tener cuidado con que si exista la tabla
    var database = prompt("Ingrese el nombre de la base de datos");  
    var table = prompt("Ingrese el nombre de la Tabla"); 
    var tupla = prompt("Ingrese el la llave de la tupla"); 
    
    await this.Server.reportTPL(database,table,tupla).then(
      result=>{
        this.graph = result.GRAPH
      }
    )
    console.log(this.graph)
    this.d3()
  }

  RepASTParser(){
    this.title = "AST PARSER"
    this.graph=""
    let parse = JSON.parse(sessionStorage.getItem("PARSER"))
    if(parse){
      this.graph= parse.AST
      console.log(this.graph)
      this.d3()
    }

  }

  repGramar(){
    this.title = "GRAMMAR"
    this.graph=""
    let parse = JSON.parse(sessionStorage.getItem("PARSER"))
    if(parse){
      this.graph=`digraph { 
        node [shape=box] 
        a [label="${parse.GrammarReport}"]
      }`
      console.log(this.graph)
      this.d3()
    }
  }

  repAstConsulta(){
    this.title = "AST CONSULTA"
    this.graph=""
    let consulta = JSON.parse(sessionStorage.getItem("CONSULTA"))
    if(consulta){
      this.graph=consulta.AST
    }
    console.log(this.graph)
    this.d3()
  }

}
