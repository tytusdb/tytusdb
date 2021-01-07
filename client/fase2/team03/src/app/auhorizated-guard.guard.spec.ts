import { TestBed, async, inject } from '@angular/core/testing';

import { AuhorizatedGuardGuard } from './auhorizated-guard.guard';

describe('AuhorizatedGuardGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AuhorizatedGuardGuard]
    });
  });

  it('should ...', inject([AuhorizatedGuardGuard], (guard: AuhorizatedGuardGuard) => {
    expect(guard).toBeTruthy();
  }));
});
