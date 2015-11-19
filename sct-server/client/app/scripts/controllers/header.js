'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('HeaderCtrl', function ($scope,$localStorage,$http) {

    $scope.$storage = $localStorage;   //Initialization of the local storage

    $scope.logout = function(){
      $scope.$storage.uid = null;
      $http.get('/logout');
    };

    $scope.$watch('$storage.uid', function () {

      console.log($scope.$storage.uid);

      if ($scope.$storage.uid===null){
          $scope.logout_class = "hidden";
          $scope.login_class = "";
      }
      else{
        $scope.logout_class = "";
        $scope.login_class = "hidden";
      }

    });

  });
