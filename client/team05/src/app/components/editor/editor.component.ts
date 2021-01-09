import { Component, OnInit } from '@angular/core';
import { faPlay, faFolderOpen, faSave, faAngleDown, faStop } from '@fortawesome/free-solid-svg-icons'

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
  faAngleDown = faAngleDown;
  faStop = faStop;
  content = "SELECT * FROM PERSONA WHERE PERSONA.id = 0;"

  handleFileInput(event) {
    let fileList: FileList = event.target.files;
    if (fileList.length > 0) {
      const readFile = fileList[0];
      let reader = new FileReader();
      reader.onload = (e) => {
        const lines = e.target.result.toString();
        this.content = lines;
      };
      reader.onerror = (e) => alert(e.target.error.name);
      reader.readAsText(readFile);
    }
  }

  saveFile() {
    var file = new Blob([this.content], {type: 'text/plain'});
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

  runScript(){
    alert('Ejecuta el script que se encuentre en el editor');
  }

  stopScript() {
    alert('Detiene la ejecución de un script');
  }
}
