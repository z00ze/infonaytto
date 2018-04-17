var weathertiming = setInterval(setWeather, 1000000);
    function setWeather(){
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET","http://api.openweathermap.org/data/2.5/weather?q=Turku,fi&appid=9e9814daf369e93cd92f2d69458b57cc&units=metric",false);
            xhttp.send(null);
            var response = JSON.parse(xhttp.responseText);
			console.log(response);
            document.getElementById("weatherNow").innerHTML = response["main"]["temp"]+'°C '+response["weather"][0]["description"];
        }