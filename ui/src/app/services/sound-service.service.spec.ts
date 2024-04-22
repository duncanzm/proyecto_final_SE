import { TestBed } from '@angular/core/testing';

import { SoundServiceService } from './sound-service.service';

describe('SoundServiceService', () => {
  let service: SoundServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SoundServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
