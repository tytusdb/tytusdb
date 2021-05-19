import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import {AppSettings} from '../../app.settings'
import { observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TableService {
  private URL = AppSettings.API_ENDPOINT + 'table/';
  constructor(private http: HttpClient) { }
  create(name: string, database: string) {
    return this.http.get<any>(this.URL + `create/${database}/${name}`, {observe: 'response'})
  }

  query(query:string) {
    return this.http.get<any>(this.URL + `query/${query}`, {observe:'response'})
  }
}
