'use strict';

describe('Service: FetchFileFactory', function () {

  // load the service's module
  beforeEach(module('angularSeedApp'));

  // instantiate service
  var FetchFileFactory;
  beforeEach(inject(function (_FetchFileFactory_) {
    FetchFileFactory = _FetchFileFactory_;
  }));

  it('should do something', function () {
    expect(!!FetchFileFactory).toBe(true);
  });

});
