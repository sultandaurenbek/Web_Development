import { Component, OnInit } from '@angular/core';
import {tablet_products} from '../tablet_products'

@Component({
  selector: 'app-tablet-list',
  templateUrl: './tablet-list.component.html',
  styleUrls: ['./tablet-list.component.css']
})
export class TabletListComponent implements OnInit {
 tablet_products = tablet_products;

  constructor() { }

  ngOnInit() {
  }

}
