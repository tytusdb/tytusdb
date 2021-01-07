import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RenametableComponent } from './renametable.component';

describe('RenametableComponent', () => {
  let component: RenametableComponent;
  let fixture: ComponentFixture<RenametableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RenametableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RenametableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
