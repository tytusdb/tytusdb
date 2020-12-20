import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class TableService {
  private URL = 'http://localhost:5000/table/'
  constructor(private http: HttpClient) { }
  create(name: string, database: string) {
    return this.http.get<any>(this.URL + `create/${database}/${name}`, {observe: 'response'})
  }
}
