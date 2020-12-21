import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponenteNavbarComponent } from "./componente-navbar.component";

describe('ComponenteNavbarComponent', () => {
  let component: ComponenteNavbarComponent;
  let fixture: ComponentFixture<ComponenteNavbarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComponenteNavbarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ComponenteNavbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
