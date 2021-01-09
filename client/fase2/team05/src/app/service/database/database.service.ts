import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {AppSettings} from '../../app.settings';

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  private URL = AppSettings.API_ENDPOINT + 'db/';
  constructor(private http: HttpClient) { }
  // tslint:disable-next-line:typedef
  create(name: string) {
    return this.http.get<any>(this.URL + `create/${name}`, { observe: 'response' });
  }
  getData_treedatabase(){
    return  this.http.get(this.URL+`showall`)
  }
}
