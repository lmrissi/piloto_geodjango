var gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var pocos_style = {
    fillColor: '#00BFFF',
    weight: 2,
    opacity: 1,
    color: '#00BFFF',
    fillOpacity: 0.2
};

var mun_style = {
    fillColor: '#FF8C00',
    weight: 2,
    opacity: 1,
    color: '#FFA500',
    fillOpacity: 0.2
};

var pocos = L.geoJson([], {
    style: pocos_style,
    pointToLayer: function (feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 4});
    },
    });

var mun = L.geoJson([], {
    style: mun_style,});

var pocos_url = $("#pocos_geojson").val();

var mun_url = $("#mun_geojson").val();

$.getJSON(pocos_url, function (data) {
    // Add GeoJSON layer
    pocos.addData(data);
});

$.getJSON(mun_url, function (data) {
    // Add GeoJSON layer
    mun.addData(data);
});

var map = L.map('map', {
    center: [-7.277444, -36.891285],
	zoom: 8,
	layers: [gstreets, satellite, mun, pocos, ]
});

var baseLayers = {
	"Google Streets": gstreets,
	"Google Satélite": satellite
};

var overlays = {
    "Municípios": mun,
    "Poços": pocos,
};

L.control.layers(baseLayers, overlays).addTo(map);