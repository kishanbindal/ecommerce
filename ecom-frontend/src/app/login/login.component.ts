import { Component, OnInit, Output, EventEmitter} from '@angular/core';
import { MatDialog, MatDialogClose, MatDialogRef } from '@angular/material/dialog';
import { LoginService} from '../services/login-service.service'
import { FormControl } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @Output() loggedInEvent = new EventEmitter<boolean>()

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openDialog(){
    const dialogRef = this.dialog.open(LoginDialogComponent, {
      width: "50%",
      height: "75%"
    })

    dialogRef.afterClosed().subscribe(result => {
      if (result === true){
        this.loggedInEvent.emit(true)
      }
    })
  }
}


@Component({
    selector: 'login-dialog',
    templateUrl: 'login-dialog.component.html'
})
export class LoginDialogComponent{

  @Output() loggedInEvent = new EventEmitter();

  phone_number = new FormControl('');
  otp = new FormControl('');
  otp_sent = false;

  constructor(private loginService: LoginService,
    private _snackbar : MatSnackBar,
    public dialogRef: MatDialogRef<LoginDialogComponent>){}

  postNumber(phone_number: FormControl){
    this.loginService.requestOtp(phone_number.value).subscribe(response => {
      if (response['success'] === true){
        this.otp_sent = true
        this.phone_number.disable()
        this._snackbar.open(`OTP has been sent to ${phone_number.value}`, 'Close',{
          duration: 2500,
        })
      }
      else{
        this._snackbar.open('Unable To send Otp. Please retry Again.', 'close', {
          duration: 1500
        })
        phone_number.setValue('')
      }
    }, (error) => {
      console.log(error.error)
      let responseData = error.error // smd response from the server
      this._snackbar.open(responseData.data+ '. Please Retry', 'Close') //responseData.data = smd['data']
      phone_number.setValue('')
    })
  }

  postOtp(phone_number: FormControl, otp: FormControl){
    this.loginService.submitOtp(phone_number.value, Number(otp.value)).subscribe(response => {
      if (response['success'] === true){
        localStorage.setItem('token', response['data']['token'])
        this.dialogRef.close(true);
      }
      else{
        this._snackbar.open('Unable to Login, please try again', 'close',{
          duration: 2000
        })
      }
    }, (error) => {
      this._snackbar.open('Please Enter Otp Again', 'close', {
        duration: 2000
      })
      otp.setValue('')
    })
  }

}
