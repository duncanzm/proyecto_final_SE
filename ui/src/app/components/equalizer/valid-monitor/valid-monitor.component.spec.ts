import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ValidMonitorComponent } from './valid-monitor.component';

describe('ValidMonitorComponent', () => {
  let component: ValidMonitorComponent;
  let fixture: ComponentFixture<ValidMonitorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ValidMonitorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ValidMonitorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
