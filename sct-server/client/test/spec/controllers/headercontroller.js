'use strict';

describe('Controller: HeadercontrollerCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var HeadercontrollerCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    HeadercontrollerCtrl = $controller('HeadercontrollerCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(HeadercontrollerCtrl.awesomeThings.length).toBe(3);
  });
});
