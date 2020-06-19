import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data-service.service';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-checkoutpage',
  templateUrl: './checkoutpage.component.html',
  styleUrls: ['./checkoutpage.component.css']
})
export class CheckoutpageComponent implements OnInit {

  cart

  address1 = new FormControl();
  address2 = new FormControl();
  city = new FormControl();
  state = new FormControl();
  country = new FormControl();

  constructor(private ds: DataService,
    private router: Router,
    private snackbar: MatSnackBar) { }

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

  updateAddress(){
    var uploadData = this.cart
    console.log("Upload Data :")
    console.log(uploadData)
    uploadData["address"] =  `${this.address1.value},${this.address2.value}, ${this.city.value}, ${this.state.value}, ${this.country.value}`
    this.ds.updateCart(this.cart.id, uploadData).subscribe(response => {
      console.log(response)
      if (response['success'] === true){
        this.ds.getCart()
      }
    })
  }

  placeOrder(){
    var uploadData = this.cart
    uploadData['order_placed'] = true
    this.ds.updateCart(this.cart.id, uploadData).subscribe(response => {
      if (response['success'] == true){
        this.snackbar.open("Order Placed Successfully, COnfirmation Message has Been Sent to your Number","close", {duration: 3000})
        this.router.navigate([''])
      }
    })
  }

}
