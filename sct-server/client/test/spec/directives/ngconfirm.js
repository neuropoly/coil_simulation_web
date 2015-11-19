'use strict';

describe('Directive: ngConfirm', function () {

  // load the directive's module
  beforeEach(module('angularSeedApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<ng-confirm></ng-confirm>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the ngConfirm directive');
  }));
});
