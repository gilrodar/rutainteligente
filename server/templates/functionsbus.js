//llamada al api rest
var xmlhttp2 = new XMLHttpRequest();
var url2 = "http://192.168.119.180:8080/json/buses";
var myJson2;

var tiempo = [];
var ocupacion = [];
var direccion = [];
var a = 1;

xmlhttp2.onreadystatechange = function() {
if (xmlhttp2.readyState == 4 && xmlhttp2.status == 200) {
    	myJson2 = JSON.parse(xmlhttp2.responseText);

    	var direc = document.getElementById("direccion");//Manipulación del DOM
    	var time = document.getElementById("minutos");
    	var ocupation = document.getElementById("ocupacion");

		var p1 = document.createElement("p");
		var p2 = document.createElement("p");
		var p3 = document.createElement("p");

    	for(var i = 0; i<myJson2.buses.length; i++){
    		if(id == myJson2.buses[i].nextstation){//Comparación de trenes cerca
    			
    			console.log(myJson2.buses[i]);
    			for(var j=0; j<=a; j++){
	    			ocupacion[j] = myJson2.buses[i].room;
	    			tiempo[j] = myJson2.buses[i].timetonextstation;
	 				console.log(ocupacion);
	    			console.log(tiempo);
	    		}

    			if(id+1 == myJson2.buses[i].prevstation){//Comparacion de direccion
    					direccion[i] = "Dirección Caminero-Indios Verdes";
    			 		
    			 	}
    			else if(id-1 == myJson2.buses[i].prevstation){
    					direccion[i] = "Dirección Indios-Verdes-Caminero";
    					
    				}

    			p1.innerHTML = direccion[i];//direccion
    			console.log(p1);
    			direc.appendChild(p1);

    			p2.innerHTML = "Tiempo: " + tiempo[i] + " segundos";//tiempo
    			console.log(p2);
    			time.appendChild(p2);	

   		 		p3.innerHTML = "Ocupación del transporte: " + ocupacion[i] + " %";//ocupacion
   		 		console.log(p3);
   		 		ocupation.appendChild(p3);
    			
			} 
			a++;
		}
	}
}

xmlhttp2.open("GET", url2, true);
xmlhttp2.send();	




