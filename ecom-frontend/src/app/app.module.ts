//Angular Imports
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule, FormsModule} from '@angular/forms'

// Component imports 
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TopbarComponent } from './topbar/topbar.component';
import { LoginComponent, LoginDialogComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { ProductcardComponent } from './productcard/productcard.component';
import { ProductgridComponent } from './productgrid/productgrid.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

// Angular Material Imports
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule, MatCard } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatInputModule} from '@angular/material/input';
import { MatGridListModule } from '@angular/material/grid-list'
import { MatSnackBarModule } from '@angular/material/snack-bar'
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatMenuModule } from '@angular/material/menu';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';

//Services Imports
import { DataService } from './services/data-service.service';
import { LoginService } from './services/login-service.service';
import { LogoutService } from './services/logout.service';
import { SingleproductComponent } from './singleproduct/singleproduct.component';
import { AdminComponent } from './admin/admin.component';
import { AdminpageComponent } from './adminpage/adminpage.component';
import { AddproductComponent, AddproductDialogComponent } from './addproduct/addproduct.component';
import { DeletebuttonComponent } from './deletebutton/deletebutton.component';
import { UpdateproductComponent, UpdateProductDialogComponent } from './updateproduct/updateproduct.component';
import { OpbuttonComponent } from './opbutton/opbutton.component';
import { AddbuttonComponent } from './addbutton/addbutton.component';
import { ReducebuttonComponent } from './reducebutton/reducebutton.component';
import { AddtocartComponent } from './addtocart/addtocart.component';
import { CartbuttonComponent, CartbuttonDialogComponent } from './cartbutton/cartbutton.component';
import { CheckoutpageComponent } from './checkoutpage/checkoutpage.component';
import { MAT_FORM_FIELD_DEFAULT_OPTIONS } from '@angular/material/form-field';

@NgModule({
  declarations: [
    AppComponent,
    TopbarComponent,
    LoginComponent,
    LoginDialogComponent,
    LogoutComponent,
    ProductgridComponent,
    ProductcardComponent,
    SingleproductComponent,
    AdminComponent,
    AdminpageComponent,
    AddproductComponent,
    AddproductDialogComponent,
    DeletebuttonComponent,
    UpdateproductComponent,
    UpdateProductDialogComponent,
    OpbuttonComponent,
    AddbuttonComponent,
    ReducebuttonComponent,
    AddtocartComponent,
    CartbuttonComponent,
    CartbuttonDialogComponent,
    CheckoutpageComponent,
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    MatInputModule,
    MatGridListModule,
    MatMenuModule,
    MatListModule,
    MatSnackBarModule,
    MatToolbarModule,
    MatIconModule,
    ReactiveFormsModule,
  ],
  providers: [
    DataService,
    LoginService,
    LogoutService,
    { provide: MAT_FORM_FIELD_DEFAULT_OPTIONS, useValue: { color: 'primary' } },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
