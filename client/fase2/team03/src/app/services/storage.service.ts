import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import {User} from '../model/user';
import {UserLogin} from '../model/userLogin'; //se utilizara para la sesion


@Injectable({
  providedIn: 'root'
})
export class StorageService {
  private localStorageService;
  private currentSession: UserLogin = null;


  constructor(private router: Router) {
    this.localStorageService = localStorage;
    this.currentSession = this.loadSessionData();
   }

  setCurrentSession(session: UserLogin)
  {
    this.currentSession = session;
    this.localStorageService.setItem('currentUser',JSON.stringify(session))
    console.log(`set current session`)
    console.log(this.getCurrentSession());
    localStorage.setItem('login_id',JSON.stringify(session));
  }

  loadSessionData(): UserLogin{
    var sessionStr = this.localStorageService.getItem('currentUser');
    return (sessionStr) ? <UserLogin> JSON.parse(sessionStr) : null;
  }

  getCurrentSession(): UserLogin {
    this.currentSession = JSON.parse(localStorage.getItem('currentUser'));
    //console.log(`currentSession: `);
    //console.log(this.currentSession)
    return this.currentSession;
    
  }
  removeCurrentSession(): void {
    this.localStorageService.removeItem('currentUser');
    this.currentSession = null;
  }

  isAuthenticated(): boolean {
    //console.log('isAuthenticated ' );
    //console.log(this.getCurrentId());
    /*let id :string= this.getCurrentId();
    console.log(`recibe: ${id}`);
    console.log(id);*/

    return (this.getCurrentEmail() != null) ? true : false;
  };

  isAuthenticatedAdmin(): boolean {
    var session = this.getCurrentRol();
    return (session != null && session == '1') ? true : false;
  };

  isAuthenticatedHelpDesk(): boolean {
    var session = this.getCurrentRol();
    return (session != null && session == '2') ? true : false;
  };

  isAuthenticatedCliente(): boolean {
    var session = this.getCurrentRol();
    // 3-> cliente premium 4-> plus 5-> basic
    return (session != null && (session == '3' || session == '4' || session == '5')) ? true : false;
  };

  getCurrentId(): string {
    var session = JSON.parse(localStorage.getItem('currentUser'));
    return ( session[0]!=null && session[0].ID_USUARIO != null ) ? session[0].ID_USUARIO  : null;
  };

  getCurrentNombre(): string {
    var session = JSON.parse(localStorage.getItem('currentUser'));
    return ( session[0]!=null && session[0].ID_USUARIO != null ) ? session[0].NOMBRE  : null;
  };

  getCurrentApellido(): string {
    var session = JSON.parse(localStorage.getItem('currentUser'));
    return ( session[0]!=null && session[0].ID_USUARIO != null ) ? session[0].APELLIDOS   : null;
  };

  getCurrentEmail(): string {
    var session = JSON.parse(localStorage.getItem('currentUser'));
    console.log(session);
    if (session!= null)
    {
      return ( session[0]!=null && session[0].EMAIL != null ) ? session[0].EMAIL   : null;
    }
    return null;
    
  };

  getCurrentRol(): string {
    var session = JSON.parse(localStorage.getItem('currentUser'));
    if (session!= null)
    {
      return ( session[0]!=null && session[0].ID_USUARIO != null ) ? session[0].ROL_ID_ROL   : null;
    }
    return null;
  };

  logout(): void{
    this.removeCurrentSession();
    this.router.navigate(['/login']);
  }

}
