import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PruebaService {

  constructor(private http: HttpClient) { }


  ejecucion(texto:any){
    return this.http.post(`http://localhost:5000/ejecucion`,{sexo:texto});
  }

  tree_data(){
    return this.http.get(`http://localhost:5000/data`);
  }

  aboutUs(){
    return this.http.get(`http://localhost:5000/grupo5`);
  }

}
