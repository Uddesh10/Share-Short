import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-view',
  templateUrl: './user-view.component.html',
  styleUrls: ['./user-view.component.css']
})
export class UserViewComponent {
  isChecked = true;
  inApp:boolean = false;
  constructor(private router:Router){
    this.inApp = this.router.url.includes('app') 
    console.log(this.inApp)
  }
  data:any = {
    profile:"https://img.freepik.com/free-photo/portrait-man-laughing_23-2148859448.jpg?size=338&ext=jpg&ga=GA1.1.735520172.1711324800&semt=ais",
    name:"Jhon Doe",
    about:"I'm a self-taught developer who is always learning and creating cool stuffs.",
    facebook:"facebook.com",
    instagram:"instagram.com",
    xTwitter:"x.com",
    threads:"threads.com",
    telegram:"telegram.com",
    youtube:"youtube.com",
    discord:"discord.com",
    github:"github.com",
    linkedin:"linkedin.com",
    snapchat:"snapchat.com",
    email:"email.com",
    whatsapp:"12345678900",
    extraLinks:[
      {
        label:"My newly launched product",
        iconKey:"amazon",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Buy Iphone from here",
        iconKey:"apple",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Deliver package here",
        iconKey:"box-seam",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Take off with cheaper flights",
        iconKey:"rocket-takeoff-fill",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
    {
        label:"My newly launched product",
        iconKey:"amazon",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Buy Iphone from here",
        iconKey:"apple",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Deliver package here",
        iconKey:"box-seam",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Take off with cheaper flights",
        iconKey:"rocket-takeoff-fill",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
    {
        label:"My newly launched product",
        iconKey:"amazon",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Buy Iphone from here",
        iconKey:"apple",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Deliver package here",
        iconKey:"box-seam",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
     {
        label:"Take off with cheaper flights",
        iconKey:"rocket-takeoff-fill",
        profile:"",
        link:"www.amazon.com",
        enabled:true
    },
    ],
    storeLinks:[
      {
        url:'www.amazon.com',
        title:'Amazon Product',
        productImage:"https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        price:'100',
        currency:'$'
      },
      {
        url:'www.flipkart.com',
        title:'Flipkart Product',
        productImage:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnU_iLA8a3fnI5yUGzelnh_XdLZzBUg4AcWEUEoooR2A&s",
        price:'100',
        currency:'$'
      },
      {
        url:'www.amazon.com',
        title:'Amazon Product',
        productImage:"https://jureursicphotography.com/wp-content/uploads/2020/10/2020_02_21_Sephora-Favurite-Box5247.jpg",
        price:'100',
        currency:'$'
      }
    ],
    design:{
      background:"https://visme.co/blog/wp-content/uploads/2017/07/50-Beautiful-and-Minimalist-Presentation-Backgrounds-018.jpg"
    }
  }
}
