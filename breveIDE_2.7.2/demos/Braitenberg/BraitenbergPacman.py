
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
				self.setIsPacman(1)
		self.changeFloor()

		filename = "maze.txt"
		f = open(filename, "r")
	
		#Reads the limits of the maze.
	
		#Reads the maze itself.
		text = f.readlines()

		#Iterates over the lines.
		for i in xrange(len(text)):
			for t in xrange(len(text[i])):
				if (text[i][t] == "o" or text[i][t] == "f" or text[i][t] == "n"):
					self.obj = breve.createInstances ( breve.BraitenbergSound, 1)
					self.obj.move( breve.vector(i*3, 0, t*2))  
					self.obj.setIntensity(1.5)
				elif (text[i][t] == "*"):
					self.block = breve.createInstances ( breve.BraitenbergBlock, 1)
					self.block.move( breve.vector(i*3, 0, t*2))
					self.block.setReflection(2.5)
			
		self.disableShadowVolumes()
		self.PacmanMusic.play(1)
		
		'''Creates the first vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergPacman, 1 )
		self.watch( self.vehicle )
		
		self.vehicle.move(breve.vector(48,0.6,7))
		
		'''Creates the first monster.'''
		monsterOne = breve.createInstances( breve.BraitenbergMonster, 1 )
		monsterOne.move(breve.vector(20,0.6,15))
		monsterOne.rotate(breve.vector(0,1,0), 3.14)
		'''Creates the second monster.'''
		monsterTwo = breve.createInstances( breve.BraitenbergMonster, 1 )
		monsterTwo.move(breve.vector(35,0.6,48))
		
breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
