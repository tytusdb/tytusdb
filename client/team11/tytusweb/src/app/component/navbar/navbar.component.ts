import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  public new() {
    Swal.fire({
      title: 'هل تريد الاستمرار؟',
      icon: 'question',
      iconHtml: '؟',
      confirmButtonText: 'نعم',
      cancelButtonText: 'لا',
      showCancelButton: true,
      showCloseButton: true
    })
  }

  public saveAs() {
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
        this.descargar(login)
        Swal.fire(
          'Query guardado exitosamente ' + login,
          '',
          'info'
        )
      },
    }).then((result) => {

    })
  }


  descargar(name: any) {
    var filename = name + ".sql";
    var blob = new Blob([name], { type: 'text/plain' }); // EN ESTA LINEA AGREGAS TU TEXTO 
    var link = document.createElement("a");
    link.download = filename;
    link.href = window.URL.createObjectURL(blob);
    link.click();
  }
}
