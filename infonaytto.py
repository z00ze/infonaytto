# coding=utf-8
import os
import cherrypy
import random
import string
import json
# db stuff
import dbstuff

def getHeader():
	return '<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="style/reset.css"><link rel="stylesheet" type="text/css" href="style/main.css"><link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lato"><title>Asteekkareiden infonäyttö</title>'+getScripts()+'</head><body onload="start()"><div id="header"><img src="images/asteriski_logo.png"><img src="images/digit_logo.png"><h1>Infonäyttö</h1><h1 id="clock"></h1><h1 id="weatherNow"></h1></div><div class="grid-container">'

def getFooter():
	return '</div></body></html>'

def getScripts():
	scripts = '<script src="scripts/clock.js"></script><script src="scripts/weather.js"></script><script>function start(){setWeather();}</script>'
	return scripts

def startJSfunctions():
	return 'setWeather();'

def getBlock(obj):
	if(int(obj[1])>5):
		return ''
	return '<div class="grid-item"><div class="grid-wrapper border-rad"><div uid="'+str(obj[0])+'" class="grid-title border-rad"><h1>'+str(obj[2])+'</h1><a href="' + str(obj[3]) + '" target="_blank"><img src="images/fullscreenicon.png"></a></div><iframe scrolling="no" src="' + str(obj[3]) + '" frameborder="0" allowfullscreen align="center"></iframe></div></div>'


@cherrypy.expose
class restApi(object):

	@cherrypy.tools.accept(media='application/json')
	def GET(self, x=''):
		page = ''
		blocks = dbstuff.getBlocks()
		blocks.sort(key=lambda tup: tup[1])
		for value in blocks:
			page += getBlock(value)
		return getHeader() + page + getFooter()

	@cherrypy.tools.accept(media='application/json')
	def POST(self, x):
		baseauth = cherrypy.request.headers.get('Authorization')
		rights = dbstuff.allowedUser(baseauth)
		dbstuff.spawnDB()
		if(rights):
			if(x == 'new'):
				cl = cherrypy.request.headers['Content-Length']
				rawbody = cherrypy.request.body.read(int(cl))
				body = json.loads(rawbody)
				dbstuff.newBlock(body)
			if(x == 'update'):
				cl = cherrypy.request.headers['Content-Length']
				rawbody = cherrypy.request.body.read(int(cl))
				body = json.loads(rawbody)
				dbstuff.updateBlock(body)
			if(x == 'delete'):
				cl = cherrypy.request.headers['Content-Length']
				rawbody = cherrypy.request.body.read(int(cl))
				body = json.loads(rawbody)
				dbstuff.deleteBlock(body)
			if(x == 'newuser'):
				cl = cherrypy.request.headers['Content-Length']
				rawbody = cherrypy.request.body.read(int(cl))
				body = json.loads(rawbody)
				dbstuff.newUser(body)
			if(x == 'deleteuser'):
				cl = cherrypy.request.headers['Content-Length']
				rawbody = cherrypy.request.body.read(int(cl))
				body = json.loads(rawbody)
				dbstuff.deleteUser(body)
			if(x == 'swap'):
				cl = cherrypy.request.headers['Content-Length']
				rawbody = cherrypy.request.body.read(int(cl))
				body = json.loads(rawbody)
				dbstuff.swapBlocks(body)
			if(x == 'getAll'):
				return dbstuff.getAll()
			return '{"post":"successfull"}'
		else:
			return '{"post":"failed"}'

if __name__ == '__main__':
	current_dir = os.path.dirname(os.path.abspath(__file__))
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		},
		'/favicon.ico': {
			'tools.staticfile.on': True,
			'tools.staticfile.filename': os.path.join(current_dir, 'favicon.ico')
		},
		'/images': {'tools.staticdir.on': True,
					'tools.staticdir.dir': os.path.join(current_dir, 'images')},
		'/style': {'tools.staticdir.on': True,
				   'tools.staticdir.dir': os.path.join(current_dir, 'style')},
		'/scripts': {'tools.staticdir.on': True,
				   'tools.staticdir.dir': os.path.join(current_dir, 'scripts')},
		'/sounds': {'tools.staticdir.on': True,
				   'tools.staticdir.dir': os.path.join(current_dir, 'sounds')},
		'/blocks': {'tools.staticdir.on': True,
					'tools.staticdir.dir': os.path.join(current_dir, 'blocks')}
	}
	cherrypy.config.update(
		{'server.socket_host': '0.0.0.0', 'server.socket_port': 1337, })
	cherrypy.quickstart(restApi(), '/', conf)
