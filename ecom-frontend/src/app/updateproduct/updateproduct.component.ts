import { Component, OnInit, Input, Inject, OnChanges, ɵɵNgOnChangesFeature, } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormControl } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';
import { DataService } from '../services/data-service.service';

@Component({
  selector: 'app-updateproduct',
  templateUrl: './updateproduct.component.html',
  styleUrls: ['./updateproduct.component.css']
})
export class UpdateproductComponent implements OnInit {

  @Input() product;

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  productUpdateDialog(){
    const dialogRef = this.dialog.open(UpdateProductDialogComponent,{
      height: '25em',
      width: '40em',
      data: this.product
    })
  }

}

@Component({
  selector: 'app-updateproductdialog',
  templateUrl: './updateproductdialog.component.html',
})
export class UpdateProductDialogComponent implements OnChanges{

  imgDomUrl

  product_name = new FormControl('')
  product_image
  product_quantity = new FormControl('')
  product_price = new FormControl('')

  constructor(public dialogRef: MatDialogRef<UpdateProductDialogComponent>,
    private domSanitizer: DomSanitizer,
    private ds: DataService,
    @Inject(MAT_DIALOG_DATA) public data: any){
      // console.log(data)
      console.log(this.data)
      this.product_name.setValue(this.data['name']);
      this.product_image = this.data['images']
      this.product_quantity.setValue(this.data['quantity']);
      this.product_price.setValue(this.data['price']);

    //   console.log(this.product_name.value);
    //   console.log(this.product_image.value);
    //   console.log(this.product_quantity.value);
    //   console.log(this.product_price.value)
    }

  // Not Relevant
  ngOnChanges():void {
    this.product_image.valueChanges.subscribe(dataChange => {
      console.log(dataChange)
    })
  }

  // GET Image And Display

  getImageFile($event){
    var uploadImage = $event.target.files[0]
    console.log(uploadImage)
    this.product_image = uploadImage // File to Upload to the server
    var reader = new FileReader()
    this.imgDomUrl = this.domSanitizer.bypassSecurityTrustUrl(JSON.stringify(reader.result))
  }

  sendUpdateRequest(){
    let uploadData = new FormData()
    let data = {
      'name': this.product_name.value,
      'quantity': this.product_quantity.value,
      'images': this.product_image,
      'price': this.product_price.value
    }
    for (var key in data) {
      uploadData.append(key, data[key])
    }
    this.ds.updateProduct(uploadData, this.data.id).subscribe(response => {
      console.log(response)
    })
  }
  
}
