import { Component, OnInit } from '@angular/core';
import { faPlay, faFolderOpen, faSave, faAngleDown, faStop } from '@fortawesome/free-solid-svg-icons'
import { TableService } from 'src/app/service/table/table.service';
import {MatPaginator} from '@angular/material/paginator';
import {MatPaginatorModule} from '@angular/material/paginator';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})

export class EditorComponent implements OnInit {

  constructor(private tbServs: TableService) { }
  
  ngOnInit(): void {
  }

  Columns:Array<string> = ["Alita","Patita"] 
  Rows:Array<any>=[[1,2],[2,3],[3,4]]

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
    this.tbServs.query(this.content).subscribe(o=>{
      console.log(o);
      if(o.body.msg.syntax.length > 0 || o.body.msg.lexical.length > 0 || o.body.msg.semantic.length > 0)
      {
        alert(JSON.stringify(o.body.msg.sintax)+"\n"+JSON.stringify(o.body.msg.lexical)+"\n"+JSON.stringify(o.body.msg.semantic))
      }else{
        alert(o.body.msg.messages)
      }
      if (o.body.msg.querys.length > 0){
        this.Columns = o.body.msg.querys[0][0]
        this.Rows = o.body.msg.querys[0][1]
        console.log(this.Columns,this.Rows)
      }
    })
  }

  stopScript() {
    alert('Detiene la ejecución de un script');
  }
}
