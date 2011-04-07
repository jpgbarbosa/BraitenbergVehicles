
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


import breve
import os

class myBraitenbergControl( breve.BraitenbergControl ):
	def __init__( self ):
		breve.BraitenbergControl.__init__( self )
		self.leftSensor = None
		self.leftWheel = None
		self.light = None
		self.n = 0
		self.rightSensor = None
		self.rightWheel = None
		self.vehicle = None
		self.block = None
		self.obj = None
		myBraitenbergControl.init( self )

	def init( self ):
		'''Several scenarios available.'''
		
		filename =  "Explorer.txt"
		f = open(filename, "r")
	
		#Reads the limits of the maze.
	
		#Reads the maze itself.
		text = f.readlines()

		#Iterates over the lines.
		for i in xrange(len(text)):
			for t in xrange(len(text[i])):
				if (text[i][t] == "o"):
					self.obj = breve.createInstances ( breve.BraitenbergOlfaction, 1)
					self.obj.move( breve.vector(i*3, 0, t*2))  
					self.obj.setIntensity(1.5)
				elif (text[i][t] == "s"):
					self.obj = breve.createInstances ( breve.BraitenbergSound, 1)
					self.obj.move( breve.vector(i*3, 0, t*2))  
					self.obj.setIntensity(3)
				elif (text[i][t] == "l"):
					self.obj = breve.createInstances ( breve.BraitenbergLight, 1)
					self.obj.move( breve.vector(i*3, 0, t*2))  
					self.obj.setIntensity(1.5)
				elif (text[i][t] == "b"):
					self.obj = breve.createInstances ( breve.BraitenbergBlock, 1)
					self.obj.move( breve.vector(i*3, 0, t*2))
						
			
		'''Creates the first vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergExplorer, 1 )
		self.watch( self.vehicle )
			
		'''Complex Explorer'''
		self.vehicle.move(breve.vector(20,1,80))
		self.vehicle.rotate(breve.vector(0,1,0),0.7)
	
breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
