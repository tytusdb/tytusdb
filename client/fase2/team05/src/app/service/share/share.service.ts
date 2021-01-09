import { Injectable } from '@angular/core';
import {BehaviorSubject, Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShareService {

  // To share data
  private messageSource = new BehaviorSubject('{}');
  currentMessage = this.messageSource.asObservable();

  // To share a function
  private subject = new Subject<any>();
  // tslint:disable-next-line:typedef
  sendClickEvent() {
    this.subject.next();
  }
  getClickEvent(): Observable<any>{
    return this.subject.asObservable();
  }


  constructor() { }

  // tslint:disable-next-line:typedef
  changeMessage(message: string) {
    this.messageSource.next(message);
  }

}
