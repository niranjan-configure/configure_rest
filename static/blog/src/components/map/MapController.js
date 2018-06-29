import angular from 'angular'

var mapController = function ($scope, NgMap) {
  $scope.markers = []
  $scope.map_center = "40.74, -74.18"
  var vm = this

  // Simple load function
  $scope.loadMarkers = function () {
    // Service method to be invoked here to load the marker jsons..
    $scope.markers= [
      {'department_name': 'SALES', 'present': 23, 'absent': 10, 'position':'40.74, -74.18', 'shown': false},
      {'department_name': 'MARKETING', 'present': 18, 'absent': 9, 'position':'40.70, -74.15' ,'shown': false},
      {'department_name': 'ENGINEERING', 'present': 16, 'absent': 5, 'position':'40.70, -74.18' ,'shown': false}
    ]

  }

  $scope.checkRed = function(marker) {
    return marker.absent >= 10
  }
  $scope.checkOrange = function(marker) {
    return marker.absent > 5 && marker.absent < 10
  }
  $scope.checkGreen = function(marker) {
    return marker.absent <= 5
  }
  $scope.departmentSelected = function (index) {
    $scope.map_center= $scope.markers[index].position
  }
  $scope.markerOpen = function(evt, index) {
    console.log(evt)
    $scope.markers[index].shown = true
  }
  $scope.markerClose = function(evt, index) {
    console.log(evt)
    $scope.markers[index].shown = false
  }
  // Code to be executed as part of controller load...
  $scope.loadMarkers()

}
angular.module('blogapp').
  controller('MapController', ['$scope','NgMap', mapController])
