import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {path:'auth' , loadChildren:()=> import('./authentication/authentication.module').then(m => m.AuthenticationModule)},
  {path:'app' , loadChildren: ()=> import('./application/application.module').then(m => m.ApplicationModule)},
  {path:'**' , redirectTo:'auth/sign-in'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
