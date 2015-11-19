'use strict';

describe('Service: FileBrowser', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var FileBrowser;
  beforeEach(inject(function (_FileBrowser_) {
    FileBrowser = _FileBrowser_;
  }));

  it('should do something', function () {
    expect(!!FileBrowser).toBe(true);
  });

});
