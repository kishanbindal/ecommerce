import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LogoutService {

  confUrl = 'http://127.0.0.1:8000'
  constructor(private _http: HttpClient) { }

  // Send Logout Request to Logout Api endpoint. Rest of the view functionality handled in component. 
  sendLogout(){
    let token = localStorage.getItem('token');
    let url = this.confUrl+'/api/logout';
    console.log('Logout Url :' + url)
    return this._http.post(url, null,{headers:{
      'token': token,
    }})
  }
}
