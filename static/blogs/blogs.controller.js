(function () {
  'use strict';

  angular
    .module('learnapp')
    .controller('BlogsHomeController', BlogsHomeController);

    BlogsHomeController.$inject = ['$rootScope', '$scope','$http'];

	function BlogsHomeController($rootScope,$scope,$http){


		 $http.get('api/getblogs/')
		 .then(function(data){
            $scope.blogs=data.data;
		 },function(error){

		 });


	}


})();