import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-deletedatabase',
  templateUrl: './deletedatabase.component.html',
  styleUrls: ['./deletedatabase.component.scss']
})
export class DeletedatabaseComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  deletedatabase(event:Event)
  {
    alert("Eliminado base de datos.....");
  }
}
