import angular from 'angular'

var imageUploadController = function($scope, imageService, $location) {
  $scope.image = { 'name': '', 'description': '', 'location': ''}
  $scope.file = ''
  $scope.uploading = false

  $scope.saveImage = function () {
    var promise = imageService.createImage($scope.image)
    promise.then(function(data) {
      $scope.uploading = false
      $location.path('/images')
    }).catch(function(error){
      console.log('Error while saving image' + error)
      $scope.uploading = false
    })
  }
  $scope.uploadImage = function () {
    $scope.uploading = true
    var promise = imageService.uploadImage($scope.file)
    promise.then(function (result) {
      $scope.image.location = result.data
      $scope.saveImage()
    }).catch (function (error) {
      console.log('Error while saving image' + error)
      $scope.uploading = false
    })
  }

}
angular.module('blogapp').
  controller('ImageUploadController', ['$scope','ImageService', '$location',imageUploadController])
