import socket
import sys
import threading

class Network(object):
	sendOrientation = None
	sendAzimuth = None

	portNumber = 0
	isinitialized = False
	s = None
	connection = None

	class myThread(threading.Thread):
		network = None
		def __init__(self, threadID, name, counter, network):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.counter = counter
			self.network = network
		def run(self):
			print("Starting" + self.name)
			Network.startServer(self.network)
			print("Exiting" + self.name)
	def setAzimuth(self, message):
		self.sendAzimuth = message

	def setOrientation(self, message):
		self.sendOrientation = message

	def waitForPing(self):
		if(s != None):
			receive = s.recv(1024)
		if receive == None or receive == ' ' :
			print("Hasn't received ping")
	def sendMessage(self, message):
		if(isIntialized != False):
			connection.send(message + b'\n')
	def __init__(self):
		global portNumber
		portNumber = 3341
		global isInitialized
		isInitialized = False
	def userServer(self):
		global s
		thread1 = self.myThread(1, "Thread-1",1,self)
		thread1.start()
		print("thread started")
	def startServer(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = "localhost"
		s.bind((host,portNumber))

		global connection
		print("in startServer")
		s.listen(5)

		connection, addr = s.accept()
		print("accepted")
		global isInitialized
		isInitialized = True
		
		while True:
			self.sendMessage(self.sendAzimuth.encode('utf-8') + b";" + self.sendOrientation.encode('utf-8'))
			self.sendAzimuth = None
			self.sendOrientation = None
