import angular from 'angular'

var imagePageController = function($scope, $routeParams, imageService ) {
  $scope.key = $routeParams.key
  $scope.image = {}
  $scope.addComment = false
  $scope.likeDone = false
  $scope.comment = {'comment_text': '', 'image': $scope.key }

  // Simple load function
  $scope.loadImage = function () {
    var promise = imageService.getImage($scope.key)
    promise.then(function(result) {
      $scope.image = result.data
    }).catch(function(error){
      console.log('Error while loading images' + error)
    })
  }
  $scope.saveComment = function () {
    var promise = imageService.addComment($scope.comment)
    promise.then(function (result) {
      $scope.addComment = false
      $scope.comment = {'comment_text': '', 'image': $scope.key }
      $scope.loadImage()
    }).catch(function (error) {
      console.log('Error while saving comment' + error)
    })
  }
  $scope.addLike = function () {
    var promise = imageService.addLike($scope.key)
    promise.then(function (result) {
      Materialize.toast( $('<span>Added your like !!</span>'), 3000, 'rounded');
      $scope.loadImage()
    }).catch(function (error) {
      console.log('Error while saving like' + error)
    })
  }

  $scope.loadImage()

}
angular.module('blogapp').
  controller('ImagePageController', ['$scope', '$routeParams','ImageService', imagePageController])
