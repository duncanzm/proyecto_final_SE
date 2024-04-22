import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InvalidMonitorComponent } from './invalid-monitor.component';

describe('InvalidMonitorComponent', () => {
  let component: InvalidMonitorComponent;
  let fixture: ComponentFixture<InvalidMonitorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InvalidMonitorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InvalidMonitorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
