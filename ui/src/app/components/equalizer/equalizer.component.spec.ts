import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EqualizerComponent } from './equalizer.component';

describe('EqualizerComponent', () => {
  let component: EqualizerComponent;
  let fixture: ComponentFixture<EqualizerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EqualizerComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EqualizerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
