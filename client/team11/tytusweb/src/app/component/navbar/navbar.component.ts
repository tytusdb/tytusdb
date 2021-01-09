import { Component, OnInit } from '@angular/core';
import { PruebaService } from 'src/app/service/prueba.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(
    private pruebaService: PruebaService
  ) { }

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

  public aboutUs(){

    this.pruebaService.aboutUs().subscribe(
      res=>{
        console.log();
        Swal.fire(
          'GRUPO 5',
          //@ts-ignore
          `${res.COORDINADOR} // ${res.INTEGRANTES[0]} // ${res.INTEGRANTES[1]}`        
        )
      },
      err => console.error(err)
    );
  }

  


 
}
