
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
			rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.75, 0, 1 ),  -1.57000000, "BraitenbergSounds", "gaussian")
			
			lFrontSensor.activationObject.setGauss(0.01,0)
			rFrontSensor.activationObject.setGauss(0.01,0)
			
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
			self.vehicle.move(breve.vector(-1,1,10))
			self.vehicle.rotate(breve.vector(0,1,0),4.0)
			
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(0.7999,1,15))
			self.block.setIntensity(1.5)
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(-18,1,15))
			self.block.setIntensity(1.5)
		
		
			'''Adds wheels and sensors.'''
			lWheel = self.vehicle.addWheel (breve.vector( 0, 0, -1.5 ))
			rWheel = self.vehicle.addWheel (breve.vector( 0, 0, 1.5 ))
			
			uB = ()
			vel = 0
			bias = 0.04
			#Inicial
			#med = 0.0486007489682
			#dpad = 0.01
			med = 0.0486007489682
			dpad = 0.01

			#Correct values
			lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.3, 0, 1 ),1.570000000, "BraitenbergSounds", "gaussian",-100,uB)
			rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.3, 0, 1 ),  1.570000000, "BraitenbergSounds", "gaussian",-100,uB)
			
			lFrontSensor.activationObject.setGauss(dpad,med)
			rFrontSensor.activationObject.setGauss(dpad,med)
			
			'''Links the sensors to the wheels.'''
			lFrontSensor.link(rWheel)
			rFrontSensor.link(lWheel)
	
			#Correct values
			lWheel.setNaturalVelocity(vel)
			rWheel.setNaturalVelocity(vel)
			
			#Correct values
			lFrontSensor.setBias(bias)
			rFrontSensor.setBias(bias)

		elif self.scenario == 'Eight2':
			self.block=breve.createInstances( breve.BraitenbergSound , 1 )
			self.block.move( breve.vector( -20 ,1 ,0 ))
			self.block.setIntensity(5)
	
			self.block=breve.createInstances( breve.BraitenbergSound , 1 )
			self.block.move( breve.vector( 9 ,1 ,0 ))
			self.block.setIntensity(5)

			self.vehicle.move(breve.vector(-28, 2, 8))

			'''Adds wheels and sensors.'''
			lWheel = self.vehicle.addWheel (breve.vector( 0, 0, -1.5 ))
			rWheel = self.vehicle.addWheel (breve.vector( 0, 0, 1.5 ))
			
			#Correct values
			lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0, 0, 1 ),1.570000000, "BraitenbergSounds", "gaussian",0,())
			rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( 0, 0, 1 ),  1.570000000, "BraitenbergSounds", "gaussian",0,())
			
			med = 0.22
			dev = 0.1
			lB = 0.000002
			rB = 0.0003
			bias = 0.1


			lFrontSensor.activationObject.setGauss(dev,med)
			lFrontSensor.activationObject.setLeftBound(lB)
			lFrontSensor.activationObject.setRightBound(rB)
			lFrontSensor.setSensorAngle(3)
			rFrontSensor.setSensorAngle(3)

			rFrontSensor.activationObject.setGauss(dev,med)
			rFrontSensor.activationObject.setLeftBound(lB)
			rFrontSensor.activationObject.setRightBound(rB)

			lFrontSensor.setBias(bias)
			rFrontSensor.setBias(bias)

			'''Links the sensors to the wheels.'''
			lFrontSensor.link(rWheel)
			rFrontSensor.link(lWheel)
		elif self.scenario == 'Eight3':
			self.block=breve.createInstances( breve.BraitenbergSound , 1 )
			self.block.move( breve.vector( -20 ,1 ,0 ))
			self.block.setIntensity(5)
	
			self.block=breve.createInstances( breve.BraitenbergSound , 1 )
			self.block.move( breve.vector( 10 ,1 ,0 ))
			self.block.setIntensity(5)

			self.vehicle.move(breve.vector(-28, 2, 8))

			'''Adds wheels and sensors.'''
			lWheel = self.vehicle.addWheel (breve.vector( 0, 0, -1.5 ))
			rWheel = self.vehicle.addWheel (breve.vector( 0, 0, 1.5 ))
			
			#Correct values
			lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.9, 0, 1 ),1.570000000, "BraitenbergSounds", "linear",-100,0.0016)
			rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.9, 0, 1 ),  1.570000000, "BraitenbergSounds", "linear",-100,0.0016)
			
			med = 1
			dev = 0.1
			lB = 0.02
			rB = 0.02
			bias = 44
			vel = 5.05
			
			'''
			uB = 10
			vel = 0
			bias = 0.04
			med = 0.005
			dpad = 0.02
			'''

			#Correct values
			lWheel.setNaturalVelocity(vel)
			rWheel.setNaturalVelocity(vel)


			lFrontSensor.activationObject.setGauss(dev,med)
			#lFrontSensor.activationObject.setLeftBound(lB)
			#lFrontSensor.activationObject.setRightBound(rB)

			rFrontSensor.activationObject.setGauss(dev,med)
			#rFrontSensor.activationObject.setLeftBound(lB)
			#rFrontSensor.activationObject.setRightBound(rB)

			lFrontSensor.setBias(bias)
			rFrontSensor.setBias(bias)

			'''Links the sensors to the wheels.'''
			lFrontSensor.link(rWheel)
			rFrontSensor.link(lWheel)




breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
