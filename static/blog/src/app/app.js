import angular from 'angular'


// import '../style/app.css';
import 'materialize-css/dist/css/materialize.min.css'


let app = () => {
  return {
    template: require('./app.html'),
    controller: 'AppCtrl',
    controllerAs: 'app'
  }
}

class AppCtrl {
  constructor($scope,$window, $location) {
    // this.url = 'https://github.com/preboot/angular-webpack'
    $scope.loggedIn = true
    // this.checkUserLoggedIn($scope,$window, $location)
  }
  checkUserLoggedIn($scope, $window, $location) {
    if ($window.sessionStorage.blogtoken === '' || typeof($window.sessionStorage.blogtoken) === 'undefined') {
      $scope.loggedIn = false
      $location.path('/login')
    } else {
      $scope.loggedIn = true
    }
  }
}

const MODULE_NAME = 'app'
const sw_module = require('angular-h-sweetalert')
angular.module(MODULE_NAME, [require('angular-route'),
  require('angular-marked'),
  require('angular-materialize'),
  require('ng-quill'),
  sw_module['ngSweetAlert2']])
  .directive('app', app)
  .controller('AppCtrl', AppCtrl)

angular.module(MODULE_NAME).config(['markedProvider', function (markedProvider) {
  markedProvider.setOptions({gfm:true})
}])
require('angular-h-sweetalert')
angular.module(MODULE_NAME).directive("fileread", [function () {
    return {
        scope: {
            fileread: "="
        },
        link: function (scope, element, attributes) {
            element.bind("change", function (changeEvent) {
                scope.$apply(function () {
                    scope.fileread = changeEvent.target.files[0];
                });
            });
        }
    }
}])
require('./common')
require('../routes')

export default MODULE_NAME
