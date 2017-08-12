{% load autoreload_tags %}
var ws;

function init() {
	ws = new WebSocket("ws://localhost:9001/");
	ws.onmessage = function(e) {
		var reload = true;
		var x = {% noreload %};
		for (i=0;i<x.length;i++)
			var path = "/"+x[i];
    		if (window.location.pathname.startsWith(path) === true) {
    			reload = false;
    		}
		if (reload === true) {
			window.location.reload(true);
		}
	};
}
init()