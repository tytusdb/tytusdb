import { Component, OnInit,ElementRef, ViewChild } from '@angular/core';
/*import * as ace from 'ace-builds';
import 'ace-builds/src-noconflict/mode-javascript';
import 'ace-builds/src-noconflict/theme-github';
const THEME = 'ace/theme/github';
const LANG = 'ace/mode/javascript';*/
@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {
  constructor( /*private codeEditor: ace.Ace.Editor */){ 
   };

  ngOnInit(): void {
  /*  const element = this.codeEditorElmRef.nativeElement;
    this.codeEditor.setTheme(THEME);
    this.codeEditor.getSession().setMode(LANG);
    this.codeEditor.setShowFoldWidgets(true); // for the scope fold feature*/
  }

}
