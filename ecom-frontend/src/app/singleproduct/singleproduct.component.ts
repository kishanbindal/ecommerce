import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-singleproduct',
  templateUrl: './singleproduct.component.html',
  styleUrls: ['./singleproduct.component.css']
})
export class SingleproductComponent implements OnInit {

  product

  constructor(private ds : DataService) {
    this.ds.productIdItem.subscribe(data => {
      console.log(data)
      this.product = data
      console.log(this.product)
    })
   }

  ngOnInit(): void {
    // GET PRODUCT BY ID
    this.ds.productIdItem.subscribe(data => {
      this.product = data
    })
  }

}
