import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-renametable',
  templateUrl: './renametable.component.html',
  styleUrls: ['./renametable.component.scss']
})
export class RenametableComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  renametable(event:Event)
  {
    alert("Modificando table.....");
  }

}
