import angular from 'angular'

var blogServiceFactory = function ($http) {
  var getBlogs = function () {
    return $http.get('/blogmgmt/api/blogs/')
  }
  var getBlog = function (key) {
    return $http.get('/blogmgmt/api/blogs/' + key + '/')
  }
  var createBlog = function (blog) {
    return $http.post('/blogmgmt/api/blogs/', blog)
  }
  var addComment = function (comment) {
    return $http.post('/blogmgmt/api/comments/', comment)
  }
  var addLike = function (post_key) {
    return $http.post('/blogmgmt/api/likes/', {'post': post_key})
  }
  return {
    getBlogs: getBlogs,
    getBlog: getBlog,
    createBlog: createBlog,
    addComment: addComment,
    addLike: addLike
  }
}

angular.module('blogapp').
  factory('BlogService',['$http', blogServiceFactory])
