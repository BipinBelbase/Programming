
var ans = (function(){
    var privateval = 12;

    return {
        getter: function(){
            console.log(privateval);

        }
    }
})()