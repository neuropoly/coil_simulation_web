'use strict';

/**
 * @ngdoc service
 * @name angularSeedApp.FilesTree
 * @description
 * # FilesTree
 * Service in the angularSeedApp.
 */
/*

if ($scope.$storage.uid === null){
        $scope.tree_path = "/tree/"+"You have to be logged to use this functionality";
      }
      else{
        $scope.tree_path = "/tree";  //The path to GET the tree

      }
*/


angular.module('angularSeedApp')
  .factory('FilesTree', function($resource){
    return $resource('/tree');
})

  .service('FilesTreeService', function ($rootScope, FilesTree) {
  var filesTree = [];
  this.getFilesTree = function() {
    filesTree = FilesTree.query();
    return filesTree;
  };
});