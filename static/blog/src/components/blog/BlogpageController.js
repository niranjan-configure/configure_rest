import angular from 'angular'

var blogPageController = function($scope, $routeParams, blogService ) {
  $scope.key = $routeParams.key
  $scope.blog = {}
  $scope.addComment = false
  $scope.likeDone = false
  $scope.comment = {'comment_text': '', 'post': $scope.key }

  // Simple load function
  $scope.loadBlog = function () {
    var promise = blogService.getBlog($scope.key)
    promise.then(function(result) {
      $scope.blog = result.data
    }).catch(function(error){
      console.log('Error while loading blogs' + error)
    })
  }
  $scope.saveComment = function () {
    var promise = blogService.addComment($scope.comment)
    promise.then(function (result) {
      $scope.addComment = false
      $scope.comment = {'comment_text': '', 'post': $scope.key }
      $scope.loadBlog()
    }).catch(function (error) {
      console.log('Error while saving comment' + error)
    })
  }
  $scope.addLike = function () {
    var promise = blogService.addLike($scope.key)
    promise.then(function (result) {
      Materialize.toast( $('<span>Added your like !!</span>'), 3000, 'rounded');
      $scope.loadBlog()
    }).catch(function (error) {
      console.log('Error while saving like' + error)
    })
  }

  $scope.loadBlog()

}
angular.module('app').
  controller('BlogPageController', ['$scope', '$routeParams','BlogService', blogPageController])
