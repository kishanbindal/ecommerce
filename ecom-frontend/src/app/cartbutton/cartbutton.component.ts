import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data-service.service';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-cartbutton',
  templateUrl: './cartbutton.component.html',
  styleUrls: ['./cartbutton.component.css']
})
export class CartbuttonComponent implements OnInit {

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openCartDialog(event){
    console.log(event)
    let rect = event.target.getBoundingClientRect()
    let leftX = rect.x + 'px';
    let topY = (rect.y+40) + 'px';
    this.dialog.open(CartbuttonDialogComponent, {
      position : {left :leftX, top: topY},
    })
  }

}

@Component({
  selector: 'app-cartbuttondialog',
  templateUrl: './cartbuttondialog.component.html',
  // styleUrls: ['./cartbuttondialog.component.css']
})
export class CartbuttonDialogComponent implements OnInit{

  cart_data

  constructor(private ds: DataService){ }

  ngOnInit(){
    this.ds.getCart()
    this.ds.cartData.subscribe(data => {
      this.cart_data = data
      console.log(this.cart_data)
    })
  }
}
