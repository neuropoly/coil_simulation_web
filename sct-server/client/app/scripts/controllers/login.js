'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('LoginCtrl', ["$scope", "$localStorage", "$http", "$window",
    function($scope, $localStorage, $http, $window) {
      $scope.$storage = $localStorage;

      /*
      * Idées pour le login/register/logout
      *
      * 1) register avec un POST qui va ajouter une entrée utilisateur dans la base de donnée.
      * login avec un get qui va vérifier user/clé cryptée et si la réponse est ok alors écrire dans le local storage
      * sinon renvoie une erreur et log l'ip avec le nombre d'essais dans la base de donnée?
      * logout supprimer la variable dans le localstorage
      * Recuperer le password -> mail à l'admin ou envoi d'un mail avec lien et token unique
      *
      * 2) ajouter un envoie de mail pour valider le compte lorsque l'étape d'enregistrement est terminée
      *
      * 3)..sinon personae ?
      * */

      /*var auth = Auth;
      $scope.auth = Auth;
      var ref = new Firebase("https://isct.firebaseio.com");


      // any time auth status updates, add the user data to scope
      auth.$onAuth(function(authData) {
        $scope.authData = authData;
        $scope.$storage.uid = authData.uid.split(':')[1];
        $scope.$storage.name = authData.password.email.replace(/@.*!/, '');

      });*/

      $scope.logout = function(){
        //Auth.$unauth();
        $scope.$storage.uid = null;
        $scope.$storage.name = null;
      };


      $scope.loginSchema = {
        "type": "object",
        "title": "Comment",
        "properties": {
          "pass": {
            "title": "Password",
            "type": "string",
            "pattern": "^[a-zA-Z0-9]*$",
            "minLength":"5",
            "maxLength":"18"
          },
          "email": {
            "title": "Email",
            "type": "string",
            "pattern": "^\\S+@\\S+$",
            "validationMessage": "Please enter your email address."
          }
        },
        "required": [
          "pass",
          "email"
        ]
      };

      $scope.loginForm = [
        {
          "type": "help",
          "helpvalue": "<div class=\"alert alert-warning\">Login into your account.</div>"
        },
        {
          "key": "email"
        },
        {
          "key": "pass",
          "type":"password"
        },
        {
          "type": "submit",
          "style": "btn-info",
          "title": "OK",
          "icon": 'glyphicon glyphicon-icon-exclamation-sign'
        }
      ];

      $scope.loginModel = {};

      $scope.onSubmit = function(form) {
        // First we broadcast an event so all fields validate themselves
        $scope.$broadcast('schemaFormValidate');

        // Then we check if the form is valid
        if (form.$valid) {
          //function to send infos with http.post
          $http.post('/login', {email:$scope.loginModel.email, password:$scope.loginModel.pass}).
            then(function(response) {
              if (response.data.ok){
                $scope.$storage.uid=response.data.uid;
                $scope.$storage.name = $scope.loginModel.email.replace(/@.*!/, '');
                $window.location.href = '#/toolbox'
              }
              else{
                $scope.$storage.uid=null; //to be sure
                $scope.error = response.data.error; //display error message
              }
            });
        }
      };

    }
  ]);
