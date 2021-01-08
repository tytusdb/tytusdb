import { Component, OnInit } from '@angular/core';
import { faSync } from '@fortawesome/free-solid-svg-icons';
import { ServiceTreeService}   from 'src/app/service/service-tree/service-tree.service'

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


  constructor(private ServiceTreeService:ServiceTreeService) {
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
    this.consumir_servicio()  
  }

  consumir_servicio(){
    var tmp: []
    this.ServiceTreeService.getData_treedatabase().subscribe(
      res=> {


       this.data=(res)
       console.log("recibiendo:")
       console.log(this.data)
       console.log("-------------------------")
      console.log("tmp:")
       tmp= this.data.result
       console.log(tmp)
       console.log("-------------------------")
        console.log("elementos:")
        
        var hola=[]

        const it = (obj, tabSize = 0) => {
          for (let k in obj) {
            const v = obj[k];
            if (Object.prototype.toString.call(v) === '[object Object]') {
              console.log(`${k}:`);
              it(v, tabSize + 1);
            } else {
              //console.log(`${'\t'.repeat(tabSize)}${k}`);
              hola.push(`${'\t'.repeat(tabSize)}${k}`)
            }
          }
          return;
        };
        

        it(tmp);
        alert(hola)


        console.log("***********************************")
        console.log(hola)
        this.array_database_service=hola
        /*
        for (const key in tmp) {
          if (Object.prototype.hasOwnProperty.call(tmp, key)) {
            const element = tmp[key];
            console.log(element)
          }
        }*/


        alert("def showDatabases()")                  //funcion a la que se invocara en siguiente fase
        let item_db = document.getElementById("db")
        item_db.innerHTML = ""                        //limpiando los datos almacenados 
        this.json = prompt("recibiendo lista de bases de datos...", "[basedatos1,basedatos2, basedatos3]");
        
        //let array = this.parser(this.json)            //array que contiene las bases de datos
        let array= this.array_database_service
    
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
    
         /* let item_tabla = document.getElementById(array[i])
          alert("def showtablees(" + array[i] + ")")        //funcion a la que se invocara en la siguiente fase
          this.json = prompt("recibiendo tablas para la base de datos '" + array[i]+"'", "[ciudad,cliente,factura,proveedor]");
          let respuesta = this.parser(this.json)                                          // array que contiene las tablas 
          document.getElementById('t_' + array[i]).innerText=  String(respuesta.length)   // actualiza el numero de tabla en cada base de datos
          /*
          for (let i = 0; i < respuesta.length; i++) {
            item_tabla.innerHTML += '<li><i class="fa fa-table"></i> ' + respuesta[i] + '</li>'
          }*/
        }
        this.funcion1()


      },err=>{
        alert("error al traer la data al arbol")
      }
    );
   
  }
 

}