import { Component, OnInit, Input, Inject, } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormControl } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';

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
export class UpdateProductDialogComponent {

  imgDomUrl

  product_name = new FormControl('')
  product_image = new FormControl('') 
  product_quantity = new FormControl('')
  product_price = new FormControl('')

  constructor(public dialogRef: MatDialogRef<UpdateProductDialogComponent>,
    private domSanitizer: DomSanitizer,
    @Inject(MAT_DIALOG_DATA) public data: any){
      console.log(data)
      this.product_name.setValue(this.data['name']);
      this.product_image.setValue(this.data['images']);
      this.product_quantity.setValue(this.data['quantity']);
      this.product_price.setValue(this.data['price']);
    }

  // GET Image And Display

  getImageFile($event){
    var uploadImage = $event.target.files[0]
    this.product_image = uploadImage // File to Upload to the server
    var reader = new FileReader()
    this.imgDomUrl = this.domSanitizer.bypassSecurityTrustUrl(JSON.stringify(reader.result))
  }
  
}
