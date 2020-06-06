import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductgridComponent } from './productgrid/productgrid.component';
import { SingleproductComponent } from './singleproduct/singleproduct.component';


const routes: Routes = [
  {path:'', component: ProductgridComponent},
  {path: 'products/:name', component: SingleproductComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
