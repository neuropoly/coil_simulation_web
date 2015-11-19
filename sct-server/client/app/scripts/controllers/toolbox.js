/**
 * Created by willispinaud on 17/08/2015.
 */
'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:ToolboxCtrl
 * @description
 * # ToolboxCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('ToolboxCtrl', ['$scope', '$modal', function ($scope, $modal) {

    $scope.console = function () {
      //Call a new modal with the toolbox
      var modalInstance = $modal.open({
        animation: true,
        templateUrl: '../views/console.html',
        controller: 'ConsoleCtrl',
        size:'xl'
      });
    };

  }]);
