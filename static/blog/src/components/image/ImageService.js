import angular from 'angular'

var imageServiceFactory = function ($http) {
  var getImages = function () {
    return $http.get('/blogmgmt/api/images/')
  }
  var getImage = function (key) {
    return $http.get('/blogmgmt/api/images/' + key + '/')
  }
  var createImage = function (blog) {
    return $http.post('/blogmgmt/api/images/', blog)
  }
  var uploadImage = function(file) {
    const url = '/blogmgmt/api/imageUpload/'
    const formData = new FormData()
    formData.append('file',file)
    const config = {
        headers: {
            'content-type': 'multipart/form-data'
        }
    }
    return  $http.post(url, formData,{
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        })
  }
  return {
    getImages: getImages,
    getImage: getImage,
    createImage: createImage,
    uploadImage: uploadImage
  }
}

angular.module('app').
  factory('ImageService',['$http', imageServiceFactory])
