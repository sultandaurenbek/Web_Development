import { Component, OnInit } from '@angular/core';
import { ProductsService } from '../products.service';

@Component({
  selector: 'app-telephone-list',
  templateUrl: './telephone-list.component.html',
  styleUrls: ['./telephone-list.component.css']
})




export class TelephoneListComponent implements OnInit {
  categoriesWithProducts: any;

  getProducts(){
    this.productsService.getProductsList().subscribe(products => this.categoriesWithProducts = products)
  }

  constructor() { }

  ngOnInit() {
  }

}

