import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-addbutton',
  templateUrl: './addbutton.component.html',
  styleUrls: ['./addbutton.component.css']
})

export class AddbuttonComponent implements OnInit {

  @Input() product
  @Input() quantity


  constructor(private ds: DataService) { }

  ngOnInit(): void {
  }

  addProductQuantity(){
    this.quantity = Number(this.quantity) + 1
    console.log(this.quantity)
  }

}
