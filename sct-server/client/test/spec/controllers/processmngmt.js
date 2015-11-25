'use strict';

describe('Controller: ProcessmngmtCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var ProcessmngmtCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ProcessmngmtCtrl = $controller('ProcessmngmtCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ProcessmngmtCtrl.awesomeThings.length).toBe(3);
  });
});
