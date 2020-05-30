import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, BehaviorSubject, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators'
import { MatSnackBar } from '@angular/material/snack-bar';

const configUrl = 'http://127.0.0.1:8000'

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private _http: HttpClient) { }

  // Gets Otp from login api endpoint
  requestOtp(phone_number){
    let data = {'phone_number': phone_number}
    let url = configUrl+'/api/login'
    return this._http.post(url, data)
    .pipe(
      catchError(this.handleError)
    )
  }

  //Submits Otp to the login-submit API endpoint
  submitOtp(phone_number, otp){
    let data = {
      'phone_number' : phone_number,
      'otp': otp 
    }
    console.log(`Data : ${data}`)
    const url = configUrl+'/api/login-submit'
    return this._http.post(url, data)
    .pipe(
      catchError(this.handleError)
    )
  }

  handleError(error : HttpErrorResponse){
    console.log('An Error occured, In handleError')
    return throwError(error)
  }
}
