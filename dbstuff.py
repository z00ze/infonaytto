#coding=utf-8
import sqlite3,json
import hashlib
import base64
#random stuff
import random

db = 'infonaytto/infodisplay.db'

# Database tables
# blocks : id int | position str | name str | url str
# users : id int | name str | password str

def spawnDB():
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('CREATE TABLE IF NOT EXISTS blocks (id integer primary key AUTOINCREMENT,position integer NOT NULL, name varchar NOT NULL, url varchar NOT NULL)')
			connection.execute('CREATE TABLE IF NOT EXISTS users (id integer primary key AUTOINCREMENT, name varchar NOT NULL, password varchar NOT NULL)')

def newBlock(obj):
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('DELETE FROM blocks WHERE position = '+obj['position'])
			connection.execute('INSERT INTO blocks (position,name,url) VALUES (?,?,?)',[obj['position'],obj['name'],obj['url']])

def newUser(obj):
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('INSERT INTO users (name,password) VALUES (?,?)',[obj['name'],hashlib.sha224(obj['password'].encode()).hexdigest()])
			
def deleteUser(obj):
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('DELETE FROM users WHERE name = "'+obj['name']+'"')

def updateBlock(obj):
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('DELETE FROM blocks WHERE position = '+obj['position'])
			connection.execute('INSERT INTO blocks (position,name,url) VALUES (?,?,?)',[obj['position'],obj['name'],obj['url']])

def deleteBlock(obj):
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('DELETE FROM blocks WHERE position = '+obj['uid'])

def updateListBlock(listA):
	with sqlite3.connect(db,timeout=10) as connection:
			connection.execute('DELETE FROM blocks WHERE position = '+str(listA[1]))
			connection.execute('INSERT INTO blocks (position,name,url) VALUES (?,?,?)',[str(listA[1]),listA[2],listA[3]])

def getBlocks():
	with sqlite3.connect(db,timeout=10) as connection:
		connection.text_factory = str
		cursor = connection.execute('SELECT * FROM blocks')
		rows = cursor.fetchall()
		return rows

def getAll():
	with sqlite3.connect(db,timeout=10) as connection:
		connection.text_factory = str
		cursor = connection.execute('SELECT * FROM blocks')
		blocks = cursor.fetchall()
		cursor = connection.execute('SELECT * FROM users')
		users = cursor.fetchall()
		return '['+json.dumps(blocks)+','+json.dumps(users)+']'

def getBlock(position):
	with sqlite3.connect(db,timeout=10) as connection:
		connection.text_factory = str
		cursor = connection.execute('SELECT * FROM blocks WHERE position = '+str(position))
		row = cursor.fetchall()
		return row

def swapBlocks(obj):
	first = getBlock(obj[0])
	second = getBlock(obj[1])
	firsty = []
	for value in first:
		firsty.append(list(value))
	secondy = []
	for value in second:
		secondy.append(list(value))
	firsty[0][1], secondy[0][1] = secondy[0][1], firsty[0][1]
	[firsty] = firsty
	[secondy] = secondy
	updateListBlock(firsty)
	updateListBlock(secondy)

def allowedUser(baseauth):
	auth = base64.urlsafe_b64decode(baseauth[6:]).split(':')
	with sqlite3.connect(db,timeout=10) as connection:
		connection.text_factory = str
		cursor = connection.execute('SELECT * FROM users WHERE (name = ?)',(auth[0],))
		data=cursor.fetchall()
		if(len(data)>0):
			if(str(data[0][2])==hashlib.sha224(auth[1].encode()).hexdigest()):
				return True
		return False

def getDBstr(name):
	with sqlite3.connect(db,timeout=10) as connection:
		connection.text_factory = str
		cursor = connection.execute('SELECT * FROM '+name)
		rows = cursor.fetchall()
		headers = list(cursor.description)
		index = 0
		for head in headers:
			rows.insert(index,str(head[0]))
			index += 1
		dbstr = '<table>'
		dbstr += '<tr>'
		for value in rows:
			if type(value) is str:
				dbstr += '<td>'+value+'</td>'
		dbstr += '</tr>'
		for value in rows:
			if type(value) is tuple:
				dbstr += '<tr>'
				for cell in value:
					dbstr += '<td>'+str(cell)+'</td>'
				dbstr += '</tr>'
		dbstr += '</table>'
		return dbstr