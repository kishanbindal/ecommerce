import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';
import { FormControl } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-addtocart',
  templateUrl: './addtocart.component.html',
  styleUrls: ['./addtocart.component.css']
})
export class AddtocartComponent implements OnInit {

  @Input() product

  quantity: number

  constructor(private ds: DataService,
    private _snackbar: MatSnackBar) { }

  ngOnInit(): void {
  }

  addProduct(){
    this.ds.getAllProducts()
    let data = {
      'product' : this.product.id,
      'price': this.product.price,
      'quantity': this.quantity,
      'subtotal': this.quantity * this.product.price,
      'is_billed': false,
    }
    console.log(data.subtotal)
    setTimeout(()=> {
      this.ds.addOrderItem(data).subscribe(response => {
        console.log(response)
        if (response['success'] === true){
          this._snackbar.open('Product was successfully added to your cart', 'close', {duration:2000})
          this.quantity = 0;
        }
      })
    }, 250)
    
  }

}
