import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {AppSettings} from '../../app.settings';

@Injectable({
  providedIn: 'root'
})
export class TableDataService {
  private URL = AppSettings.API_ENDPOINT + 'query/';

  constructor(private http: HttpClient) { }
  // tslint:disable-next-line:typedef
  public create(query: any) {
    return this.http.post<any>(this.URL + 'exec', query, {observe: 'response'});
  }
}
