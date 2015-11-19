'use strict';

describe('Controller: ArgumentsCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var ArgumentsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ArgumentsCtrl = $controller('ArgumentsCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ArgumentsCtrl.awesomeThings.length).toBe(3);
  });
});
