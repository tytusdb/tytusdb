import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { EventEmitter } from 'events';
import { EditorComponent } from '../editor/editor.component';

@Component({
  selector: 'app-console',
  templateUrl: './console.component.html',
  styleUrls: ['./console.component.css']
})
export class ConsoleComponent implements OnInit {
  constructor() {
    this.state = ""
    this.encabezados = []
    this.resultados = []
    this.querys = []
    this.errores = ""
  }
  @Input() public state:string;  
  @Input() public encabezados:any[]
  @Input() public resultados:any[]
  @Input() public querys:any[]
  @Input() public errores:string;  

  ngOnInit(): void {
  }
}
