import { Component, OnInit } from '@angular/core';

import { headphone_products } from '../headphone_products';

@Component({
  selector: 'app-headphone-list',
  templateUrl: './headphone-list.component.html',
  styleUrls: ['./headphone-list.component.css']
})
export class HeadphoneListComponent implements OnInit {
  headphone_products = headphone_products;

  constructor() { }

  ngOnInit() {
  }

}
