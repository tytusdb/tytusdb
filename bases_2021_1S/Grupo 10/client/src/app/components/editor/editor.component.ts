import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ShareService } from 'src/app/service/share/share.service';
import { Subscription } from 'rxjs';
import { TableDataService } from '../../service/tableData/table-data.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})

export class EditorComponent implements OnInit, OnDestroy {

  message: string;
  subscription: Subscription;

  //tabs
  tabs = [];
  selected = new FormControl(0);
  codeArray = [];

  constructor(private data: ShareService, private servicio: TableDataService) { }

  ngOnInit(): void {
    this.subscription = this.data.currentMessage.subscribe(message => this.message = message);
    this.onAddTab();
  }

  
  ngOnDestroy() {
      this.subscription.unsubscribe();
  }

  onOpenFile(event){
    const fileList: FileList = event.target.files;
      if (fileList.length > 0) {
        const readFile = fileList[0];
        const reader = new FileReader();
        reader.onload = (e) => {
          const lines = e.target.result.toString();
          this.onAddTab( lines )
        };
        reader.onerror = (e) => alert(e.target.error.name);
        reader.readAsText(readFile);
      }
  }

  onSaveFile(){
    const file = new Blob([this.getCode()], { type: 'text/plain' });
    if (window.navigator.msSaveOrOpenBlob) {
      window.navigator.msSaveOrOpenBlob(file, 'script.sql');
    } else {
      const a = document.createElement('a'),
        url = URL.createObjectURL(file);
      a.href = url;
      a.download = 'script.sql';
      document.body.appendChild(a);
      a.click();
      setTimeout(() => {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
      }, 0);
    }
  }

  onAddTab( str: string = '\n\n\n\n\n\n\n\n\n') {
    this.tabs.push('Query Console ' + (this.tabs.length + 1) );
    this.selected.setValue(this.tabs.length - 1);
    this.codeArray.push( str );
  }

  onRunScript(){
    
    this.servicio.create({query: this.getCode()}).subscribe((response) => {
      const body = response.body;
      this.data.changeMessage(body);
      console.log(body);
      this.clickMe();
    }, err => console.log(err));   
  }

  onRemoveTab(index: number) {
    if ( this.tabs.length === 1 ) { return }
    this.tabs.splice(index, 1);
    this.codeArray.splice(index, 1);
  }


  handleChange($event: Event): void {
    this.codeArray[this.selected.value] = $event;
  }

  private getCode() : string {
    return this.codeArray[this.selected.value]
  }
  
  clickMe(){
    this.data.sendClickEvent();
  }


}
