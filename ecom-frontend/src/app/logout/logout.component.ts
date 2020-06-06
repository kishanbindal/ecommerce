import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { LogoutService } from '../services/logout.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  @Output() logOutEvent = new EventEmitter<boolean>()

  constructor(private logoutService : LogoutService,
    private _snackbar : MatSnackBar) { }

  ngOnInit(): void {
  }

  logUserOut(){
  this.logoutService.sendLogout().subscribe(response => {
    if (response['success'] == true){
      localStorage.removeItem('token')
      this.logOutEvent.emit(true)
      this._snackbar.open('Successfully Logged Out', 'Close', {
        duration : 3000 
      })
    }
  })
  }

}
