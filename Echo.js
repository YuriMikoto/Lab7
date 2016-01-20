var url = "ws://149.153.102.47:8080/wstest";

var ws = new WebSocket(url);

ws.onopen = function() {
	ws.send("Hello world");
}

ws.onmessage = function(evt) {
	alert(evt.data);
}