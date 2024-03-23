import { Component } from '@angular/core';
import {CdkDragDrop, moveItemInArray} from '@angular/cdk/drag-drop';
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

  drop(event: CdkDragDrop<string[]>) {
    moveItemInArray(this.extraLink, event.previousIndex, event.currentIndex);
  }
}
