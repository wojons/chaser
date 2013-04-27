import tornado.ioloop
import tornado.web
import inspect
import importlib
import os
import sys
import glob


if __name__ == "__main__":
	endPoints = {'http' : list(), 'sock' : dict()}
	controllers = dict()
	
	for i in glob.glob('./controllers/*.py'): #we dont need the pyc files
		#print i
		#fix file name
		i = i.replace(".py", "")
		i = i.replace("./controllers/", "")
		
		controllers[i] = importlib.import_module('controllers.'+i)
		if hasattr(controllers[i], 'handlers') == False:
			continue
			
		m = controllers[i].handlers() #get the hanlder class starteds
		members = inspect.getmembers(m) #list all the memebers because they are the handlers
		
		for member in members:
			if not member[0].startswith("_"):
				endPoints['http'].append((r"/api/http/"+i+"/"+member[0], getattr(m, member[0])))
				#print member[0]
	
	print endPoints
	application = tornado.web.Application(endPoints['http'])			
	application.listen(54213)
	tornado.ioloop.IOLoop.instance().start()
