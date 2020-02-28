import { Component, OnInit } from '@angular/core';
import {watch_products} from '../watch_products'


@Component({
  selector: 'app-watch-list',
  templateUrl: './watch-list.component.html',
  styleUrls: ['./watch-list.component.css']
})
export class WatchListComponent implements OnInit {
 watch_products = watch_products;

  constructor() { }

  ngOnInit() {
  }

}
