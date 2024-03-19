import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LinksComponent } from './links/links.component';
import { DesignComponent } from './design/design.component';
import { StoreComponent } from './store/store.component';
import { PreviewComponent } from './preview/preview.component';
import { ApplicationRoutingModule } from './application-routing.module';



@NgModule({
  declarations: [
    LinksComponent,
    DesignComponent,
    StoreComponent,
    PreviewComponent
  ],
  imports: [
    CommonModule,
    ApplicationRoutingModule
  ]
})
export class ApplicationModule { }
