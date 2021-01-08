import { Component, OnInit } from '@angular/core';
import { faPlay, faFolderOpen, faSave, faAngleDown, faStop } from '@fortawesome/free-solid-svg-icons'
import { ThemePalette } from '@angular/material/core';
import { FormControl } from '@angular/forms';
@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']


})
export class EditorComponent implements OnInit {
  contador = 5
  constructor() { }

  tabs = ['tab4'];
  selected = new FormControl(0);
  background: ThemePalette = undefined;

  ngOnInit(): void {

  }

  faPlay = faPlay;
  faFolderOpen = faFolderOpen;
  faSave = faSave;
  faAngleDown = faAngleDown;
  faStop = faStop;

  content0 = ""
  content1 = ""
  content2 = ""
  content3 = ""
  content4 = ""
  content5 = ""

  handleFileInput(event) {
    let fileList: FileList = event.target.files;
    if (fileList.length > 0) {
      const readFile = fileList[0];
      let reader = new FileReader();
      reader.onload = (e) => {
        const lines = e.target.result.toString();
        switch (this.selected.value) {
          case 0:
            this.content0=lines
            break;
          case 1:
            this.content1=lines
            break;
          case 2:
            this.content2=lines
            break;
          case 3:
            this.content3=lines
            break;
        }

        //this.content1 = lines;
      };
      reader.onerror = (e) => alert(e.target.error.name);
      reader.readAsText(readFile);
    }
  }

  saveFile() {
    var file = new Blob([this.get()], { type: 'text/plain' });
    if (window.navigator.msSaveOrOpenBlob) {
      window.navigator.msSaveOrOpenBlob(file, "script.sql");
    } else {
      var a = document.createElement("a"),
        url = URL.createObjectURL(file);
      a.href = url;
      a.download = "script.sql";
      document.body.appendChild(a);
      a.click();
      setTimeout(() => {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
      }, 0);
    }
  }

  runScript() {
    alert('Ejecuta el script que se encuentre en el editor');
  }

  stopScript() {
    alert('Detiene la ejecución de un script');
  }

  get() {
    let mensaje
    switch (this.selected.value) {
      case 0:
        alert("'" + this.content0.trim() + "'")
        mensaje= this.content0.trim()
        break;
      case 1:
        alert("'" + this.content1.trim() + "'")
        mensaje= this.content1.trim()
        break;
      case 2:
        alert("'" + this.content2.trim() + "'")
        mensaje= this.content2.trim()
        break;
      case 3:
        alert("'" + this.content3.trim() + "'")
        mensaje= this.content3.trim()
        break;
    }
    return mensaje
  }
  addTab(selectAfterAdding: boolean) {

    this.contador++
    this.tabs.push('tab' + this.contador);

    if (selectAfterAdding) {
      this.selected.setValue(this.tabs.length - 1);
    }
  }

  removeTab(index: number) {
    this.tabs.splice(index, 1);
  }

}
