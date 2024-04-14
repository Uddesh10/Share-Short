import { Component } from '@angular/core';
import {CdkDragDrop, moveItemInArray} from '@angular/cdk/drag-drop';
import { Router } from '@angular/router';
@Component({
  selector: 'app-links',
  templateUrl: './links.component.html',
  styleUrls: ['./links.component.css']
})
export class LinksComponent {
 extraLink = [
    {
      lable:"Amazon",
      iconKey:"envelope-arrow-down",
      profile:"",
      link:"www.amazon.com"
    },
    {
      lable:"Flipkart",
      iconKey:"envelope-arrow-down",
      profile:"",
      link:"www.flipkart.com"
    }
  ];

  drop(event: CdkDragDrop<any[]>) {
    moveItemInArray(this.extraLink, event.previousIndex, event.currentIndex);
  }

  openBootstrapIcon(){
     window.open("https://icons.getbootstrap.com/", "_blank");
  }
}
