import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { PruebaService } from 'src/app/service/prueba.service'
import Swal from 'sweetalert2';
import 'brace';
import 'brace/mode/sql';
import 'brace/theme/github';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']

})
export class EditorComponent implements OnInit {
  constructor(
    private puebaService: PruebaService
  ) {
  };
  text: string = "";
  options: any = { maxLines: 20, minLines: 20, printMargin: false };
  ngOnInit(): void {
  }

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
    this.puebaService.consultaPrueba().subscribe(
      res=>{
        console.log(res);
      },
      err => console.error(err)
    );
    
    Swal.fire(
      'Ejucucion exitosa',
      'Resultados se encuentran en la consola',
      'success'
    )
  }

  public check() {
    Swal.fire(
      'Entrada sin errores',
      '',
      'info'
    )
  }
}
