import angular from 'angular'

var loginController = function ($scope, loginService, $location, $window, $routeParams) {
  $scope.creds = {'username': '','password':''}

  $scope.login = function () {
    var promise = loginService.login($scope.creds)
    promise.then(function(result) {
      console.log('Logged In ')
      $window.sessionStorage.blogtoken = result.data.token
      $location.search('next', null)
      if ($routeParams.next !== '' || typeof($routeParams.next) !== 'undefined') {
        $location.path('/'+$routeParams.next)
      } else {
        $location.path('/')
      }
    }).catch(function(error){
      console.log('Error Loggin In' + error.data.error)
      Materialize.toast( $('<span>Login Error !!' + error.data.error + '  Try again</span>'), 3000, 'rounded');
    })
  }

  // Code to be executed as part of controller load...
  //$scope.loadImages()


}
angular.module('blogapp').
  controller('LoginController', ['$scope','LoginService', '$location','$window', '$routeParams' , loginController])
