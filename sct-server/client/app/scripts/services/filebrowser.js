'use strict';

/**
 * @ngdoc service
 * @name angularSeedApp.FileBrowser
 * @description
 * # FileBrowser
 * Service in the angularSeedApp.
 */
angular.module('angularSeedApp')
  .service('FileBrowser', ['$modal', function ($modal) {

    var animationsEnabled = true;

    var open = function () {

      var modalInstance = $modal.open({
        animation: animationsEnabled,
        templateUrl: '../views/browser.html',
        controller: 'BrowserCtrl',
      });

      modalInstance.result.then(
      );
    };

    return open();



    var modalInstance = {
      FirstName: ''
    };

    return {
      getFirstName: function () {
        return data.FirstName;
      },
      setFirstName: function (firstName) {
        data.FirstName = firstName;
      }
    };


  }]);
