'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:FileUploadCtrl
 * @description
 * # FileUploadCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
    .controller('FileUploadCtrl', ['$scope', 'Upload', '$timeout', 'SharedDataService', "$localStorage",
    function ($scope, Upload, $timeout, SharedDataService, $localStorage) {
      $scope.$storage = $localStorage;


      $scope.NewFile = SharedDataService; //Data shared between browserCntrl and updateCntrl

    //Watch if the user try to upload a file with the button or the drag and dropé
    $scope.$watch('files', function () {
        $scope.upload($scope.files);
    });
    $scope.$watch('file', function () {
        if ($scope.file != null) {
            $scope.upload([$scope.file]);
        }
    });

    $scope.log = '';
    $scope.upload = function (files) {
        if (files && files.length) { //If the files exists
            for (var i = 0; i < files.length; i++) { //Update each file one by one
                var file = files[i];
                Upload.upload({
                    url: '/upload', //The server address to receive files, it's can take .nii or .gz but decompress them automatically
                    fields: {
                        'username': $scope.$storage.uid //send the uid to put the file inside the right folder
                    },
                    file: file
                }).progress(function (evt) { //During the progression update a value in order to show a progressbar
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    $scope.log = 'progress: ' + progressPercentage + '% ' +
                                evt.config.file.name + '\n' + $scope.log;
                }).success(function (data, status, headers, config) { //If the request works
                    $timeout(function() { //Update the log
                        $scope.log = 'file: ' + config.file.name + ', Response: ' + JSON.stringify(data) + '\n' + $scope.log;
                    });
                    console.log(config.file.name);
                    $scope.NewFile.text = config.file.name;
                    $scope.NewFile.state = true; //This value say 'The user has updated  a new file'
                });
            }
        }
        $scope.NewFile.state = false;
    };
}]);
