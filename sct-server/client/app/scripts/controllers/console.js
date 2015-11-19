'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:ConsoleCtrl
 * @description
 * # ConsoleCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('ConsoleCtrl', function ($scope, $http, $interval, $localStorage) {

    $scope.$storage = $localStorage;   //Initialization of the local storage

    var log = "";
    $scope.log = ". . : : Welcome on the iSCT logger : : . .\n\n\n";

    var old_log = "";

    var getLog = function(){$http.get('/logger?uid='+$scope.$storage.uid).
      then(function(response) {
        // this callback will be called asynchronously
        // when the response is available
        if (response.data!=""){
          log = response.data;
          $scope.log = $scope.log + log;}
      }, function(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        if (response.data!=""){
          log = 'Communication error with the server: HTTP status='+response.status+"\n";
            if (log===old_log){
              log="";
            }
          old_log = 'Communication error with the server: HTTP status='+response.status+"\n";
          $scope.log = $scope.log + log;}
      })};


    // store the interval promise in this variable
    var promise;

    // starts the interval
    $scope.start = function() {
      // stops any running interval to avoid two intervals running at the same time
      $scope.stop();

      // store the interval promise
      promise = $interval(getLog, 500);
    };

    // stops the interval
    $scope.stop = function() {
      $interval.cancel(promise);
    };

    // starting the interval by default
    $scope.start();

    // stops the interval when the scope is destroyed,
    $scope.$on('$destroy', function() {
      $scope.stop();
    });

    var init = function(){$http.get('/logger?old=1&uid='+$scope.$storage.uid).
      then(function(response) {
        // this callback will be called asynchronously
        // when the response is available
        if (response.data!=""){
          log = response.data;
          $scope.log = $scope.log + log;}
      }, function(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        if (response.data!=""){
          log = 'Communication error with the server: HTTP status='+response.status+"\n";
          $scope.log = $scope.log + log;}
      })};
    init();

  });
