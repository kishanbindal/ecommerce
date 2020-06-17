import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-productcard',
  templateUrl: './productcard.component.html',
  styleUrls: ['./productcard.component.css']
})
export class ProductcardComponent implements OnInit {

  @Input() product

  url : SafeUrl;
  
  constructor(private ds : DataService, 
    private domSanitizer: DomSanitizer) { }

  ngOnInit(): void {
    console.log(this.product)
    if (this.product.images != null){
      this.url = this.domSanitizer.bypassSecurityTrustUrl(this.product.images)
    }
  }

  requestSingleProduct(product_primary_key){
    this.ds.getProductById(product_primary_key)
  } 

}
