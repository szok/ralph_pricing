'use strict';

var scrooge = angular.module('scrooge.controller', []);

scrooge.controller('mainCtrl', ['$scope', '$routeParams', '$location', 'menuService', 'menuCalendar', 'stats', function ($scope, $routeParams, $location, menuService, menuCalendar, stats) {
    stats.init();
    $scope.menuService = menuService;
    $scope.menuCalendar = menuCalendar;
    $scope.stats = stats;
    $scope.getDictLength = function (dict) {
        if (typeof(dict) == 'object') {
            return Object.keys(dict).length;
        }
    };
}]);
