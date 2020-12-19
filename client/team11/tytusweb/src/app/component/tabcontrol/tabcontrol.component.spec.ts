import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TabcontrolComponent } from './tabcontrol.component';

describe('TabcontrolComponent', () => {
  let component: TabcontrolComponent;
  let fixture: ComponentFixture<TabcontrolComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TabcontrolComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TabcontrolComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
