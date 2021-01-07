import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PruebaService {

  constructor(private http: HttpClient) { }


  consultaPrueba(){
    return this.http.get(`http://localhost:5000/prueba`);
  }

  aboutUs(){
    return this.http.get(`http://localhost:5000/grupo5`);
  }

}
