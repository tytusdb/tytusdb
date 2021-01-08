import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {AppSettings} from '../../app.settings';

@Injectable({
  providedIn: 'root'
})
export class ServiceTreeService {

  constructor(private http:HttpClient) { }

  getData_treedatabase(){
    return  this.http.get(AppSettings.API_ENDPOINT+`db/showall`)
  }
}
