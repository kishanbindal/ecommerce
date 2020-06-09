import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletebuttonComponent } from './deletebutton.component';

describe('DeletebuttonComponent', () => {
  let component: DeletebuttonComponent;
  let fixture: ComponentFixture<DeletebuttonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeletebuttonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeletebuttonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
