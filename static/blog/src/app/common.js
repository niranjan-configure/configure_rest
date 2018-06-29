var angular = require('angular')
var currentApp = angular.module('blogapp')
currentApp.factory('authInterceptor', function ($rootScope, $q, $window,swal,$location) {
  return {
    request: function (config) {
    		config.headers = config.headers || {};
    		if (config.url.includes("windows.net")) {
		      	return config
		      }
		    if ($window.sessionStorage.blogtoken) {
		    	config.headers.Authorization = 'Token ' + $window.sessionStorage.blogtoken;
		    }
      return config;
    },
    response: function (response) {
      if (response.status === 401) {
      	swal({
            title: 'Error',
            text: 'Token Expired, Please Log in again.',
            type: 'error',
            showCancelButton: false,
            confirmButtonColor: '#DD6B55',
            confirmButtonText: 'Login',
            closeOnConfirm: true,
            closeOnCancel: false
        }, function(isConfirm) {
            if (isConfirm) {
                $location.path("/login")
				        $window.location.reload()
            }
        });

      }
      return response || $q.when(response);
    },
    responseError: function (response) {
      //var defer $q.defer();
      if (response.status === 401) {
      	swal({
            title: 'Error',
            text: 'Login session Expired, Please Log in again.',
            type: 'error',
            showCancelButton: false,
            confirmButtonColor: '#DD6B55',
            confirmButtonText: 'Login',
            closeOnConfirm: true,
            closeOnCancel: false
        }, function(isConfirm) {
            if (isConfirm) {
                //$location.path("login.html");
				$window.location.href="/login";
				//$window.location.reload();
            }
        });

      } else if (response.status === 400) {
      	swal({
            title: 'Error',
            text: 'Bad Request Error occured.Try with different settings or contact support.',
            type: 'error',
            showCancelButton: false,
            confirmButtonColor: '#DD6B55',
            confirmButtonText: 'OK',
            closeOnConfirm: true,
            closeOnCancel: false
        	}, function(isConfirm) {
            	if (isConfirm) {
                	return response || $q.when(response);
            	}
        	});
       } else if (response.status === 500) {
      	swal({
            title: 'Error',
            text: 'Server Error occured.Please try again or contact support if problem persists.',
            type: 'error',
            showCancelButton: false,
            confirmButtonColor: '#DD6B55',
            confirmButtonText: 'OK',
            closeOnConfirm: true,
            closeOnCancel: false
        	}, function(isConfirm) {
            	if (isConfirm) {
                	return response || $q.when(response)
            	}
        	});
       }
      else {
      return response || $q.when(response)
      }
    }
  };
});
currentApp.config(function ($httpProvider) {
  $httpProvider.interceptors.push('authInterceptor')
})
