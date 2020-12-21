import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RenamedatabaseComponent } from './renamedatabase.component';

describe('RenamedatabaseComponent', () => {
  let component: RenamedatabaseComponent;
  let fixture: ComponentFixture<RenamedatabaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RenamedatabaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RenamedatabaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
