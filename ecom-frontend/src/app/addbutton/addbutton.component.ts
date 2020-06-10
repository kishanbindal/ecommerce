import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-addbutton',
  templateUrl: './addbutton.component.html',
  styleUrls: ['./addbutton.component.css']
})
export class AddbuttonComponent implements OnInit {

  @Input() product

  constructor(private ds: DataService) { }

  ngOnInit(): void {
  }

  addProduct(){
    let data = {
      'product': this.product.id,
      'quantity': 1,
      'subtotal': this.product.price,
      'is_billed': false
    }
    this.ds.addOrderItem(data).subscribe(response => console.log(response))
  }

}
