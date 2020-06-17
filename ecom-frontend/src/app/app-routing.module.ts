import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductgridComponent } from './productgrid/productgrid.component';
import { SingleproductComponent } from './singleproduct/singleproduct.component';
import { AdminpageComponent } from './adminpage/adminpage.component';
import { CheckoutpageComponent } from './checkoutpage/checkoutpage.component';


const routes: Routes = [
  {path:'', component: ProductgridComponent},
  {path: 'products/:name', component: SingleproductComponent},
  {path: 'admin', component: AdminpageComponent},
  {path: 'checkout', component: CheckoutpageComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
