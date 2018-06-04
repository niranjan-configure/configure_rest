import angular from 'angular'

var signUpController = function ($scope, loginService, swal, $location) {
  $scope.user = {'username': '', 'password': ''}

  $scope.signup = function () {
    var promise = loginService.signup($scope.user)
    promise.then(function(result) {
      swal(
        'Great!',
        'You have signed up! Lets log you in',
        'success')
        .then( function () {
          $location.path('/login')
        })
    })
    .catch(function (error) {
      console.log('Error while signin up' + error.data.error)
      Materialize.toast( $('<span>Signup Error !! '+ error.data.error +' Try again</span>'), 3000, 'rounded')
    })
  }
}
angular.module('app').
  controller('SignupController', ['$scope','LoginService', 'swal', '$location', signUpController])
