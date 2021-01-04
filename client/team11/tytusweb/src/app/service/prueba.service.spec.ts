import { TestBed } from '@angular/core/testing';

import { PruebaService } from './prueba.service';

describe('PruebaService', () => {
  let service: PruebaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PruebaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
