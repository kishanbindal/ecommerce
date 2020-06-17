import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-checkoutpage',
  templateUrl: './checkoutpage.component.html',
  styleUrls: ['./checkoutpage.component.css']
})
export class CheckoutpageComponent implements OnInit {

  cart

  constructor(private ds: DataService) { }

  ngOnInit(): void {
    this.ds.getCart()
    this.ds.cartData.subscribe(data => {
      this.cart = data
    })
    setTimeout(()=> {
      console.log(this.cart);
      var total = 0
      for (const item of this.cart.items) {
        console.log(item)
        total += Number(item['subtotal'])
      }
      this.cart.total_amount = total
    }, 150)
  }

}
