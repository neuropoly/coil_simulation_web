'use strict';

describe('Service: getTools', function () {

  // load the service's module
  beforeEach(module('angularSeedApp'));

  // instantiate service
  var getTools;
  beforeEach(inject(function (_getTools_) {
    getTools = _getTools_;
  }));

  it('should do something', function () {
    expect(!!getTools).toBe(true);
  });

});
