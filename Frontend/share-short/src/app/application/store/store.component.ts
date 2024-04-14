import { Component } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';

@Component({
  selector: 'app-store',
  templateUrl: './store.component.html',
  styleUrls: ['./store.component.css']
})
export class StoreComponent {

  constructor(public dialog: MatDialog){}

  openDialog() {
    const dialogRef = this.dialog.open(AddProductDialog , {panelClass:'product-modal'});

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}

@Component({
  selector: 'add-product-ialog',
  templateUrl: './add-product.dialog.html',
  styleUrls:['./store.component.css']
})
export class AddProductDialog {
  
}
