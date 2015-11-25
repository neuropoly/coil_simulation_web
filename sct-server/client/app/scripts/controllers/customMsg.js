'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:customMsgCtrl
 * @description
 * # customMsgCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('customMsgCtrl', ["$rootScope","$scope", "$routeParams", "$route",
    function($rootScope,$scope, $routeParams, $route) {
        $scope.custom_title = $routeParams.title;
        $scope.custom_msg = $routeParams.msg;
    }
  ]);
