import tornado.websocket
import tornado.httpclient
import json
listeners = []

class WsHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    self.httpClient = tornado.httpclient.HTTPClient()
    print "opened a new websocket"
    listeners.append(self)
    print listeners

  def on_message(self, message):
     #r = self.httpClient.fetch("http://www.google.com/")
     r = self.httpClient.fetch("http://127.0.0.1:54213/api/http/users/login")
     self.write_msg(r.body)
     self.write_msg(u"You Said: " + message)
     print ("in on_message " + message)
     change = message
     #self.write_message(message)

  def on_close(self):
    print 'connection closed'
    listeners.remove(self)
    
  def write_msg(self, change):
    print ("in write message " + change)
    self.write_message(change)
