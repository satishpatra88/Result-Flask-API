var url="http://127.0.0.1:5000/result?regno="
var app=angular.module("mymodule",[]);

app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
  }]);


app.controller("contro",($scope,$http)=>{


    console.log(url);
    $scope.up=function(){
        $http.get(`${url}${$scope.reg}`).then(
            (response)=>
            {
                console.log("😎✔");
                $scope.data=response.data;
            }
            ,
            (fail)=>
            {
                console.log("👿");
                console.log(fail);
            }
        );
    };
    
});