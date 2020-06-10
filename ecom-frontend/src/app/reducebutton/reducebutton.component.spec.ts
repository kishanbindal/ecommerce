import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReducebuttonComponent } from './reducebutton.component';

describe('ReducebuttonComponent', () => {
  let component: ReducebuttonComponent;
  let fixture: ComponentFixture<ReducebuttonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReducebuttonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReducebuttonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
