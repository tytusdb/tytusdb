import { Component, OnInit } from '@angular/core';
import { StorageService } from '../services/storage.service';
import { Router } from '@angular/router';
import { ProductosService } from '../services/productos.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {

  public templateLogout: string= ' ';
  modelCategoria=[];
  usuario : any

  constructor(  
    //private storageService: StorageService,
    //private productoService: ProductosService,
    private router: Router) { 
      // vverifica si existe un usuario para mostrar boton logout
      /*if (storageService.isAuthenticated()!= null)
      {
        this.templateLogout= 
        `  <li class="nav-item" >
        <a class="nav-link" >
          <i class="fas fa-fw fa-power-off" ></i>
          <span>Logout</span></a>
      </li>`;
      }else{
        this.templateLogout= ' ';
      }
      this.usuario = storageService.getCurrentEmail()*/
  }

  public class_body: string =  'navbar-nav bg-gradient-primary sidebar sidebar-dark accordion';

  ngOnInit() {
    /*this.getCategorias();
    if (this.storageService.isAuthenticated()!= null)
      {
        
        this.templateLogout= 
        ` <li class="nav-item" >
            <a class="nav-link" >
              <i class="fas fa-fw fa-power-off" ></i>
            <span>Logout</span></a>
          </li>`;
      }else{
        this.templateLogout= ' ';
      }
      console.log('esto se activa')*/
  }

  cambiarestado()
  {
    if (this.class_body ==  'navbar-nav bg-gradient-primary sidebar sidebar-dark accordion')
    {
      this.class_body =  'navbar-nav bg-gradient-warning sidebar sidebar-dark accordion toggled'
    }else{
      this.class_body =  'navbar-nav bg-gradient-primary sidebar sidebar-dark accordion';
    }
    
  }

  getCategorias()
  {

    /*this.productoService.getCategorias()
    .subscribe(data => {
        this.setValorCategoria(data);
      },
      error => {
        console.log("Error", error);
        //alert('Error ' + error);
      });*/
    
  }
  setValorCategoria(data)
  {
    this.modelCategoria =data;
  }

}
