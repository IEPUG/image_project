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

function dmsToDecimalDegrees(deg, min, sec){
	var decimalDegrees = deg + min/60 + sec/3600
	return decimalDegrees
}

function convertStringGeoCoords(coords){
	// expect coords of format "[33, 25, 7717/500]"
	// trim off the [] values & split on the comma
	var coordElements = coords.replace('[', '').replace(']', '').split(",");
	// convert values to numbers
	var degrees = new Number(coordElements[0]);
	var minutes = new Number(coordElements[1]);

	// should check IF rawSeconds contains '/' first
	var rawSeconds = coordElements[2].split('/');
	var numerator = new Number(rawSeconds[0]);
	var denominator = new Number(rawSeconds[1]);
	var seconds = numerator / denominator

	var geoCoords = [degrees, minutes, seconds]
	return geoCoords

	// push onto the returned array
}


var app = {

	images : [],

	init : function(){

		app.getAllImages();
		app.dropMarkers();


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

				app.images.push(data.images[i]);
			}
			console.log("Loaded "+app.images.length+" from the server.");

		});
	}
}