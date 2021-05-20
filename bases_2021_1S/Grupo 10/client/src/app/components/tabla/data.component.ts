import { Component, OnDestroy, OnInit } from '@angular/core';
import { TableDataService } from 'src/app/service/tableData/table-data.service';
import { ShareService } from 'src/app/service/share/share.service';
import { Subscription } from 'rxjs';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})

export class DataComponent implements OnInit, OnDestroy {

  message: any;
  subscription: Subscription;

  //tabs
  tabs: Array<number> = [];
  selected = new FormControl(0);
  arrayResult: Array<any> = []

  constructor(private servicio: TableDataService, private data: ShareService) {
    this.subscription =    this.data.getClickEvent().subscribe(() => {
      this.refresh();
    });

  }

  anuncio: any;

  ngOnInit(): void {
    this.subscription = this.data.currentMessage.subscribe(message => this.message = message);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  private concatMessages (tittle: string, array :Array<string>){
    this.anuncio += tittle.toUpperCase() + "\n";

    for (const msg of array) 
      this.anuncio += msg + "\n"
    
  }

  refresh(){
    this.anuncio = "";
    this.tabs = []

    if (this.message.result.messages.length > 0)
      this.concatMessages("resultados", this.message.result.messages)

    if (this.message.result.lexical.length > 0)
      this.concatMessages("errores lexicos", this.message.result.lexical)
    
    if (this.message.result.postgres.length > 0)
      this.concatMessages("errores sintacicos", this.message.result.postgres)
    
    if (this.message.result.semantic.length > 0)
      this.concatMessages("errores semanticos", this.message.result.semantic)

      
      this.arrayResult = this.message.result.querys;
      
      if (this.arrayResult[0] != null){

        for (const item of this.arrayResult) {
          this.onAddTab()
        }
    }

  }

  onAddTab() {
    this.tabs.push( this.tabs.length );
  }

  onRemoveTab(index: number) {
    this.tabs.splice(index, 1);
  }

}