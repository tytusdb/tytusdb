import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Mandar } from 'src/app/model/mandar';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http:HttpClient) { }
  public getdb(){
    return this.http.get("http://localhost:5000/prueba");
  }
  public postquery(Accion:Mandar){
    const ruta = "http://localhost:5000/prueba2";
    return this.http.post(ruta, Accion);
  }
}
