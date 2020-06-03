import { Injectable } from '@angular/core';
import { BehaviorSubject, throwError } from 'rxjs';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { MatSnackBar } from '@angular/material/snack-bar';

const configUrl = 'http://127.0.0.1:8000'

export interface Product{
  name: string,
  images : string,
  quantity: number,
  price: number
}

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private productSource = new BehaviorSubject('');
  public productsList = this.productSource.asObservable();
  
  constructor(private _http: HttpClient, private _snackbar: MatSnackBar) {}

  handleError(error: HttpErrorResponse){
    console.log('An Error Occured :' +error)
    return throwError(error)
  }

  getAllProducts(){
    const token = localStorage.getItem('token')
    console.log(`Token : ${token}`)
    let url = configUrl+'/api/products/'
    this._http.get(url)
    .pipe(
      catchError(this.handleError)
    )
    .subscribe(response => {
      console.log('DataService All Products Respone :')
      console.log(response)
      if (response['success'] === true){
        this.productSource.next(response['data'])
      }
      else{
        this._snackbar.open('Unable to retrieve data from server', 'close', {
          duration: 1500,
        })
      }
    })
  }

}
