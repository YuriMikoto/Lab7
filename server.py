from tornado import websocket, web, ioloop, httpserver
import tornado

connections = {}

class WSHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print("Websocket open")
		ip = self.request.remote_ip
		print('Client IP:' + ip)
		connections[ip] = self
		sendToAll(self, "lziugrlb.uzl.h,bg.lezujbh")
	
	def check_origin(self, origin):
		return True

	def on_message(self, message):
		print("Message received %s" %message)
		self.write_message("You said " + message)

	def on_close(self):
		print ("Websocket closed")

def sendToAll(self, message):
	#key is ip and value is the websockethandler
	for key, value in connections.items():
		value.write_message(message)

app= tornado.web.Application([
	#map the handler to the URI named "wstest"
	(r'/wstest', WSHandler),
])
 
if __name__ == '__main__':
	app.listen(8080)
	tornado.ioloop.IOLoop.instance().start()