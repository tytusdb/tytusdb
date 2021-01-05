import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewdatabaseComponent } from './newdatabase.component';

describe('NewdatabaseComponent', () => {
  let component: NewdatabaseComponent;
  let fixture: ComponentFixture<NewdatabaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewdatabaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewdatabaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
