import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-renamedatabase',
  templateUrl: './renamedatabase.component.html',
  styleUrls: ['./renamedatabase.component.scss']
})
export class RenamedatabaseComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  
  renamedatabase(event:Event)
  {
    alert("Modificando base de datos.....");
  }

}
