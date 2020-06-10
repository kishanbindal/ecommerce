import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddbuttonComponent } from './addbutton.component';

describe('AddbuttonComponent', () => {
  let component: AddbuttonComponent;
  let fixture: ComponentFixture<AddbuttonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddbuttonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddbuttonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
