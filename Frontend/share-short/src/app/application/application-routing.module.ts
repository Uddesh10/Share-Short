import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LinksComponent } from './links/links.component';
import { DesignComponent } from './design/design.component';
import { StoreComponent } from './store/store.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {path:'home' , children:[
    {path:'links' , component:LinksComponent},
    {path:'design' , component:DesignComponent},
    {path:'store' , component:StoreComponent}
  ] , component:HomeComponent}
  
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ApplicationRoutingModule { }
