import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletedatabaseComponent } from './deletedatabase.component';

describe('DeletedatabaseComponent', () => {
  let component: DeletedatabaseComponent;
  let fixture: ComponentFixture<DeletedatabaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeletedatabaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeletedatabaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
