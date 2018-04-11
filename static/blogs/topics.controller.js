(function () {
  'use strict';

  angular
    .module('learnapp')
    .controller('TopicsController', TopicsController);

    TopicsController.$inject = ['$rootScope', '$scope','$http','$window','$routeParams'];

	function TopicsController($rootScope,$scope,$http,$window,$routeParams){


		$scope.topicId=$routeParams.id;
		$scope.newTopic={
			subject:"",
			message:"",
			id:$scope.topicId
		}

		$scope.onNewTopic=function(){
         $http({
         	method:'POST',
         	url:'api/newtopic/',
         	data:$scope.newTopic
         }).then(function(data){

         	$window.location='boards/'+$scope.topicId

         },function(error){

         })

		}


	}


})();