'use strict';

describe('Service: SharedDataService', function () {

  // load the service's module
  beforeEach(module('angularSeedApp'));

  // instantiate service
  var SharedDataService;
  beforeEach(inject(function (_SharedDataService_) {
    SharedDataService = _SharedDataService_;
  }));

  it('should do something', function () {
    expect(!!SharedDataService).toBe(true);
  });

});
