import { Component, OnInit } from '@angular/core';
import { faSync } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-tree',
  templateUrl: './tree.component.html',
  styleUrls: ['./tree.component.css']
})
export class TreeComponent implements OnInit {

  json: String = "";
  faSync = faSync

  constructor() {
  }

  ngOnInit(): void {
    //this.funcion1()
  }

  funcion1() {
    let toggler = document.getElementsByClassName("caret");
    for (let i = 0; i < toggler.length; i++) {
      toggler[i].addEventListener("click", function () {
        this.parentElement.querySelector(".animacion").classList.toggle("activada");
        this.classList.toggle("caret-down");
      });
    }
  }

  refresh() {
    alert("def showDatabases()")                  //funcion a la que se invocara en siguiente fase
    let item_db = document.getElementById("db")
    item_db.innerHTML = ""                        //limpiando los datos almacenados 
    this.json = prompt("recibiendo lista de bases de datos...", "[basedatos1,basedatos2, basedatos3]");
    let array = this.parser(this.json)            //array que contiene las bases de datos
    console.log("data base : ", array)
    document.getElementById("num_db").innerText = String(array.length)  //  actualizando el numero de base de datos en el navegador
    var contenedor=""
    for (let i = 0; i < array.length; i++) {

      item_db.innerHTML += 
        '<li> <span class="caret"> <i class="fa fa-database"></i> ' + array[i] +' </span>'+
        '<ul class="animacion">'+
        '<li><span class="caret"><i class="fa fa-folder-o"></i> Tablas [<a id ="t_' +array[i] +'">0</a>]</span>'+
        '<ul class="animacion" id="'+array[i] +'"></ul>'+
        '</li></ul></li>'

      let item_tabla = document.getElementById(array[i])
      alert("def showtablees(" + array[i] + ")")        //funcion a la que se invocara en la siguiente fase
      this.json = prompt("recibiendo tablas para la base de datos '" + array[i]+"'", "[ciudad,cliente,factura,proveedor]");
      let respuesta = this.parser(this.json)                                          // array que contiene las tablas 
      document.getElementById('t_' + array[i]).innerText=  String(respuesta.length)   // actualiza el numero de tabla en cada base de datos
      
      for (let i = 0; i < respuesta.length; i++) {
        item_tabla.innerHTML += '<li><i class="fa fa-table"></i> ' + respuesta[i] + '</li>'
      }
    }
    this.funcion1()
  }

  parser(data) {
    var array = []
    data = data.replace('[', "")
    data = data.replace(']', "")
    var list_data = data.split(',')
    for (let i = 0; i < list_data.length; i++) {
      array.push(list_data[i])
    }
    return array
  }

}