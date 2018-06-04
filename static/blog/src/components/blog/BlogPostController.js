import angular from 'angular'

var blogPostController = function($scope, blogService, loginService, $location) {
  $scope.blog = { 'title': '', 'message': ''}
  var init = function () {
    if ( ! loginService.checkUserLoggedIn()) {
      $location.path('/login').search({'next':'post'})
    }
  }
  $scope.saveBlog = function () {
    var promise = blogService.createBlog($scope.blog)
    promise.then(function(data) {
      $location.path('/')
    }).catch(function(error){
      console.log('Error while loading blogs' + error)
    })
  }
  // Initialize
  init()
}
angular.module('app').
  controller('BlogPostController', ['$scope','BlogService','LoginService', '$location',blogPostController])
