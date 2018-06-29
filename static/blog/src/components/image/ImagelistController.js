import angular from 'angular'

var imageController = function ($scope, imageService) {
  $scope.images = []
    /*{ 'title': 'Creek of Woman',
      'content': 'Post no so what deal evil rent by real in. But her ready least set lived spite solid. September how men saw tolerably two behaviour arranging. She offices for highest and replied one venture pasture. Applauded no discovery in newspaper allowance am northward. Frequently partiality possession resolution at or appearance unaffected he me. Engaged its was evident pleased husband. Ye goodness felicity do disposal dwelling no. First am plate jokes to began of cause an scale. Subjects he prospect elegance followed no overcame possible it on'
    },
    { 'title': 'Day of War',
      'content': 'Now indulgence dissimilar for his thoroughly has terminated. Agreement offending commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted. '
    },
    { 'title': 'The Stopping Dog',
      'content': 'Arrived compass prepare an on as. Reasonable particular on my it in sympathize. Size now easy eat hand how. Unwilling he departure elsewhere dejection at. Heart large seems may purse means few blind. Exquisite newspaper attending on certainty oh suspicion of. He less do quit evil is. Add matter family active mutual put wishes happen.  '
    },
    { 'title': 'Fire and Alien',
      'content': 'Projecting surrounded literature yet delightful alteration but bed men. Open are from long why cold. If must snug by upon sang loud left. As me do preference entreaties compliment motionless ye literature. Day behaviour explained law remainder. Produce can cousins account you pasture. Peculiar delicate an pleasant provided do perceive.  '
    },
    { 'title': 'Cold Witchs',
      'content': 'An country demesne message it. Bachelor domestic extended doubtful as concerns at. Morning prudent removal an letters by. On could my in order never it. Or excited certain sixteen it to parties colonel. Depending conveying direction has led immediate. Law gate her well bed life feet seen rent. On nature or no except it sussex.   '
    },*/
  //]

  // Simple load function
  $scope.loadImages = function () {
    var promise = imageService.getImages()
    promise.then(function(result) {
      $scope.images.length = 0
      $scope.images.push.apply($scope.images,result.data)
      console.log(' Blogs = ' + $scope.images.length)
    }).catch(function(error){
      console.log('Error while loading images' + error)
    })
  }

  // Code to be executed as part of controller load...
  $scope.loadImages()


}
angular.module('blogapp').
  controller('ImagelistController', ['$scope','ImageService', imageController])
