import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-adminpage',
  templateUrl: './adminpage.component.html',
  styleUrls: ['./adminpage.component.css']
})
export class AdminpageComponent implements OnInit {

  allProducts

  constructor(private ds: DataService) { }

  ngOnInit(): void {
    this.ds.getAllProducts()
    this.ds.productsList.subscribe(data => {
      this.allProducts = data
    })
  }

}
