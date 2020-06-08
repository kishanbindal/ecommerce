import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MatDialogRef, MatDialog } from '@angular/material/dialog';
import { DataService } from '../services/data-service.service';
import { MatSnackBar } from '@angular/material/snack-bar';

// interface Product {
//   name: string,
//   image: File,
//   quantity: number,
//   price: number
// }

@Component({
  selector: 'app-addproduct',
  templateUrl: './addproduct.component.html',
  styleUrls: ['./addproduct.component.css']
})
export class AddproductComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openAddProductDialog(){
    this.dialog.open(AddproductDialogComponent,{
      height: '25rem',
      width: '40rem',
    })
  }

}

@Component({
  selector: 'app-addproductdialog',
  templateUrl: './addproductdialog.component.html',
  // styleUrls: ['./addproduct.component.css']
})
export class AddproductDialogComponent {

  product_name = new FormControl('');
  product_image = null;
  product_quantity = new FormControl('');
  product_price = new FormControl('');

  constructor(private ds : DataService,
    private dialogRef: MatDialogRef<AddproductDialogComponent>,
    private _snackbar: MatSnackBar){ }

  submitAddProductData(){
    let data = {
      name: this.product_name.value,
      images: this.product_image,
      quantity: this.product_quantity.value,
      price: this.product_price.value,
    }
    console.log('Data to backend : ');
    console.log(data)
    // this.ds.addProduct(data).subscribe(response => {
    //   console.log(response)
    //   if (response['success'] == true){
    //     this.ds.getAllProducts()
    //     this._snackbar.open('Product Has been Created', 'close',{duration: 1500})
    //     this.dialogRef.close()
    //   }
    // })
  }

  getImage($event){
    console.log($event);
    let fileToUpload = $event.target.files[0];
    console.log(fileToUpload)
    var reader = new FileReader();
    reader.readAsDataURL(fileToUpload);
    console.log(JSON.stringify(reader.result))
    console.log(reader.result)
  }
}
