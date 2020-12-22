import { Injectable } from '@angular/core';
import {HttpClient, HttpEventType} from '@angular/common/http';

import {User} from '../model/user';
import {UserLogin} from '../model/userLogin';
import {Bitacora} from '../model/bitacora';

import {Observable} from "rxjs/Rx";
import 'rxjs/Rx';
import { map } from  'rxjs/operators';
//import './rxjs-operators';
//import 'rxjs/add/operators/map';
//import { map } from 'rxjs/operators';
//import 'rxjs-compat';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  domain: string = "http://localhost:3000";
  constructor(private http: HttpClient) { }
  
  getDomain()
  {
    return this.domain;
  }

  login(username: string, password: string)
  {
    return this.http.post(`${this.domain}/user/login/`,{
      Id_Usuario: username,
      Password: password,
    });
  }

  loginEmail(username: string, password: string)
  {
    console.log(`username: ${username}`);
    return this.http.post(`${this.domain}/user/loginEmail/`,{
      Email: username,
      Password: password,
    });
  }

  loginObject(login: UserLogin)
  {
    //var usuario : User = this.http.post<User>(`${this.domain}/user/login/`,login);
    //login.ID_USUARIO = usuario.body.i;

    return this.http.post(`${this.domain}/user/login/`,{
      Id_Usuario: login.ID_USUARIO,
      Password: login.PASSWORD,
    }); 
  }

  setUser(newUser){
    return this.http.post(`${this.domain}/user/insert`,newUser);
  }
  getUsers()
  {
    return this.http.get(`${this.domain}/user/allUsers`);
  }
  getUser(id: any)
  {
    console.log('servicio');
    console.log(id)
    return this.http.post(`${this.domain}/user/getProfile`,id);
  }

  getUser2(id: any): Observable<User>
  {
    console.log('servicio');
    console.log(id)
    return this.http.post<User>(`${this.domain}/user/getProfile`,id);
  }

  getUsuarios(): Observable<User>{
    return this.http.get<User>('http://localhost:3000/user/users');
  }

  updateEstado(id: any)
  {
    return this.http.post(`${this.domain}/user/changeStatus`,id);
  }

  updateUser(newUser: User){
    return this.http.put(`${this.domain}/user/update/${newUser.ID_USUARIO}`,newUser);
  }

  deleteUser(Id_Usuario:number){
    return this.http.delete(`${this.domain}/user/delete/${Id_Usuario}`);
  }

  private extractData(res: Response) {
    let body = res.json();
    return body;
  }

  public upload(data, userId) {
    let uploadURL = `${this.domain}/uploadUser`;

    return this.http.post<any>(uploadURL, data, {
      reportProgress: true,
      observe: 'events'
    }).pipe(map((event) => {

      switch (event.type) {

        case HttpEventType.UploadProgress:
          const progress = Math.round(100 * event.loaded / event.total);
          return { status: 'progress', message: progress };

        case HttpEventType.Response:
          return event.body;
        default:
          return `Unhandled event: ${event.type}`;
      }
    })
    );
  }

  enviarCorreoConfirmacion(email:string){
    console.log(email);
    return this.http.post(`${this.domain}/user/enviarCorreo/`,{
      asunto: 'Confirmacion de Creacion  de usuario',
      contenido: 'Usted ha creado una cuenta en Publishells http://localhost:4200/confirmacion',
      emailTo: `${email}`
    });
  }

  getRoles()
  {
    return this.http.get<User[]>(`${this.domain}/user/allUsers`);
  }

  getAllBitacora() 
  {
    return this.http.get<Bitacora[]>(`${this.domain}/user/getBitacora`).subscribe();
  }
  getAllBitacora2() 
  {
    return this.http.get(`${this.domain}/user/getBitacora`).subscribe();
  }
  getLog()
  {
    return this.http.get(`${this.domain}/user/getBitacora`);
  }
  setLogUserConfirm(id: any)
  {
    return this.http.post(`${this.domain}/user/setBitacora`,id);
  }

  recuperarPass(id: any)
  {
    return this.http.post(`${this.domain}/user/recuperarPass`,id);
  }
  validarPass(id: any)
  {
    return this.http.post(`${this.domain}/user/validarPass`,id);
  }

}
