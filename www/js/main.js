// Create a map variable using Leaflet
// Set the View to center on California
var map = L.map('map').setView([37.10, -120.58], 6);

/**
 -- Establishing a connection to the Mapbox Tile Server --
 You need to setup a Free account to get a valid MapID and access key (sign up at mapbox.com)

 Example for Tile Server URL
 http://api.tiles.mapbox.com/v4/{mapid}/{z}/{x}/{y}.{format}?access_token=<your access token>
**/

// the MapID is the 'mapbox.pirates' in the url below
L.tileLayer('http://api.tiles.mapbox.com/v4/mapbox.pirates/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoic2lnZXAzMTEiLCJhIjoieHl3VlZmayJ9.zu3NQM5L6WfJt5OVNlxfqA',
{
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18
}).addTo(map);




// Image Object Constructor Function

function MapImage(id, lat, lon) {
	this.id = id;
	this.lat = lat;
	this.lon = lon;
};

function dmsToDecimalDegrees(dms){
	// dms is an array of degrees, minutes, seconds
	var deg = dms[0],
		min = dms[1],
		sec = dms[2];
	var decimalDegrees = deg + min/60 + sec/3600
	return decimalDegrees
}

function convertStringGeoCoords(coords){
	// expect coords of format "[33, 25, 7717/500]"
	// trim off the [] values & split on the comma
	var coordElements = coords.replace('[', '').replace(']', '').split(",");
	// convert values to numbers using built-in parseInt() function.
	// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt
	var degrees = parseInt(coordElements[0], 10);
	var minutes = parseInt(coordElements[1], 10);

	// IF the seconds element contains '/' convert fraction to decimal seconds
	if (coordElements[2].match('\/') != null) {
		var rawSeconds = coordElements[2].split('/');
		var numerator = new Number(rawSeconds[0]);
		var denominator = new Number(rawSeconds[1]);
		var seconds = numerator / denominator
	} else {
		var seconds = new Number(coordElements[2]);
	}

 	return [degrees, minutes, seconds]
}


var app = {

	images : [],

	init : function(){

		app.getAllImages();
		app.dropMarkers();


	},

	convertDataToImage : function(dataObject){
		var dataId = dataObject.id;
		var latitude = dmsToDecimalDegrees(convertStringGeoCoords(dataObject.latitude));
		var longitude = dmsToDecimalDegrees(convertStringGeoCoords(dataObject.longitude));

		return new MapImage(dataId, latitude, longitude);

	},

	dropMarkers : function(){
		//Loop over the images array and insert a marker on the map
	},

	getAllImages : function() {
		// GET url to fetch simple object with all images in an array
		var url = "http://127.0.0.1:5000/api/v1/images/";
		$.getJSON(url, function(data){
			// Save Objects into the app.images array
			for (var i=0; i < data.images.length; i++){

				app.images.push(
					app.convertDataToImage(data.images[i])
					);
			}
			console.log("Loaded "+app.images.length+" from the server.");

		});
	}
}