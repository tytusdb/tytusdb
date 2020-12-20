import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  private URL = 'http://localhost:5000/database/'
  constructor(private http: HttpClient) { }
  create(name: string) {
    return this.http.get<any>(this.URL + `create/${name}`, { observe: 'response' })
  }

}
