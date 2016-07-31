
//llamada al api rest
var xmlhttp = new XMLHttpRequest();
var url = "http://192.168.119.180:8080/json/stations";
var myJson;

// var url2 = "http://192.168.119.180:8080/json/buses";
// var myJson2;

var latitud = [];
var longitud = [];
var imagenes = [];
var nombre = [];

var ubicacion = [19.46883,-99.1388]; //ubicacion de la estación.
var id;


xmlhttp.onreadystatechange = function() {
if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
		myJson = JSON.parse(xmlhttp.responseText);
	
    

    
    //Sacar datos del Json
    for(var i = 0; i<myJson.stations.length; i++){
	    	latitud[i] = myJson.stations[i].latitude;
	    	longitud[i] = myJson.stations[i].longitude;
	    	nombre[i] = myJson.stations[i].name;
	    	imagenes[i] = myJson.stations[i].urlimg;

    	};

    //Insertar etiquetas
    var ruta = document.getElementById("Ruta");
    var h3 = document.createElement("h3");
    //Insertar imagenes
    // var image = document.getElementById("imagen");
    // var img = document.createElement("img");

    //Algoritmo
    for(i = 0; i<myJson.stations.length; i++){ //Recorremos el arreglo
     	if(ubicacion[0] == [myJson.stations[i].latitude]){//comparamos primer termino
     		for(j = 0; j<myJson.stations.length; j++){//Volvemos a recorrer
    			if(ubicacion[1] == [myJson.stations[j].longitude]){//comparamos ubicación
					console.log("Comparación Funcionando");
					if(i==j){
						h3.innerHTML = nombre[i];
		    			ruta.appendChild(h3);
		    			id = myJson.stations[i].id;
					}

    			}
 			
     		} 
    		
		    }
		} 
	} ;
return {myJson: myJson, longitud: longitud, imagenes: imagenes, nombre: nombre, latitud:latitud, id:id };
};
	
xmlhttp.open("GET", url, true);
xmlhttp.send();	




