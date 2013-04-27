import tornado.ioloop
import tornado.web

class handlers():		
	class login(tornado.web.RequestHandler):
		def get(self):
			self.write("Hello2, world")
		   
		def post(self):
			self.write("Post, world")

