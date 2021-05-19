import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { promise } from 'selenium-webdriver';

@Injectable({
  providedIn: 'root'
})
export class ServerService {

  constructor(private http:HttpClient) { }

  private URL_SERVER = "http://localhost:7778" //Tytus

  public parser(Query:String):Promise<any>{
    let JSO = { entrada : Query }
    return this.http.post<any>(`${this.URL_SERVER}/Tytus/parser`,JSO).toPromise()
  }

  public consultar(Query:String):Promise<any>{
    let JSO = { entrada : Query }
    return this.http.post<any>(`${this.URL_SERVER}/Tytus/consultar`,JSO).toPromise()
  }

  public reportTBL(database):Promise<any>{
    let JSO = { nameDB : database}
    return this.http.post<any>(`${this.URL_SERVER}/Tytus/EDD/reportTBL`,JSO).toPromise()
  }

  public reportDB():Promise<any>{
    let JSO = {}
    return this.http.post<any>(`${this.URL_SERVER}/Tytus/EDD/reportDB`,JSO).toPromise()
  }

  public reportAVL(database,tabName):Promise<any>{
    let JSO = {nameDB:database,nameTab:tabName}
    return this.http.post<any>(`${this.URL_SERVER}/Tytus/EDD/reportAVL`,JSO).toPromise()
  }

  public reportTPL(database,tabName,llabe):Promise<any>{
    let JSO = {nameDB:database,nameTab:tabName,llave:llabe}
    return this.http.post<any>(`${this.URL_SERVER}/Tytus/EDD/reportTPL`,JSO).toPromise()
  }

}
