import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from '../model/user';
import { Categoria } from '../model/categoria';
import { Product, ProductCat } from '../model/Producto'

import 'rxjs/Rx';
import { map } from  'rxjs/operators';
import { FormGroup } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class ProductosService {
  

  domain: string = "http://192.168.1.4:3000";
  constructor(private http: HttpClient) { }
  
  getDomain()
  {
    return this.domain;
  }

  getCategorias()
  {
    return this.http.get<Categoria[]>(`${this.domain}/categoria/allCategorias`,{});
  }

  insertarCategoria(categoria: any)
  {
    console.log('servicio');
    console.log(categoria);
    return this.http.post<any>(`${this.domain}/categoria/insert`,{
      CATEGORIA: categoria.categoria,
      CATEGORIA_ID_CATEGORIA_PADRE: categoria.categoria_id_categoria_padre,
    });
  }

  createPhoto(title: string, photo: File) {
    const fd = new FormData();
    fd.append('photo', photo);
    return this.http.post(`${this.domain}/categoria/uploadUser`, fd);
  }

  uploadUserWithPhoto(form: FormGroup, photo: File)
  {
    console.log(form);
    const fd = new FormData();
    fd.append('credito',form.get('credito').value);
    fd.append('ganancia',form.get('ganancia').value);

    fd.append('nombre',form.get('nombre').value);
    fd.append('email',form.get('email').value);
    fd.append('telefono',form.get('telefono').value);
    fd.append('direccion',form.get('direccion').value);
    fd.append('fecha_born',form.get('fecha_born').value);
    fd.append('apellido',form.get('lastName').value);
    fd.append('idgenero',form.get('idgenero').value);
    fd.append('idrol',form.get('idrol').value);
    fd.append('idestado',form.get('idestado').value);
    
    fd.append('photo',photo);
    

    console.log('hola usuario con photo');
    console.log(fd.getAll);
    return this.http.post(`${this.domain}/user/uploadUser2`, fd);
    
  }

  crearProducto(form: FormGroup, photo: File, categoria: [])
  {
    
    console.log(form);
    const fd = new FormData();
    fd.append('producto',form.get('producto').value);
    fd.append('imagen',form.get('imagen').value);
    fd.append('descripcion',form.get('descripcion').value);
    fd.append('precio',form.get('precio').value);
    fd.append('cantidad',form.get('cantidad').value);
    fd.append('usuario_id_usuario',form.get('usuario_id_usuario').value);

    fd.append('categoria',JSON.stringify(categoria));
    
    fd.append('photo',photo);

    console.log('hola usuario con photo');
    console.log(fd);
    return this.http.post(`${this.domain}/categoria/insertProduct`, fd);
    
  }


  getProductos()
  {
    return this.http.get(`${this.domain}/categoria/allProductos`);
  }

  getProducto(id: any)
  {
    return this.http.post(`${this.domain}/categoria/getProducto`,id);
  }

  //REPORTES
  getRepGeneroYear(id: any)
  {
    return this.http.post(`${this.domain}/categoria/repGeneroYear`,id);
  }

  getRep2masGanancias()
  {
    return this.http.get(`${this.domain}/categoria/rep2masGanacias`);
  }

  getRep6ClientesMasP()
  {
    return this.http.get(`${this.domain}/categoria/rep6ClientesMasP`);
  }
  getRep7Productos()
  {
    return this.http.get(`${this.domain}/categoria/rep7_1Productos`);
  }

  getRep7_2Categorias(id: any)
  {
    return this.http.post(`${this.domain}/categoria/rep7_2Categorias`, id);
  }

  getRep9ProductoXcantidad(id: any)
  {
    return this.http.post(`${this.domain}/categoria/rep9ProductoXcantidad`, id);
  }

  insertarCart(id: any)
  {
    return this.http.post(`${this.domain}/categoria/insertCart`, id);
  }

  getCart(id: any)
  {
    return this.http.post(`${this.domain}/categoria/getCart`, id);
  }

  deleteCart(id: any)
  {
    return this.http.post(`${this.domain}/categoria/deleteCart`, id);
  }
  getProductoPorCategora(id: any)
  {
    return this.http.post(`${this.domain}/categoria/getProductoPorCategora`, id);
  }
  getCategoriasDeProducto(id: any)
  {
    return this.http.post(`${this.domain}/categoria/getCategoriasDeProducto`, id);
  }
}
