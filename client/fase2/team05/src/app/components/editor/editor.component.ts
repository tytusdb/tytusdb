import {Component, OnDestroy, OnInit} from '@angular/core';
import { faPlay, faFolderOpen, faSave, faAngleDown, faStop } from '@fortawesome/free-solid-svg-icons';
import { ThemePalette } from '@angular/material/core';
import { FormControl } from '@angular/forms';
import { ShareService } from 'src/app/service/share/share.service';
import { Subscription } from 'rxjs';
import {TableDataService} from '../../service/tableData/table-data.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit, OnDestroy {

  message: string;
  subscription: Subscription;

  constructor(private data: ShareService, private servicio: TableDataService) { }

  contador = 5;

  tabs = ['tab4'];
  selected = new FormControl(0);
  background: ThemePalette = undefined;

  faPlay = faPlay;
  faFolderOpen = faFolderOpen;
  faSave = faSave;
  faAngleDown = faAngleDown;
  faStop = faStop;

  content0 = '';
  content1 = '';
  content2 = '';
  content3 = '';
  content4 = '';
  content5 = '';

  ngOnInit(): void {
    this.subscription = this.data.currentMessage.subscribe(message => this.message = message);
  }

  // tslint:disable-next-line:typedef
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  // tslint:disable-next-line:typedef
  newMessage() {
    // ------------------------

    this.servicio.create({query: this.get()}).subscribe((response) => {
      const body = response.body;
      // const msg = body;
      this.data.changeMessage(body);
      this.clickMe();
    }, err => console.log(err));
    // -----------------------
  }

  // tslint:disable-next-line:typedef
  clickMe(){
    this.data.sendClickEvent();
  }

  // tslint:disable-next-line:typedef
  handleFileInput(event) {
    const fileList: FileList = event.target.files;
    if (fileList.length > 0) {
      const readFile = fileList[0];
      const reader = new FileReader();
      reader.onload = (e) => {
        const lines = e.target.result.toString();
        switch (this.selected.value) {
          case 0:
            this.content0 = lines;
            break;
          case 1:
            this.content1 = lines;
            break;
          case 2:
            this.content2 = lines;
            break;
          case 3:
            this.content3 = lines;
            break;
        }

        // this.content1 = lines;
      };
      reader.onerror = (e) => alert(e.target.error.name);
      reader.readAsText(readFile);
    }
  }

  // tslint:disable-next-line:typedef
  saveFile() {
    const file = new Blob([this.get()], { type: 'text/plain' });
    if (window.navigator.msSaveOrOpenBlob) {
      window.navigator.msSaveOrOpenBlob(file, 'script.sql');
    } else {
      // tslint:disable-next-line:one-variable-per-declaration
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

  // tslint:disable-next-line:typedef
  runScript() {
    alert('Ejecuta el script que se encuentre en el editor');
  }

  // tslint:disable-next-line:typedef
  stopScript() {
    alert('Detiene la ejecución de un script');
  }

  // tslint:disable-next-line:typedef
  get() {
    let mensaje;
    switch (this.selected.value) {
      case 0:
        alert('\'' + this.content0.trim() + '\'');
        mensaje = this.content0.trim();
        break;
      case 1:
        alert('\'' + this.content1.trim() + '\'');
        mensaje = this.content1.trim();
        break;
      case 2:
        alert('\'' + this.content2.trim() + '\'');
        mensaje = this.content2.trim();
        break;
      case 3:
        alert('\'' + this.content3.trim() + '\'');
        mensaje = this.content3.trim();
        break;
    }
    return mensaje;
  }
  // tslint:disable-next-line:typedef
  addTab(selectAfterAdding: boolean) {

    this.contador++;
    this.tabs.push('tab' + this.contador);

    if (selectAfterAdding) {
      this.selected.setValue(this.tabs.length - 1);
    }
  }

  // tslint:disable-next-line:typedef
  removeTab(index: number) {
    this.tabs.splice(index, 1);
  }

}
