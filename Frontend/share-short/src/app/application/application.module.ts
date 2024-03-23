import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LinksComponent } from './links/links.component';
import { DesignComponent } from './design/design.component';
import { StoreComponent } from './store/store.component';
import { PreviewComponent } from './preview/preview.component';
import { ApplicationRoutingModule } from './application-routing.module';
import { HomeComponent } from './home/home.component';
import { SharedModule } from '../shared/shared.module';
import { DragDropModule } from '@angular/cdk/drag-drop';



@NgModule({
  declarations: [
    LinksComponent,
    DesignComponent,
    StoreComponent,
    PreviewComponent,
    HomeComponent,
  ],
  imports: [
    CommonModule,
    ApplicationRoutingModule,
    SharedModule,
    DragDropModule
  ]
})
export class ApplicationModule { }
