import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletetableComponent } from './deletetable.component';

describe('DeletetableComponent', () => {
  let component: DeletetableComponent;
  let fixture: ComponentFixture<DeletetableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeletetableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeletetableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
