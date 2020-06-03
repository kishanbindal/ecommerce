import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-productgrid',
  templateUrl: './productgrid.component.html',
  styleUrls: ['./productgrid.component.css']
})
export class ProductgridComponent implements OnInit {

  allProducts

  constructor(private ds: DataService) { }

  ngOnInit(): void {
    this.ds.getAllProducts()
    this.ds.productsList.subscribe(data => {
      this.allProducts = data
      console.log('All Products : ' + this.allProducts)
    })
  }

}
