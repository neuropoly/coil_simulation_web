'use strict';

describe('Controller: ToolsCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var ToolsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ToolsCtrl = $controller('ToolsCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ToolsCtrl.awesomeThings.length).toBe(3);
  });
});
