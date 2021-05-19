import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StorageService {


  private URL_STORAGE = "http://localhost:7778"
  constructor(private http:HttpClient) { }

  public Tables(database:String):Promise<any>{
    return this.http.post<any>(this.URL_STORAGE+`/Tytus/SHTABLE`,{nameDB:database}).toPromise()
  }
}
