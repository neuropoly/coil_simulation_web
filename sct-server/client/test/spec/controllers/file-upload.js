'use strict';

describe('Controller: FileUploadCtrl', function () {

  // load the controller's module
  beforeEach(module('angularSeedApp'));

  var FileUploadCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    FileUploadCtrl = $controller('FileUploadCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(FileUploadCtrl.awesomeThings.length).toBe(3);
  });
});
