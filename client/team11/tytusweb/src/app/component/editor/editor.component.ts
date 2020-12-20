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
   options:any = {maxLines: 20,minLines:20,printMargin: false};
  ngOnInit(): void {
  }

}
