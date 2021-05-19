import { query } from '@angular/animations';
import { Component, OnInit, ViewChild } from '@angular/core';
import { faPlay, faFolderOpen, faSave, faAngleDown, faStop } from '@fortawesome/free-solid-svg-icons'
import { ServerService } from 'src/app/service/Server/server.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {

  @ViewChild("Editor") Editor

  constructor(private Server:ServerService) { }

  ngOnInit(): void {
  }

  faPlay = faPlay;
  faFolderOpen = faFolderOpen;
  faSave = faSave;
  faAngleDown = faAngleDown;
  faStop = faStop;
  content = ""
  content2 = ""

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

  public async runScript(){
    const Query:String=this.SelectText()
    document.getElementById("SpinnerLoadQuery").hidden = false
    setTimeout(()=>{},5000)
    let result_parser:any
    await this.Server.parser(Query).then(
      result=>{
        console.log(result)
        result_parser = result
      }
    )
    let result_consulta : any
    if(result_parser.Message == "Analisis Realizado Con Exito!"){
      let use=sessionStorage.getItem("use")
      let query:any
      if(use){
        query = use+Query
      }else{
        query = Query
      }
      await this.Server.consultar(query).then(
        result=>{
          console.log(result)
          result_consulta = result
        }
      )
      sessionStorage.setItem("use",`use ${result_consulta.UseTable};`)
      sessionStorage.setItem("CONSULTA",JSON.stringify(result_consulta))
      alert(result_consulta.Messages)
      this.content2 = String(result_consulta.Messages)
    }
    sessionStorage.setItem("PARSER",JSON.stringify(result_parser))
    document.getElementById("SpinnerLoadQuery").hidden = true
  }

  stopScript() {
    document.getElementById("SpinnerLoadQuery").hidden = false
  }

  private SelectText(){
    let ArrayTexto:String[] = this.content.split('\n')
    let Texto:String = ""
    const Posiciones = this.Editor.codeMirror.doc.sel.ranges[0]
    if(Posiciones.anchor.line == Posiciones.head.line){
      if(Posiciones.anchor.ch > Posiciones.head.ch){  
        let inicio = Posiciones.head.ch
        let size = Posiciones.anchor.ch - Posiciones.head.ch
        Texto = ArrayTexto[Posiciones.head.line].substr(inicio,size)
      }else if(Posiciones.anchor.ch < Posiciones.head.ch){
        let inicio = Posiciones.anchor.ch
        let size = Posiciones.head.ch - Posiciones.anchor.ch
        Texto = ArrayTexto[Posiciones.head.line].substr(inicio,size)
      }else{
        let FilaInicio=0
        for (let i = Posiciones.head.line-1; i >=0 ; i--) {//para arriba
          if(ArrayTexto[i].includes(";")){
            FilaInicio=i
            break
          }
        }
        let Concat = false;
        for (let index = 0; index < ArrayTexto[FilaInicio].length; index++) {
          if(Concat == true){
            if(index == ArrayTexto[FilaInicio].length-1){
              Texto += ArrayTexto[FilaInicio][index] + " "
            }else{
              Texto += ArrayTexto[FilaInicio][index]
            }
          }else if(ArrayTexto[FilaInicio][index]==";"){
            Concat = true
          }
        }
        let UltimaFila = false
        for (let fila = FilaInicio+1; fila < ArrayTexto.length; fila++) {
          if(ArrayTexto[fila].includes(";")){
            UltimaFila = true
          }
          for (let columna = 0; columna < ArrayTexto[fila].length; columna++) {
            if(UltimaFila == true){
              if(ArrayTexto[fila][columna] == ";"){
                Texto += ArrayTexto[fila][columna]+' '
                fila = ArrayTexto.length
                break;
              }else{
                Texto += ArrayTexto[fila][columna]
              }
            }else{
              if(columna == ArrayTexto[fila].length-1){
                Texto += ArrayTexto[fila][columna] + ' '
              }else{
                Texto += ArrayTexto[fila][columna]
              }
            }
          }
        }
      }
    }else if(Posiciones.anchor.line > Posiciones.head.line){
      Texto = ArrayTexto[Posiciones.head.line].substr(Posiciones.head.ch,ArrayTexto[Posiciones.head.line].length-Posiciones.head.ch)+" "
      for (let fila = Posiciones.head.line+1; fila <= Posiciones.anchor.line; fila++) {
        if(fila == Posiciones.anchor.line){
          Texto += ArrayTexto[fila].substr(0,Posiciones.anchor.ch)
        }else{
          Texto += ArrayTexto[fila].substr(0,ArrayTexto[fila].length)+" "
        }
      }
    }else if(Posiciones.anchor.line < Posiciones.head.line){
      Texto = ArrayTexto[Posiciones.anchor.line].substr(Posiciones.anchor.ch,ArrayTexto[Posiciones.anchor.line].length-Posiciones.anchor.ch)+" "
      for (let fila = Posiciones.anchor.line+1; fila <= Posiciones.head.line; fila++) {
        if(fila == Posiciones.head.line){
          Texto += ArrayTexto[fila].substr(0,Posiciones.head.ch)
        }else{
          Texto += ArrayTexto[fila].substr(0,ArrayTexto[fila].length)+" "
        }
      }
    }
    return Texto
  }
}
