import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';

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

  private productSource = new BehaviorSubject('')
  
  constructor(private _http: HttpClient) {}

  getAllProducts(){
    const token = localStorage.getItem('token')
    console.log(`Token : ${token}`)
    let url = configUrl+'/api/products/'
    this._http.get(url).subscribe(response => {
      console.log(response)
    })
  }

}
