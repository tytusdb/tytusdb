import { TestBed } from '@angular/core/testing';

import { ServiceTreeService } from './service-tree.service';

describe('ServiceTreeService', () => {
  let service: ServiceTreeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServiceTreeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
