import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeasurementErrorComponent } from './measurement-error.component';

describe('MeasurementErrorComponent', () => {
  let component: MeasurementErrorComponent;
  let fixture: ComponentFixture<MeasurementErrorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MeasurementErrorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MeasurementErrorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
