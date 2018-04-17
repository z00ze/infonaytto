var myVar = setInterval(function() {myTimer();}, 1000);
var pokemon = true;
var pokemontime = '13.37';
function myTimer() {
    var d = new Date().toLocaleTimeString('fi-FIN');
    if(d.toString().substr(0, 5)==pokemontime && pokemon){
        var audio = new Audio('../sounds/poksu.mp3');
        audio.play();
        pokemon = false;
    }
    if(d.toString().substr(0, 5)!=pokemontime){
        pokemon = true;
    }
    document.getElementById("clock").innerHTML = d;
}