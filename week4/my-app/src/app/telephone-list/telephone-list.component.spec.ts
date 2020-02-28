import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TelephoneListComponent } from './telephone-list.component';

describe('TelephoneListComponent', () => {
  let component: TelephoneListComponent;
  let fixture: ComponentFixture<TelephoneListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TelephoneListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TelephoneListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
