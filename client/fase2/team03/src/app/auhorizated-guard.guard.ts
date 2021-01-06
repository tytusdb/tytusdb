import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import {StorageService} from './services/storage.service';



@Injectable({
  providedIn: 'root'
})
export class AuhorizatedGuardGuard implements CanActivate {

  constructor(private router: Router,
    private storageService: StorageService
    )
  {

  }
  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

      if (this.storageService.isAuthenticated()) {
        // logged in so return true
        console.log('trueeee');
        return true;
      }
      // not logged in so redirect to login page
      console.log('falsee');
      this.router.navigate(['/pageNotFound']);
      return false;
    
    
  }

  canActivateAdmin(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      console.log('holaaa');
      console.log(`es Autenticado: ${this.storageService.isAuthenticated()}`); //esta autenticado
      if (this.storageService.isAuthenticatedAdmin()) {
        // logged in so return true
        return true;
      }
      // not logged in so redirect to login page
      this.router.navigate(['/pageNotFound']);
      return false;
    
    
  }
  
}
