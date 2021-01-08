import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {AppSettings} from '../../app.settings';

@Injectable({
  providedIn: 'root'
})
export class TableDataService {
  private URL = AppSettings.API_ENDPOINT + '*************/'; // ruta por definir
  constructor(private http: HttpClient) { }
  // tslint:disable-next-line:typedef
  public create(query: string) {
    return this.http.get<any>(this.URL + `create/${query}`, {observe: 'response'}); // ruta por definir
  }
}
