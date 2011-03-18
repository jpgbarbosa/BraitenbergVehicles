
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
		self.scenario = 'Maze'
		self.block = None
		self.obj = None
		myBraitenbergControl.init( self )

	def init( self ):
		'''Several scenarios available.'''
		if self.scenario == 'Circle':
			self.n = 0
			while ( self.n < 40 ):
				breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector( ( 20 * breve.breveInternalFunctionFinder.sin( self, ( ( self.n * 1.570000 ) / 10 ) ) ), 2, ( 20 * breve.breveInternalFunctionFinder.cos( self, ( ( self.n * 1.570000 ) / 10 ) ) ) ) )
				self.n = ( self.n + 1 )
				
			self.n = 0
			while ( self.n < 20 ):
				breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector( ( 12 * breve.breveInternalFunctionFinder.sin( self, ( ( self.n * 3.140000 ) / 10 ) ) ), 1.5, ( 12 * breve.breveInternalFunctionFinder.cos( self, ( ( self.n * 3.140000 ) / 10 ) ) ) ) )
				self.n = ( self.n + 1 )
				
		elif self.scenario == 'Tunel':
			#Blocks	
			for i in range(10):
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(i*4,0,5))
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(i*4,0,-5))
				
			for i in range(10,14):	
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(i*4,0,5))
			
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(13*4,0,5))
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(13*4,0,0))
			
			for i in range(7):
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(13*4,0,-5-i*4))
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(10*4,0,-5-i*4))
				
			for i in range(7,9):	
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(13*4,0,-5-i*4))
			
			
			for i in range(10):
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(i*4,0,-30))
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(i*4,0,-40))
			
			for i in range(10,14):	
				self.block = breve.createInstances( breve.BraitenbergSound,1)
				self.block.move( breve.vector(i*4,0,-40))
						elif self.scenario == 'eight':
			self.vehicle.move(breve.vector(2,1,10))
			self.vehicle.rotate(breve.vector(0,1,0),-0.05)
			
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(2,1,15))
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(-18,1,15))
			
			
		elif self.scenario == 'Maze':
			
			filename = "maze.txt"
			f = open(filename, "r")
		
			#Reads the limits of the maze.
		
			#Reads the maze itself.
			text = f.readlines()

			#Iterates over the lines.
			for i in xrange(len(text)):
				for t in xrange(len(text[i])):
					if (text[i][t] == "o"):
						self.obj = breve.createInstances ( breve.BraitenbergSound, 1)
						self.obj.move( breve.vector(i*3, 0, t*2))  
					elif (text[i][t] == "*"):
						self.block = breve.createInstances ( breve.BraitenbergBlock, 1)
						self.block.move( breve.vector(i*3, 0, t*2))
			
		elif self.scenario == 'Attraction':
			breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector(14 , 1, 17))
			breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector(16 , 1, 21))
			breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector(20, 1, 27))
					elif self.scenario == 'None':
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector(20 , 1, 4))
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector( 20, 1, 17))

		
		'''Creates the first vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		self.vehicle.move(breve.vector(30,1,5))
		
		'''Adds wheels and sensors.'''
		lWheel = self.vehicle.addWheel (breve.vector( -0.5, 0, -1.5 ))
		rWheel = self.vehicle.addWheel (breve.vector( -0.5, 0, 1.5 ))
		self.vehicle.addSense (breve.vector( 0, 0.7, 0 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "Light")
		lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57000000, "linear", -100, 100)
		rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "linear", -100, 100)
		
		backOlfactionSensor = self.vehicle.addSensor (breve.vector( -2.2, 0.1, 0 ),breve.vector( 0, 0, 1 ),  -1.57000000, "linear", -100, 100)
		
		
		lBlockSensor = self.vehicle.addBlockSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57000000, "linear", -100, 100)
		rBlockSensor = self.vehicle.addBlockSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "linear", -100, 100)
		
		
		'''WARNING: If we are adding sensor other than block sensors, we have to make the setType.'''
		lFrontSensor.setType("BraitenbergSounds")
		rFrontSensor.setType("BraitenbergSounds")
		backOlfactionSensor.setType("BraitenbergOlfactions")
		
		'''Links the sensors to the wheels.'''
		lFrontSensor.link(lWheel)
		rFrontSensor.link(rWheel)
		backOlfactionSensor.link(lWheel)
		backOlfactionSensor.link(rWheel)

		'''Block sensors.'''
		lBlockSensor.link(rWheel)
		rBlockSensor.link(lWheel)
		
		#lBlockSensor.activationObject.setGauss(0.001,0)
		#rBlockSensor.activationObject.setGauss(0.001,0)

		
		lWheel.setNaturalVelocity(1.00000)
		rWheel.setNaturalVelocity(1.00000)
		
		lFrontSensor.setBias(10)
		rFrontSensor.setBias(10)
		lBlockSensor.setBias(5)
		rBlockSensor.setBias(5)
		backOlfactionSensor.setBias(7)
				
		'''Creates the second vehicle.'''
		monsterOne = breve.createInstances( breve.BraitenbergVehicle, 1 )
		monsterOne.move(breve.vector(20,1,5))
		
		'''Adds wheels and sensors.'''
		lWheel = monsterOne.addWheel (breve.vector( -0.5, 0, -1.5 ))
		rWheel = monsterOne.addWheel (breve.vector( -0.5, 0, 1.5 ))
		monsterOne.addSense (breve.vector( 0, 0.7, 0 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "Olfaction")
		lFrontSensor = monsterOne.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57000000, "linear", -100, 100)
		rFrontSensor = monsterOne.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "linear", -100, 100)
		
		lLightSensor = monsterOne.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57000000, "linear", -100, 100)
		rLightSensor = monsterOne.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "linear", -100, 100)
		
		
		'''WARNING: If we are adding sensor other than block sensors, we have to make the setType.'''
		lFrontSensor.setType("BraitenbergSounds")
		rFrontSensor.setType("BraitenbergSounds")
		lLightSensor.setType("BraitenbergLights")
		rLightSensor.setType("BraitenbergLights")
		
		'''Links the sensors to the wheels.'''
		lFrontSensor.link(lWheel)
		rFrontSensor.link(rWheel)
		
		'''Block sensors.'''
		lLightSensor.link(rWheel)
		rLightSensor.link(lWheel)
		
		#lBlockSensor.activationObject.setGauss(0.001,0)
		#rBlockSensor.activationObject.setGauss(0.001,0)

		
		lWheel.setNaturalVelocity(1.00000)
		rWheel.setNaturalVelocity(1.00000)
		
		lFrontSensor.setBias(10)
		rFrontSensor.setBias(10)
		lLightSensor.setBias(5)
		rLightSensor.setBias(5)

breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
