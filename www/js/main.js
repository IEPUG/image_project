// Create a map variable using Leaflet
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

