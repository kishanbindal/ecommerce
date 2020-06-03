import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-productcard',
  templateUrl: './productcard.component.html',
  styleUrls: ['./productcard.component.css']
})
export class ProductcardComponent implements OnInit {

  @Input() product
  
  constructor() { }

  ngOnInit(): void {
  }

}
