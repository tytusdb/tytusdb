import { Component, OnInit } from '@angular/core';
import { faPlay, faFolderOpen, faSave } from '@fortawesome/free-solid-svg-icons'

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  faPlay = faPlay;
  faFolderOpen = faFolderOpen;
  faSave = faSave;
  content = "SELECT * FROM PERSONA WHERE PERSONA.id = 0;"
}
