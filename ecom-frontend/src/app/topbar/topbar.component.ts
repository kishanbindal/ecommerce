import { Component, OnInit, OnChanges, SimpleChange, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrls: ['./topbar.component.css']
})
export class TopbarComponent implements OnInit, OnChanges {

  loggedInStatus = false;
  adminCheck = false;

  constructor() { 
    if (localStorage.getItem('token') != null){
      this.loggedInStatus = true
    }
  }

  ngOnInit(): void {
    setTimeout(()=> {this.adminCheck = this.isAdmin()}, 500)
  }

  ngOnChanges(changes : SimpleChanges): void{
    // this.adminCheck = this.isAdmin()
  }

  GetLogInStatus($event){
    if ($event === true){
      this.loggedInStatus = true
      this.adminCheck = this.isAdmin()
    }
  }

  GetLoggedOutStatus($event){
    if ($event === true){
      this.loggedInStatus = false
      this.adminCheck = false
    }
  }

  isAdmin(): boolean{
    let token = localStorage.getItem('token')
    var token_payload_section = JSON.stringify(token).split('.')[1]
    let payload = JSON.parse(atob(token_payload_section))
    // console.log(payload)
    if (payload['role'] === 'admin'){
      return true
    }
    return false
  }

}
