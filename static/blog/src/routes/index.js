import angular from 'angular'


angular.module('app').config(
  function ($routeProvider, $locationProvider) {
    $routeProvider.when('/', {
      templateUrl: 'partials/blogs/blog-list.html',
      controller: 'BloglistController'
    }).when('/blog/:key', {
      templateUrl: 'partials/blogs/blog-page.html',
      controller: 'BlogPageController'
    }).when('/post', {
      templateUrl: 'partials/blogs/post.html',
      controller: 'BlogPostController'
    }).when('/images', {
      templateUrl: 'partials/images/image-list.html',
      controller: 'ImagelistController'
    }).when('/upload', {
      templateUrl: 'partials/images/image-upload.html',
      controller: 'ImageUploadController'
    }).when('/login', {
      templateUrl: 'partials/login/login.html',
      controller: 'LoginController'
    })
    .when('/signup', {
      templateUrl: 'partials/login/signup.html',
      controller: 'SignupController'
    })
    $locationProvider.html5Mode(true);
  }
)
require('../components/blog')
require('../components/image')
require('../components/login')
