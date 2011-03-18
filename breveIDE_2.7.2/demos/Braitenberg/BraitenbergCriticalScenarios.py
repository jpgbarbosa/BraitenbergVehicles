
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
		self.scenario = 'Eight'
		self.block = None
		self.obj = None
		
		self.blw = None
		self.brw = None
		
		myBraitenbergControl.init( self )

	def init( self ):
	
		'''Creates the vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		self.vehicle.move(breve.vector(2,1,5))
			
		if self.scenario == 'Elipse':
			self.vehicle.move(breve.vector(2,1,10))
			self.vehicle.rotate(breve.vector(0,1,0),3.14)
			
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(2,1,15))
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(-18,1,15))
		
		
			'''Adds wheels and sensors.'''
			lWheel = self.vehicle.addWheel (breve.vector( 0, 0, -1.5 ))
			rWheel = self.vehicle.addWheel (breve.vector( 0, 0, 1.5 ))
			
			#Correct values
			lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.75, 0, 1 ), 1.57000000, "BraitenbergSounds", "gaussian")
			rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.75, 0, 1 ),  1.57000000, "BraitenbergSounds", "gaussian")
			
			lFrontSensor.activationObject.setGauss(0.01,0.002)
			rFrontSensor.activationObject.setGauss(0.01,0.002)
			
			'''Links the sensors to the wheels.'''
			lFrontSensor.link(rWheel)
			rFrontSensor.link(lWheel)
	
			#Correct values
			lWheel.setNaturalVelocity(1.16)
			rWheel.setNaturalVelocity(1.16)
			
			#Correct values
			lFrontSensor.setBias(0.005)
			rFrontSensor.setBias(0.005)
	
		elif self.scenario == 'Eight':
			self.vehicle.move(breve.vector(0,1,10))
			self.vehicle.rotate(breve.vector(0,1,0),4.14)
			
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(2,1,15))
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(-18,1,15))		
		
		
			'''Adds wheels and sensors.'''
			lWheel = self.vehicle.addWheel (breve.vector( 0, 0, -1.5 ))
			rWheel = self.vehicle.addWheel (breve.vector( 0, 0, 1.5 ))
			
			#Correct values
			lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.3, 0, 1 ),1.570000000, "BraitenbergSounds", "gaussian")
			rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.3, 0, 1 ),  1.570000000, "BraitenbergSounds", "gaussian")
			
			lFrontSensor.activationObject.setGauss(0.01,0.002)
			rFrontSensor.activationObject.setGauss(0.01,0.002)
			
			'''Links the sensors to the wheels.'''
			lFrontSensor.link(rWheel)
			rFrontSensor.link(lWheel)
	
			#Correct values
			lWheel.setNaturalVelocity(0)
			rWheel.setNaturalVelocity(0)
			
			#Correct values
			lFrontSensor.setBias(0.04)
			rFrontSensor.setBias(0.04)



breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
