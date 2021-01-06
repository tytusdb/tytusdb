import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BotongetComponent } from './botonget.component';

describe('BotongetComponent', () => {
  let component: BotongetComponent;
  let fixture: ComponentFixture<BotongetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BotongetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BotongetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
