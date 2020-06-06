import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-productcard',
  templateUrl: './productcard.component.html',
  styleUrls: ['./productcard.component.css']
})
export class ProductcardComponent implements OnInit {

  @Input() product
  
  constructor(private ds : DataService) { }

  ngOnInit(): void {
  }

  requestSingleProduct(product_primary_key){
    this.ds.getProductById(product_primary_key)
  } 

}
