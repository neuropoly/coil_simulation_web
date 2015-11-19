'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:RegisterCtrl
 * @description
 * # RegisterCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('RegisterCtrl', function ($scope, $http, $location, $localStorage, $window) {
    $scope.$storage = $localStorage;

    $scope.registerSchema = {
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
          "description": "Email will be used as username.",
          "validationMessage": "Please enter your email address."
        },
        "center": {
          "title": "Indicate your research center",
          "type": "string",
          "default": ""
        },
        "occupations": {
          "title": "Your occupation",
          "type": "string",
          "enum": [
            "Student",
            "Postdoc",
            "Researcher",
            "Clinician",
            "Other"
          ]
        },
        "country": {
          "title": "Your country",
          "type": "string",
          "enum": $scope.countries
        }
      },
      "required": [
        "pass",
        "email",
        "occupations",
        "country"
      ]
    };

    $scope.registerForm = [
      {
        "type": "help",
        "helpvalue": "<div class=\"alert alert-info\">Create your new account on iSCT</div>"
      },
      {
        "type": "section",
        "htmlClass": "row",
        "items": [
          {
            "type": "section",
            "htmlClass": "col-xs-6",
            "items": [
              "email"
            ]
          },
          {
            "type": "section",
            "htmlClass": "col-xs-6",
            "items": [
              {
                "key": "pass",
                "type": "password"
              }
            ]
          }
        ]
      },
      {
        "key": "occupations"
      },
      {
        "key": "center",
        "placeholder": "Your beloved research center"
      },
      {
        "key": "country"
      },
      {
        "type": "submit",
        "style": "btn-info",
        "title": "Register",
        "icon": 'glyphicon glyphicon-icon-exclamation-sign'
      }
    ];

    $scope.registerModel = {};

    $scope.onSubmit = function(form) {
      // First we broadcast an event so all fields validate themselves
      $scope.$broadcast('schemaFormValidate');

      // Then we check if the form is valid
      if (form.$valid) {
        //Function to send infos with http.post
        $http.post('/register', {email:$scope.registerModel.email, password:$scope.registerModel.pass, country:$scope.registerModel.country, occupation:$scope.registerModel.occupations, research_center:$scope.registerModel.center}).
          then(function(response) {
            if (response.data.ok){
              console.log(response.data.ok);
              $window.location.href = "/#/cmsg/Confirm%20your%20account/Wonderful,%20You%20are%20registered.%20Last%20step,%20you%20have%20to%20confirm%20your%20account%20with%20the%20link%20sent%20in%20your%20mailbox.";
            }
            else{
              clicked_on_register(false);
              $scope.$storage.uid=null; //to be sure
              $scope.error = response.data.error;
            }

          });
      }
    };

    $scope.clicked = false;
    var clicked_on_register = function(bool){
      $scope.clicked=bool;
    };


    $scope.countries = ['Canada',
      'United States',
      'United Kingdom',
      'France',
      'Afghanistan',
      'Åland Islands',
      'Albania',
      'Algeria',
      'American Samoa',
      'Andorra',
      'Angola',
      'Anguilla',
      'Antarctica',
      'Antigua and Barbuda',
      'Argentina',
      'Armenia',
      'Aruba',
      'Australia',
      'Austria',
      'Azerbaijan',
      'Bahamas',
      'Bahrain',
      'Bangladesh',
      'Barbados',
      'Belarus',
      'Belgium',
      'Belize',
      'Benin',
      'Bermuda',
      'Bhutan',
      'Bolivia',
      'Bosnia and Herzegovina',
      'Botswana',
      'Bouvet Island',
      'Brazil',
      'British Indian Ocean Territory',
      'Brunei Darussalam',
      'Bulgaria',
      'Burkina Faso',
      'Burundi',
      'Cambodia',
      'Cameroon',
      'Cape Verde',
      'Cayman Islands',
      'Central African Republic',
      'Chad',
      'Chile',
      'China',
      'Christmas Island',
      'Cocos (Keeling) Islands',
      'Colombia',
      'Comoros',
      'Congo',
      'Congo, The Democratic Republic of the',
      'Cook Islands',
      'Costa Rica',
      'Cote D\'Ivoire',
      'Croatia',
      'Cuba',
      'Cyprus',
      'Czech Republic',
      'Denmark',
      'Djibouti',
      'Dominica',
      'Dominican Republic',
      'Ecuador',
      'Egypt',
      'El Salvador',
      'Equatorial Guinea',
      'Eritrea',
      'Estonia',
      'Ethiopia',
      'Falkland Islands (Malvinas)',
      'Faroe Islands',
      'Fiji',
      'Finland',
      'French Guiana',
      'French Polynesia',
      'French Southern Territories',
      'Gabon',
      'Gambia',
      'Georgia',
      'Germany',
      'Ghana',
      'Gibraltar',
      'Greece',
      'Greenland',
      'Grenada',
      'Guadeloupe',
      'Guam',
      'Guatemala',
      'Guernsey',
      'Guinea',
      'Guinea-Bissau',
      'Guyana',
      'Haiti',
      'Heard Island and Mcdonald Islands',
      'Holy See (Vatican City State)',
      'Honduras',
      'Hong Kong',
      'Hungary',
      'Iceland',
      'India',
      'Indonesia',
      'Iran, Islamic Republic Of',
      'Iraq',
      'Ireland',
      'Isle of Man',
      'Israel',
      'Italy',
      'Jamaica',
      'Japan',
      'Jersey',
      'Jordan',
      'Kazakhstan',
      'Kenya',
      'Kiribati',
      'Korea, Democratic People\'s Republic of',
      'Korea, Republic of',
      'Kuwait',
      'Kyrgyzstan',
      'Lao People\'s Democratic Republic',
      'Latvia',
      'Lebanon',
      'Lesotho',
      'Liberia',
      'Libyan Arab Jamahiriya',
      'Liechtenstein',
      'Lithuania',
      'Luxembourg',
      'Macao',
      'Macedonia, The Former Yugoslav Republic of',
      'Madagascar',
      'Malawi',
      'Malaysia',
      'Maldives',
      'Mali',
      'Malta',
      'Marshall Islands',
      'Martinique',
      'Mauritania',
      'Mauritius',
      'Mayotte',
      'Mexico',
      'Micronesia, Federated States of',
      'Moldova, Republic of',
      'Monaco',
      'Mongolia',
      'Montserrat',
      'Morocco',
      'Mozambique',
      'Myanmar',
      'Namibia',
      'Nauru',
      'Nepal',
      'Netherlands',
      'Netherlands Antilles',
      'New Caledonia',
      'New Zealand',
      'Nicaragua',
      'Niger',
      'Nigeria',
      'Niue',
      'Norfolk Island',
      'Northern Mariana Islands',
      'Norway',
      'Oman',
      'Pakistan',
      'Palau',
      'Palestinian Territory, Occupied',
      'Panama',
      'Papua New Guinea',
      'Paraguay',
      'Peru',
      'Philippines',
      'Pitcairn',
      'Poland',
      'Portugal',
      'Puerto Rico',
      'Qatar',
      'Reunion',
      'Romania',
      'Russian Federation',
      'Rwanda',
      'Saint Helena',
      'Saint Kitts and Nevis',
      'Saint Lucia',
      'Saint Pierre and Miquelon',
      'Saint Vincent and the Grenadines',
      'Samoa',
      'San Marino',
      'Sao Tome and Principe',
      'Saudi Arabia',
      'Senegal',
      'Serbia and Montenegro',
      'Seychelles',
      'Sierra Leone',
      'Singapore',
      'Slovakia',
      'Slovenia',
      'Solomon Islands',
      'Somalia',
      'South Africa',
      'South Georgia and the South Sandwich Islands',
      'Spain',
      'Sri Lanka',
      'Sudan',
      'Suriname',
      'Svalbard and Jan Mayen',
      'Swaziland',
      'Sweden',
      'Switzerland',
      'Syrian Arab Republic',
      'Taiwan, Province of China',
      'Tajikistan',
      'Tanzania, United Republic of',
      'Thailand',
      'Timor-Leste',
      'Togo',
      'Tokelau',
      'Tonga',
      'Trinidad and Tobago',
      'Tunisia',
      'Turkey',
      'Turkmenistan',
      'Turks and Caicos Islands',
      'Tuvalu',
      'Uganda',
      'Ukraine',
      'United Arab Emirates',
      'United States Minor Outlying Islands',
      'Uruguay',
      'Uzbekistan',
      'Vanuatu',
      'Venezuela',
      'Vietnam',
      'Virgin Islands, British',
      'Virgin Islands, U.S.',
      'Wallis and Futuna',
      'Western Sahara',
      'Yemen',
      'Zambia',
      'Zimbabwe'
    ];


  });
