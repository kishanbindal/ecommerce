import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/data-service.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-deletebutton',
  templateUrl: './deletebutton.component.html',
  styleUrls: ['./deletebutton.component.css']
})
export class DeletebuttonComponent implements OnInit {

  @Input() id: number;

  constructor(private ds: DataService,
    private snackbar: MatSnackBar) { }

  ngOnInit(): void {
  }

  sendDeleteRequest(){
    this.ds.deleteProduct(this.id).subscribe(response => {
      console.log(response)
      if(response['success'] == true){
        this.snackbar.open('Successfully Removed/Deleted Product', 'close',{
          duration: 1500
        })
        this.ds.getAllProducts()
      }
      else{
        this.snackbar.open(response['message'], 'close', {duration: 3000})
      }
    }, (error)=> {
      this.snackbar.open(error, 'close', {duration: 1500})
    })
  }

}
