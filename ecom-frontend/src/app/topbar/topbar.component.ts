import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrls: ['./topbar.component.css']
})
export class TopbarComponent implements OnInit {

  loggedInStatus = false;

  constructor() { 
    if (localStorage.getItem('token') != null){
      this.loggedInStatus = true
    }
  }

  ngOnInit(): void {

  }

  GetLogInStatus($event){
    console.log($event)
    if ($event === true){
      this.loggedInStatus = true
    }
  }

}
