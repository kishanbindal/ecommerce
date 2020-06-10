import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OpbuttonComponent } from './opbutton.component';

describe('OpbuttonComponent', () => {
  let component: OpbuttonComponent;
  let fixture: ComponentFixture<OpbuttonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OpbuttonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OpbuttonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
