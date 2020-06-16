import { Injectable } from '@angular/core';
import { BehaviorSubject, throwError, config } from 'rxjs';
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

  private productIdSource = new BehaviorSubject('No Product to Show');
  public productIdItem = this.productIdSource.asObservable();

  private orderItemSource = new BehaviorSubject('No Items Ordered');
  public orderedItems = this.orderItemSource.asObservable();

  private cartSource = new BehaviorSubject('Cart is Empty');
  public cartData = this.cartSource.asObservable();
  
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
      // console.log('DataService All Products Respone :')
      // console.log(response)
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

  getProductById(product_id){
    const token = localStorage.getItem('token')
    let url = configUrl+`/api/products/${product_id}`
    console.log('Product by ID url :' +url)
    this._http.get(url, {headers: {
      'token': token
    }}).pipe(
      catchError(this.handleError)
    )
    .subscribe(response => {
      // console.log(response)
      if (response['success'] === true){
        this.productIdSource.next(response['data'])
      }
    })
  }

  addProduct(data){
    const token = localStorage.getItem('token')
    let url = configUrl+"/api/products/"
    return this._http.post(url, data, {headers:{
      'token': token
    }})
    .pipe(
      catchError(this.handleError)
    )
  }

  deleteProduct(id){
    const token = localStorage.getItem('token')
    let url = configUrl+`/api/products/${id}/`
    return this._http.delete(url,{headers:{
      'token': token
    }})
    .pipe(
      catchError(this.handleError)
    )
  }

  updateProduct(data, product_id: number){
    const token = localStorage.getItem('token')
    let url = configUrl+`/api/products/${product_id}/`;
    return this._http.put(url, data, {
      headers:{
        'token': token
      }
    })
    .pipe(
      catchError(this.handleError)
    )
  }

  addOrderItem(data){
    const token = localStorage.getItem('token')
    let url = configUrl+'/api/order/'
    console.log(url)
    return this._http.post(url, data, {headers:{
      'token': token
    }})
    .pipe(
      catchError(this.handleError)
    )
  }

  getOrderItems(){
    const token = localStorage.getItem('token')
    let url = configUrl + "/api/order/"
    this._http.get(url, {headers: {
      'token': token
    }})
    .pipe(
      catchError(this.handleError)
    )
    .subscribe(response => {
      if (response['success'] == true){
        this.orderItemSource.next(response['data'])
      }
    })
  }

  updateOrderItem(order_id, data){
    const token = localStorage.getItem('token')
    let url = configUrl+`/api/order/${order_id}`;
    this._http.patch(url, data, {headers:{
      'token': token
    }})
    .pipe(
      catchError(this.handleError)
    )
    .subscribe(response => {
      console.log(response)
      if (response['success'] === true){
        this.getOrderItems()
      }
    })
  }

  deleteOrderItem(order_id){
    const token = localStorage.getItem('token')
    let url = configUrl + `/api/order/${order_id}`;
    return this._http.delete(url, {headers: {
      'token': token
    }})
  }

  getCart(){
    const token = localStorage.getItem('token')
    let url = configUrl+'/api/cart/'
    this._http.get(url, { headers :{
      'token': token
    }})
    .pipe(
      catchError(this.handleError)
    )
    .subscribe(response => {
      if (response['success'] === true){
        this.cartSource.next(response['data'])
      }
    })
  }

}
