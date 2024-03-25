import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LinksComponent } from './links/links.component';
import { DesignComponent } from './design/design.component';
import { StoreComponent , AddProductDialog } from './store/store.component';
import { PreviewComponent } from './preview/preview.component';
import { ApplicationRoutingModule } from './application-routing.module';
import { HomeComponent } from './home/home.component';
import { SharedModule } from '../shared/shared.module';
import { DragDropModule } from '@angular/cdk/drag-drop';
import { MatTooltipModule } from "@angular/material/tooltip";
import { MatDialogModule } from "@angular/material/dialog";
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    LinksComponent,
    DesignComponent,
    StoreComponent,
    PreviewComponent,
    HomeComponent,
    AddProductDialog
  ],
  imports: [
    CommonModule,
    ApplicationRoutingModule,
    SharedModule,
    DragDropModule,
    MatTooltipModule,
    MatDialogModule,
    FormsModule
  ]
})
export class ApplicationModule { }
