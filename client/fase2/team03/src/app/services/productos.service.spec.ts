import { TestBed } from '@angular/core/testing';

import { ProductosService } from './productos.service';

describe('ProductosService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ProductosService = TestBed.get(ProductosService);
    expect(service).toBeTruthy();
  });
});
