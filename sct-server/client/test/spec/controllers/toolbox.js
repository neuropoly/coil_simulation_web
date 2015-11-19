'use strict';

describe('Controller: ToolboxCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var ToolboxCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ToolboxCtrl = $controller('ToolboxCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ToolboxCtrl.awesomeThings.length).toBe(3);
  });
});
