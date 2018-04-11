angular
  .module('learnapp', ['ngRoute'])
  .config(config)
  .run(run);

  run.$inject = ['$http'];

  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }

  config.$inject = ['$routeProvider','$locationProvider'];

  function config($routeProvider,$locationProvider) {
  	$locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  	
    $routeProvider.when('/blogs', {
      controller: 'BlogsHomeController', 
      controllerAs: 'vm',
      templateUrl: '/static/blogs/blogs.home.html'
    })
    .when('/boards/:id', {
      controller: 'TopicsController', 
      controllerAs: 'vm',
      templateUrl: '/static/blogs/topics.html'
    })

    .when('/boards/:id/new', {
      controller: 'TopicsController', 
      controllerAs: 'vm',
      templateUrl: '/static/blogs/new_topic.html'
    })


    .otherwise('/blogs');

 }
