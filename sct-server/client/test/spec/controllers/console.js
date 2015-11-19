'use strict';

describe('Controller: ConsoleCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var ConsoleCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ConsoleCtrl = $controller('ConsoleCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ConsoleCtrl.awesomeThings.length).toBe(3);
  });
});
