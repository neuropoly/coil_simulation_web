'use strict';

describe('Controller: CallfilebrowserCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var CallfilebrowserCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    CallfilebrowserCtrl = $controller('CallfilebrowserCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(CallfilebrowserCtrl.awesomeThings.length).toBe(3);
  });
});
