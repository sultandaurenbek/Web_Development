import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FilmsdetailsComponent } from './filmsdetails.component';

describe('FilmsdetailsComponent', () => {
  let component: FilmsdetailsComponent;
  let fixture: ComponentFixture<FilmsdetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FilmsdetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FilmsdetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
