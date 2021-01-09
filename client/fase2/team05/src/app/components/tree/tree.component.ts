import { Component, OnInit } from '@angular/core';
import { faSync } from '@fortawesome/free-solid-svg-icons';
import { DatabaseService } from 'src/app/service/database/database.service';

@Component({
  selector: 'app-tree',
  templateUrl: './tree.component.html',
  styleUrls: ['./tree.component.css']
})
export class TreeComponent implements OnInit {

  json: String = "";
  faSync = faSync
  data: any
  array_database_service: any[]
  array_tabas_service = []

  constructor(private databaseservice: DatabaseService) {
  }

  ngOnInit(): void {
    //this.funcion1()
  }

  funcion1() {/*
    let toggler = document.getElementsByClassName("caret");
    for (let i = 0; i < toggler.length; i++) {
      toggler[i].addEventListener("click", function () {
        this.parentElement.querySelector(".animacion").classList.toggle("activada");
        this.classList.toggle("caret-down");
      });
    }*/
  }

  refresh() {
    this.consumir_servicio()
  }

  consumir_servicio() {
    var array_result: []
    this.databaseservice.getData_treedatabase().subscribe(
      res => {

        this.data = (res)
        //console.log("recibiendo:")
        //console.log(this.data)
        //console.log("-------------------------")
        //console.log("array_result:")
        array_result = this.data.result
        //console.log(array_result)
        //console.log("-------------------------")
        //console.log("elementos:")

        var array_tmp = []

        const it = (obj, tabSize = 0) => {
          for (let k in obj) {
            const v = obj[k];
            if (Object.prototype.toString.call(v) === '[object Object]') {
              console.log(`${k}:`);
              it(v, tabSize + 1);
            } else {
              //console.log(`${'\t'.repeat(tabSize)}${k}`);
              array_tmp.push(`${'\t'.repeat(tabSize)}${k}`)
            }
          }
          return;
        };


        it(array_result);
        //alert(array_tmp)

        console.log("respuesta del servidor: (basedatos)", array_tmp)
        this.array_database_service = array_tmp

        var a = []
        for (const key in array_result) {
          if (Object.prototype.hasOwnProperty.call(array_result, key)) {
            const element = array_result[key];
            //console.log(element)
            a.push(element)
          }
        }
        //alert("mira la consola")
        //console.log(a)


        let item_db = document.getElementById("db")
        item_db.innerHTML = ""                        //limpiando los datos almacenados 

        let array = this.array_database_service

        document.getElementById("num_db").innerText = String(array.length)  //  actualizando el numero de base de datos en el navegador

        for (let i = 0; i < array.length; i++) {

          item_db.innerHTML +=
            '<li> <span class="caret caret-down"> <i class="fa fa-database"></i> ' + array[i] + ' </span>' +
              '<ul class="animacion activada">' +
                '<li><span class="caret caret-down"><i class="fa fa-folder-o"></i> Tablas [<a id ="t_' + array[i] + '">0</a>]</span>' +
                  '<ul class="animacion activada" id="' + array[i] + '"></ul>' +
                '</li>'+
              '</ul>'+
            '</li>'

          /*----------------------------- INGRESANDO TABLAS----------------------------------------*/

          let item_tabla = document.getElementById(array[i])
          let respuesta = a[i]                                         // array que contiene las tablas 

          document.getElementById('t_' + array[i]).innerText = String(respuesta.length)   // actualiza el numero de tabla en cada base de datos

          for (let i = 0; i < respuesta.length; i++) {
            item_tabla.innerHTML += '<li><i class="fa fa-table"></i> ' + respuesta[i] + '</li>'
          }
          /*----------------------------------------------------------------------------------------------------*/

        }
        this.funcion1()
        //alert("listo...")

      }, err => {
        alert("error al traer la data al arbol")
      }
    );

  }


}