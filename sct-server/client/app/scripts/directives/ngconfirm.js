'use strict';

/**
 * @ngdoc directive
 * @name angularSeedApp.directive:ngConfirm
 * @description
 * # A generic confirmation for risky actions.
 * # Usage: Add attributes: ng-really-message="Are you sure"? ng-really-click="takeAction()" function
 */
angular.module('angularSeedApp')
  .directive('ngConfirm', function () {
    return {
      restrict: 'A',
      link: function(scope, element, attrs) {
        element.bind('click', function() {
          var message = attrs.ngConfirmMessage;
          if (message && confirm(message)) {
            scope.$apply(attrs.ngConfirm);
          }
        });
      }
    };
  });
