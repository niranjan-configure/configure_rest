import angular from 'angular'

var loginServiceFactory = function ($http, $window) {
  var login = function (creds) {
    return $http.post('/blogmgmt/api/login/', creds)
  }
  var signup = function (user) {
    return $http.post('/blogmgmt/api/signup/', user)
  }
  var checkUserLoggedIn = function() {
    if ($window.sessionStorage.blogtoken === '' || typeof($window.sessionStorage.blogtoken) === 'undefined') {
      return false
    } else {
      return true
    }
  }

  return {
    login: login,
    signup: signup,
    checkUserLoggedIn: checkUserLoggedIn
  }
}

angular.module('blogapp').
  factory('LoginService',['$http','$window', loginServiceFactory])
