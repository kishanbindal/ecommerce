import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-opbutton',
  templateUrl: './opbutton.component.html',
  styleUrls: ['./opbutton.component.css']
})
export class OpbuttonComponent implements OnInit {

  @Input() product
  @Input() quantity

  @Output() updatedQuantity = new EventEmitter<Number>()

  constructor(private ds: DataService) { }

  ngOnInit(): void {
    // setTimeout(() => {
    //   console.log(this.product.id)
    // }, 250);
  }

  addProductQuantity(){
    // var intermediateQuant = Number(this.quantity)
    // intermediateQuant += 1
    this.quantity = Number(this.quantity) + 1
    let data = {
      'quantity': this.quantity
    }
    this.ds.updateOrderItem(this.product.id, data)
    // this.updatedQuantity.emit(this.quantity)
  }

  reduceProductQuantity(){
    if (this.quantity >> 1){
      this.quantity = Number(this.quantity) - 1
      let data = {
        'quantity': this.quantity
      }
      this.ds.updateOrderItem(this.product.id, data)
    }
  }

  removeOrderItem(){
    this.ds.deleteOrderItem(this.product.id).subscribe(response => {
      console.log(response)
      if (response['success'] === true) {
        this.ds.getCart()
      }
    })
  }

}
