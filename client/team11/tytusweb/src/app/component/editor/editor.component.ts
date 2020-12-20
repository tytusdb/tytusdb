import { Component, OnInit,ElementRef, ViewChild } from '@angular/core';


@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
  
})
export class EditorComponent implements OnInit {
  constructor( ){ 
   };
   text:string = "";
   options:any = {maxLines: 30,minLines:30,printMargin: false};
  ngOnInit(): void {
  }

}
