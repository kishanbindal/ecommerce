import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-opbutton',
  templateUrl: './opbutton.component.html',
  styleUrls: ['./opbutton.component.css']
})
export class OpbuttonComponent implements OnInit {

  @Input() product
  @Input() quantity

  constructor(private ds: DataService) { }

  ngOnInit(): void {
    setTimeout(() => {
      console.log(this.product.id)
    }, 250);
  }
}
