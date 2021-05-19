import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import {AppSettings} from '../../app.settings'

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  private URL = AppSettings.API_ENDPOINT + 'db/';
  constructor(private http: HttpClient) { }
  create(name: string) {
    return this.http.get<any>(this.URL + `create/${name}`, { observe: 'response' })
  }

  showAll(){
    return this.http.get<any>(this.URL + `showall`)
  }
}
