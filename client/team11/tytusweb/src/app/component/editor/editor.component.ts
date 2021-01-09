Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@RomaelP 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


RomaelP
/
TytusDB_team11
forked from joorgej/TytusDB_team11
0
01
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
TytusDB_team11/cliente/tytusweb/src/app/component/editor/editor.component.ts /

Jose Moran Funcionalidades
Latest commit a03421b 1 hour ago
 History
 1 contributor
161 lines (142 sloc)  4.16 KB
 
import { Component, OnInit, ElementRef, ViewChild, Output } from '@angular/core';
import { PruebaService } from 'src/app/service/prueba.service'
import Swal from 'sweetalert2';
import 'brace';
import 'brace/mode/sql';
import 'brace/theme/sqlserver';
import * as ace from 'ace-builds';
import { AceEditorModule } from 'ng2-ace-editor';
import { ConsoleComponent } from '../console/console.component';
import { EventEmitter } from 'events';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']

})
export class EditorComponent implements OnInit {
  @ViewChild('editor') editor: any;
  constructor(private puebaService: PruebaService) { };

  ngAfterViewInit() {
  }

  text: any = "";
  options: any = { maxLines: 20, minLines: 20, printMargin: false };
  public messages: string = ""
  public res: any[] = []
  public resultados: any[] = []
  public querys: any[] = []
  public errores: string = ""
  copytext:string = ""
  ngOnInit(): void { }



  public run() {
    this.puebaService.ejecucion(this.text).subscribe(
      res => {
        //@ts-ignore
        for (const iterator of res.response.messages) {
          this.messages += iterator + "\n\n"
        }
        //@ts-ignore
        console.log(res.response);
        //@ts-ignore
        this.querys = res.response.querys
        this.errores = ""
        //@ts-ignore
        for (const iterator of res.response.postgres) {
          this.errores += iterator + "\n\n"
        }

        //@ts-ignore
        for (const iterator of res.response.lexical) {
          this.errores += iterator + "\n\n"
        }

        //@ts-ignore
        for (const iterator of res.response.semantic) {
          this.errores += iterator + "\n\n"
        }

        //console.log(this.errores)
      },
      err => console.error(err)
    );

    /* Swal.fire(
       'Ejucucion exitosa',
       'Resultados se encuentran en la consola',
       'success'
     )*/
    //console.log(this.text)
  }

  public check() {
    let editor = ace.edit('editor').getSelectedText()
    this.puebaService.ejecucion(editor).subscribe(
      res => {
        //@ts-ignore
        for (const iterator of res.response.messages) {
          this.messages += iterator + "\n\n"
        }
        //@ts-ignore
        console.log(res.response);
        //@ts-ignore
        this.querys = res.response.querys
        this.errores = ""
        //@ts-ignore
        for (const iterator of res.response.postgres) {
          this.errores += iterator + "\n\n"
        }

        //@ts-ignore
        for (const iterator of res.response.lexical) {
          this.errores += iterator + "\n\n"
        }

        //@ts-ignore
        for (const iterator of res.response.semantic) {
          this.errores += iterator + "\n\n"
        }
      },
      err => console.error(err)
    );
  }

  public save() {
    Swal.fire({
      title: 'Ingrese el nombre:',
      input: 'text',
      inputAttributes: {
        autocapitalize: 'off'
      },
      showCancelButton: true,
      confirmButtonText: 'Guardar',
      showLoaderOnConfirm: true,
      cancelButtonText: 'Cancelar   ',
      preConfirm: (login) => {
        this.descargar(login, this.text)
        Swal.fire(
          'Query guardado exitosamente ' + login,
          '',
          'info'
        )
      },
    }).then((result) => {

    })
  }

  descargar(name: string, value:string) {
    var filename = name + ".sql";
    var blob = new Blob([value], { type: 'text/plain' }); // EN ESTA LINEA AGREGAS TU TEXTO 
    var link = document.createElement("a");
    link.download = filename;
    link.href = window.URL.createObjectURL(blob);
    link.click();
  }

  async  paste() {
    const text = await navigator.clipboard.readText();
    this.text += text;
  }

  public copy(){
    let editor = ace.edit('editor').getSelectedText()
    const selBox = document.createElement('textarea');
    selBox.style.position = 'fixed';
    selBox.style.left = '0';
    selBox.style.top = '0';
    selBox.style.opacity = '0';
    selBox.value = editor;
    document.body.appendChild(selBox);
    selBox.focus();
    selBox.select();
    document.execCommand('copy');
    document.body.removeChild(selBox);
  }
}
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
