import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { RouterModule } from '@angular/router';
import { UserViewComponent } from './user-view/user-view.component';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
        HeaderComponent,
        UserViewComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule
  ],
  exports:[HeaderComponent,UserViewComponent]
})
export class SharedModule { }
