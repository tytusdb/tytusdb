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

  ngOnInit(): void { }

  public save() {
    Swal.fire({
      title: 'Quieres guardar los cambios?',
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: `Si`,
      denyButtonText: `No`,
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire('Guardado!', '', 'success')
      } else if (result.isDenied) {
        Swal.fire('Los cambios no fueron guardados', '', 'error')
      }
    })
  }

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
        console.log(this.errores)
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
        console.log(this.errores)
      },
      err => console.error(err)
    );
  }
}
