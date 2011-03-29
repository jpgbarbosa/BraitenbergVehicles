
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


import breve
import random

from math import *

isPacman = 1

class BraitenbergControl( breve.PhysicalControl ):
	'''This class is used for building simple Braitenberg vehicle  simulations.  To create a Braitenberg vehicle simulation,  subclass BraitenbergControl and use the init method to  create OBJECT(BraitenbergLight) and  OBJECT(BraitenbergVehicle) objects.'''

	def __init__( self ):
		breve.PhysicalControl.__init__( self )
		self.cloudTexture = None
		self.floor = None
		BraitenbergControl.init( self )

	def init( self ):
		self.enableLighting()
		self.enableSmoothDrawing()
		self.floor = breve.createInstances( breve.Floor, 1 )
		self.pointCamera( breve.vector( 0, 0, 0 ), breve.vector( 3, 3, 24 ) )
		#self.enableShadows()
		self.disableShadowVolumes()
		#self.enableReflections()
		self.cloudTexture = breve.createInstances( breve.Image, 1 ).load( 'images/clouds.png' )
		self.PacmanMusic =  breve.createInstances( breve.Sound, 1 ).load( 'sounds/Pacman/opening song.wav' )
		self.PacmanMusic.play(1)
		self.setBackgroundColor( breve.vector( 0.400000, 0.600000, 0.900000 ) )
		self.setBackgroundTextureImage( self.cloudTexture )


breve.BraitenbergControl = BraitenbergControl
class BraitenbergVehicle( breve.MultiBody ):
	'''This object is used in conjunction with OBJECT(BraitenbergControl) to create simple Braitenberg vehicles.'''

	def __init__( self ):
		breve.MultiBody.__init__( self )
		self.bodyLink = None
		self.bodyShape = None
		self.sensorShape = None
		self.sensors = breve.objectList()
		self.wheelShape = None
		self.wheels = breve.objectList()
		self.wheelsList = [ ]
		self.sensorsList = [ ]
		BraitenbergVehicle.init( self )
		self.radius = 0.6

	def addSensor( self, location , axis, angle, viewAngle, type, function, name = "Sensor"):
		'''Adds a sensor at location on the vehicle.  This method returns the sensor which is created, a OBJECT(BraitenbergLightSensor).  You'll use the returned object to connect it to the vehicle's wheels.'''

		'''This sensor can interact with light, smell and sound. The final type of the sensor is defined by a method of the sensor itself.'''
		joint = None
		sensor = None

		sensor = breve.createInstances( breve.BraitenbergSensor, 1 )
		sensor.setShape( self.sensorShape )
		
		activationFunction = breve.createInstances(breve.BraitenbergActivationObject, 1)
		activationFunction.setType(function)
		sensor.setActivationObject( activationFunction )
		sensor.activationObject.setName( name)
		
		'''Sets the angle of the sensor'''
		sensor.setSensorAngle(viewAngle)
		
		joint = breve.createInstances( breve.FixedJoint, 1 )
		joint.setRelativeRotation( axis, angle )
			
		joint.link( location, breve.vector( 0, 0, 0 ), sensor, self.bodyLink )
		joint.setDoubleSpring( 300, 0.010000, -0.010000 )
		self.addDependency( joint )
		self.addDependency( sensor )
		
		sensor.setType(type)
			
		self.sensors.append( sensor )
		self.sensorsList.append( sensor )
		return sensor
		
	def addSense( self, location , axis, angle, type):
		'''Adds a sensor at location on the vehicle.  This method returns the sensor which is created, a OBJECT(BraitenbergLightSensor).  You'll use the returned object to connect it to the vehicle's wheels.'''

		'''This sensor can interact with light, smell and sound. The final type of the sensor is defined by a method of the sensor itself.'''
		joint = None
		sense = None

		if type == "Light":
			sense = breve.createInstances( breve.BraitenbergLight, 1 )
		elif type == "Olfaction":
			sense = breve.createInstances( breve.BraitenbergOlfaction, 1 )
		elif type == "Block":
			sense = breve.createInstances( breve.BraitenbergBlock, 1 )
		
		joint = breve.createInstances( breve.FixedJoint, 1 )
		joint.setRelativeRotation( axis, angle )
			
		joint.link( location, breve.vector( 0, 0, 0 ), sense, self.bodyLink )
		joint.setDoubleSpring( 300, 0.010000, -0.010000 )
		self.addDependency( joint )
		self.addDependency( sense )
		self.sensors.append( sense )
		return sense
		
	def addBlockSensor( self, location , axis, ang, viewAngle, function, name = "BlockSensor"):
		'''Adds a sensor at location on the vehicle.  This method returns the sensor which is created, a OBJECT(BraitenbergSensor).  You'll use the returned object to connect it to the vehicle's wheels.'''

		''' This sensor only interacts  with blocks. '''
		joint = None
		sensor = None

		sensor = breve.createInstances( breve.BraitenbergBlockSensor, 1 )
		sensor.setShape( self.sensorShape )
		
		activationFunction = breve.createInstances(breve.BraitenbergActivationObject, 1)
		activationFunction.setType(function)
		sensor.setActivationObject( activationFunction )
		sensor.activationObject.setName( name)
		
		'''Sets the angle of the sensor'''
		sensor.setSensorAngle(viewAngle)
		
		joint = breve.createInstances( breve.FixedJoint, 1 )
		joint.setRelativeRotation( axis, ang )
			
		joint.link( location, breve.vector( 0, 0, 0 ), sensor, self.bodyLink )
		joint.setDoubleSpring( 300, 0.010000, -0.010000 )
		self.addDependency( joint )
		self.addDependency( sensor )
		sensor.setColor( breve.vector( 0, 0, 0 ) )
		self.sensors.append( sensor )
		return sensor

	def addWheel( self, location ):
		'''Adds a wheel at location on the vehicle.  This method returns the wheel which is created, a OBJECT(BraitenbergWheel).  You'll use the returned object to connect it to the vehicle's sensors.'''

		joint = None
		wheel = None

		wheel = breve.createInstances( breve.BraitenbergWheel, 1 )
		wheel.setShape( self.wheelShape )
		joint = breve.createInstances( breve.RevoluteJoint, 1 )
		joint.setRelativeRotation( breve.vector( 1, 0, 0 ), 1.570800 )
		joint.link( breve.vector( 0, 0, 1 ), location, breve.vector( 0, 0, 0 ), wheel, self.bodyLink )
		wheel.setET( 0.800000 )
		wheel.setJoint( joint )
		joint.setStrengthLimit( ( joint.getStrengthHardLimit() / 2 ) )
		#wheel.setColor( breve.vector( 0.600000, 0.600000, 0.600000 ) )
		wheel.setColor( breve.vector( 1, 0, 0 ) )
		wheel.setMu( 100000 )
		self.addDependency( joint )
		self.addDependency( wheel )
		self.wheels.append( wheel )
		self.wheelsList.append (wheel)
		return wheel

	def destroy( self ):
		breve.deleteInstances( self.sensorShape )
		breve.deleteInstances( self.wheelShape )
		breve.deleteInstances( self.bodyShape )
		breve.MultiBody.destroy( self )

	def getDensity( self ):
		return 1.000000

	def getWheelRadius( self ):
		return self.radius
	
	def setWheelRadius(self, rad):
		self.radius = rad
		self.wheelShape.initWithPolygonDisk( 40, self.getWheelWidth(), self.getWheelRadius() )

	def getWheelWidth( self ):
		return 0.100000

	def init( self ):
		self.radius = 0.6
		self.bodyShape = breve.createInstances( breve.Shape, 1 )
		self.bodyShape.initWithCube( breve.vector( 4.000000, 0.750000, 3.000000 ) )
		self.wheelShape = breve.createInstances( breve.Shape, 1 )
		self.wheelShape.initWithPolygonDisk( 40, self.getWheelWidth(), self.getWheelRadius() )
		self.sensorShape = breve.createInstances( breve.Shape, 1 )
		self.sensorShape.initWithPolygonCone( 10, 0.500000, 0.200000 )
		self.bodyShape.setDensity( self.getDensity() )
		self.bodyLink = breve.createInstances( breve.Link, 1 )
		self.bodyLink.setShape( self.bodyShape )
		self.bodyLink.setMu( -1.000000 )
		self.bodyLink.setET( 0.800000 )
		self.setRoot( self.bodyLink )
		self.move( breve.vector( 0, 0.900000, 0 ) )
		self.setTextureScale( 0.500000 )
		
		'''The colour of the car.'''
		self.bodyLink.setColor( breve.vector( 0, 0, 0 ) )


breve.BraitenbergVehicle = BraitenbergVehicle

class BraitenbergTwoWheelsVehicle( breve.BraitenbergVehicle ):
	'''This is the OBJECT(BraitenbergVehicle) configuration that will make the elipse around two scenario objects.'''
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
	
		'''Adds wheels and sensors.'''
		self.lWheel = self.addWheel (breve.vector( -0.5, 0, -1.5 ))
		self.rWheel = self.addWheel (breve.vector( -0.5, 0, 1.5 ))
		#self.addSense (breve.vector( 0, 0.7, 0 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "Light")
		self.lFrontSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57000000, 1.6, "BraitenbergOlfactions", "linear")
		self.rFrontSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57000000, 1.6, "BraitenbergOlfactions", "linear")

		self.lBlockSensor = self.addBlockSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57000000, 1.6, "linear")
		self.rBlockSensor = self.addBlockSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57000000, 1.6, "linear")
		
		'''Links the sensors to the wheels.'''
		self.lFrontSensor.link(self.lWheel)
		self.rFrontSensor.link(self.rWheel)

		'''Block sensors.'''
		self.lBlockSensor.link(self.rWheel)
		self.rBlockSensor.link(self.lWheel)
		
		#self.lBlockSensor.activationObject.setGauss(0.001,0)
		#self.rBlockSensor.activationObject.setGauss(0.001,0)

		
		self.lWheel.setNaturalVelocity(1.00000)
		self.rWheel.setNaturalVelocity(1.00000)
		
		self.lFrontSensor.setBias(10)
		self.rFrontSensor.setBias(10)
		self.lBlockSensor.setBias(5)
		self.rBlockSensor.setBias(5)
			
breve.BraitenbergTwoWheelsVehicle = BraitenbergTwoWheelsVehicle

class BraitenbergPacman( breve. BraitenbergVehicle ):
	'''This is the OBJECT(BraitenbergVehicle) configuration for our Pacman!'''
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
		
		'''Adds wheels and sensors.'''
		self.lWheel = self.addWheel (breve.vector( -0.5, 0, -1.5 ))
		self.rWheel = self.addWheel (breve.vector( -0.5, 0, 1.5 ))
		sense = self.addSense (breve.vector( 0, 1.0, 0 ),breve.vector( -0.5, 0, 1 ),  1.57000000, "Light")
		self.lTrackSensor = self.addSensor (breve.vector( 2.2, 0.1, -2 ), breve.vector( 0, 0, 1 ), 1.57, 3.1, "BraitenbergSounds", "linear", "SoundLeft")
		self.rTrackSensor = self.addSensor (breve.vector( 2.2, 0.1, 2 ),breve.vector( 0, 0, 1 ),  1.57, 3.1, "BraitenbergSounds", "linear", "SoundRight")
		self.lLimitsSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0, 0, 1 ), 1.57, 3.1, "BraitenbergLights", "linear")
		self.rLimitsSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( 0, 0, 1 ),  1.57, 3.1, "BraitenbergLights", "linear")

		self.lMonsterSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0, 0, 1 ), 1.57, 0.8, "BraitenbergOlfactions", "gaussian", "MonsterSensorLeft")
		self.rMonsterSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( 0, 0, 1 ),  1.57, 0.8, "BraitenbergOlfactions", "gaussian", "MonsterSensorRight")
		
		
		'''Associates the sensors with the sense that constitutes the body of the Pacman.'''
		sense.setLeftSensor(self.lTrackSensor)
		sense.setRightSensor(self.rTrackSensor)
		
		'''"Hides" the body of the vehicle.'''
		self.bodyLink.setTransparency(0)
		for i in xrange(len(self.wheelsList)):
			self.wheelsList[i].setTransparency(0)
		for i in xrange(len(self.sensorsList)):
			self.sensorsList[i].setTransparency(0)
		
		'''Links the sensors to the wheels.'''
		self.lTrackSensor.link(self.rWheel)
		self.rTrackSensor.link(self.lWheel)

		'''Block sensors.'''
		self.lMonsterSensor.link(self.lWheel)
		self.rMonsterSensor.link(self.lWheel)
		
		self.lMonsterSensor.activationObject.setGauss(0.001,0.02)
		self.rMonsterSensor.activationObject.setGauss(0.001,0.02)
		self.lMonsterSensor.activationObject.setLeftBound(0.001)
		self.rMonsterSensor.activationObject.setLeftBound(0.001)
		
		self.lWheel.setNaturalVelocity(1)
		self.rWheel.setNaturalVelocity(1)
		
		self.lTrackSensor.setBias(5)
		self.rTrackSensor.setBias(5)
		self.lLimitsSensor.setBias(-1)
		self.rLimitsSensor.setBias(-1)
		self.lMonsterSensor.setBias(10)
		self.rMonsterSensor.setBias(10)
			
breve.BraitenbergTwoWheelsVehicle = BraitenbergTwoWheelsVehicle

class BraitenbergMonster( breve.BraitenbergVehicle ):
	'''This is the OBJECT(BraitenbergVehicle) configuration that will chase poor Pacman.'''
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
		
		self.bodyLink.setTransparency(0)
		
		'''Adds wheels and sensors.'''
		self.lWheel = self.addWheel (breve.vector( -0.5, 0, -1.5 ))
		self.rWheel = self.addWheel (breve.vector( -0.5, 0, 1.5 ))
		self.addSense (breve.vector( 0, 1.0, 0 ),breve.vector( 0, 0, 0 ),  1.57000000, "Olfaction")
		
		self.lTrackSensor = self.addSensor (breve.vector( 2.2, 0.1, -2 ), breve.vector( 0, 0, 1 ), 1.57, 3.1, "BraitenbergSounds", "linear")
		self.rTrackSensor = self.addSensor (breve.vector( 2.2, 0.1, 2 ),breve.vector( 0, 0, 1 ),  1.57, 3.1, "BraitenbergSounds", "linear")
		
		self.lLimitsSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 3.1, "BraitenbergLights", "linear")
		self.rLimitsSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 3.1, "BraitenbergLights", "linear")
		
		self.lPacmanSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergLights", "log", "PacmanLeft")
		self.rPacmanSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergLights", "log", "PacmanRight")

		'''"Hides" the body of the vehicle.'''
		self.bodyLink.setTransparency(0)
		for i in xrange(len(self.wheelsList)):
			self.wheelsList[i].setTransparency(0)
		for i in xrange(len(self.sensorsList)):
			self.sensorsList[i].setTransparency(0)
		
		
		'''Links the sensors to the wheels.'''
		self.lTrackSensor.link(self.rWheel)
		self.rTrackSensor.link(self.lWheel)
		
		self.lTrackSensor.link(self.rWheel)
		self.rTrackSensor.link(self.lWheel)
		
		self.lPacmanSensor.link(self.rWheel)
		self.rPacmanSensor.link(self.lWheel)
		
		self.lWheel.setNaturalVelocity(0.7)
		self.rWheel.setNaturalVelocity(0.7)
	
		self.lTrackSensor.setBias(3)
		self.rTrackSensor.setBias(3)
		self.lPacmanSensor.setBias(1)
		self.rPacmanSensor.setBias(1)
		
			
breve.BraitenbergMonster = BraitenbergMonster


class Braitenberg3c( breve.BraitenbergVehicle ):
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
		
		'''Adds wheels and sensors.'''
		self.lWheel = self.addWheel (breve.vector( -0.5, 0, -1.5 ))
		self.rWheel = self.addWheel (breve.vector( -0.5, 0, 1.5 ))
		
		'''Creates all the types of sensors that it needs.'''
		self.lSoundSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergSounds", "linear")
		self.rSoundSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergSounds", "linear")
		self.lLightSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergLights", "linear")
		self.rLightSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergLights", "linear")
		self.lOlfactionSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergOlfactions", "linear")
		self.rOlfactionSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergOlfactions", "linear")
		self.lBlockSensor = self.addBlockSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "linear")
		self.rBlockSensor = self.addBlockSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "linear")
		
		'''Links the sensors to the wheels.'''
		self.lSoundSensor.link(self.lWheel)
		self.rSoundSensor.link(self.rWheel)
		self.lLightSensor.link(self.rWheel)
		self.rLightSensor.link(self.lWheel)
		self.lOlfactionSensor.link(self.rWheel)
		self.rOlfactionSensor.link(self.lWheel)
		'''Block sensors.'''
		self.lBlockSensor.link(self.rWheel)
		self.rBlockSensor.link(self.lWheel)
		
		self.lWheel.setNaturalVelocity(3.00000)
		self.rWheel.setNaturalVelocity(3.00000)
	
		self.lSoundSensor.setBias(15)
		self.rSoundSensor.setBias(15)
		self.lLightSensor.setBias(-10)
		self.rLightSensor.setBias(-10)
		self.lOlfactionSensor.setBias(5)
		self.rOlfactionSensor.setBias(5)
		'''Block sensors.'''
		self.lBlockSensor.setBias(-5)
		self.rBlockSensor.setBias(-5)
			
breve.Braitenberg3c = Braitenberg3c

class BraitenbergExplorer( breve.BraitenbergVehicle ):
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
		
		'''Adds wheels and sensors.'''
		self.lWheel = self.addWheel (breve.vector( -0.5, 0, -1.5 ))
		self.rWheel = self.addWheel (breve.vector( -0.5, 0, 1.5 ))
		
		'''Creates all the types of sensors that it needs.'''
		self.lSoundSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergSounds", "linear")
		self.rSoundSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergSounds", "linear")
		self.lLightSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergLights", "gaussian")
		self.rLightSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergLights", "gaussian")
		self.lOlfactionSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "BraitenbergOlfactions", "linear")
		self.rOlfactionSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "BraitenbergOlfactions", "linear")
		self.lBlockSensor = self.addBlockSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.5, 0, 1 ), 1.57, 1.6, "linear")
		self.rBlockSensor = self.addBlockSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.5, 0, 1 ),  1.57, 1.6, "linear")
		
		self.lLightSensor.activationObject.setGauss(1,0.02)
		self.rLightSensor.activationObject.setGauss(1,0.02)
		
		'''Links the sensors to the wheels.'''
		self.lSoundSensor.link(self.lWheel)
		self.rSoundSensor.link(self.rWheel)
		self.lLightSensor.link(self.rWheel)
		self.rLightSensor.link(self.lWheel)
		self.lOlfactionSensor.link(self.rWheel)
		self.rOlfactionSensor.link(self.lWheel)
		'''Block sensors.'''
		self.lBlockSensor.link(self.rWheel)
		self.rBlockSensor.link(self.lWheel)
		
		self.lWheel.setNaturalVelocity(0)
		self.rWheel.setNaturalVelocity(0)
	
		self.lSoundSensor.setBias(5)
		self.rSoundSensor.setBias(5)
		self.lLightSensor.setBias(5)
		self.rLightSensor.setBias(5)
		self.lOlfactionSensor.setBias(5)
		self.rOlfactionSensor.setBias(5)
		'''Block sensors.'''
		self.lBlockSensor.setBias(5)
		self.rBlockSensor.setBias(5)
			
breve.BraitenbergExplorer = BraitenbergExplorer

class BraitenbergElipser( breve.BraitenbergVehicle ):
	'''This is the OBJECT(BraitenbergVehicle) configuration that will make the elipse around two scenario objects.'''
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
	
		sPos = 1

		med = 0.03
		dpad = 0.3
		
		naturalVel = 0.5
		bias = 0.03 
	
		'''Adds wheels and sensors.'''
		self.setWheelRadius(0.9)
		
		self.lWheel = self.addWheel (breve.vector( -0.8, 0, -1.5 ))
		
		self.rWheel = self.addWheel (breve.vector( -0.8, 0, 1.5 ))
		
		#Correct values
		self.lFrontSensor = self.addSensor (breve.vector( 2.2, 0.1, -1.2 ), breve.vector( sPos, 0, 1 ), 1.57000000, 1.6,"BraitenbergSounds", "gaussian")
		self.rFrontSensor = self.addSensor (breve.vector( 2.2, 0.1, 1.2 ),breve.vector( -sPos, 0, 1 ),  1.57000000, 1.6,"BraitenbergSounds", "gaussian")
		
		self.lFrontSensor.activationObject.setGauss(dpad,med)
		#self.lFrontSensor.activationObject.setLeftBound(0.2)
		self.lFrontSensor.activationObject.setLowerBound(0)
		self.rFrontSensor.activationObject.setGauss(dpad,med)
		#self.rFrontSensor.activationObject.setLeftBound(0.2)
		self.rFrontSensor.activationObject.setLowerBound(0)
		
		'''Links the sensors to the wheels.'''
		self.lFrontSensor.link(self.rWheel)
		self.rFrontSensor.link(self.lWheel)

		#Correct values
		self.lWheel.setNaturalVelocity(naturalVel)
		self.rWheel.setNaturalVelocity(naturalVel)
		
		#Correct values
		self.lFrontSensor.setBias(bias)
		self.rFrontSensor.setBias(bias)
			
			
breve.BraitenbergElipser = BraitenbergElipser

class BraitenbergEightMaker( breve.BraitenbergVehicle ):
	'''This is the OBJECT(BraitenbergVehicle) configuration that will make the elipse around two scenario objects.'''
	def __init__( self ):
		breve.BraitenbergVehicle.__init__(self)
	
		'''Adds wheels and sensors.'''
		self.lWheel = self.addWheel (breve.vector( 0, 0, -1.5 ))
		self.rWheel = self.addWheel (breve.vector( 0, 0, 1.5 ))

		lB = 0
		uB = 0.03
		vel = 1
		rightBound = 0.08

		#Correct values
		self.lFrontSensor = self.addSensor (breve.vector(1.8, 0.1, -1.8),breve.vector( 1, 0, 0 ),1.57, 1.6, "BraitenbergSounds", "linear")
		self.rFrontSensor = self.addSensor (breve.vector(1.8, 0.1, 1.8),breve.vector( -1, 0, 0 ),1.57, 1.6, "BraitenbergSounds", "linear")
		
		'''Links the sensors to the wheels.'''
		self.lFrontSensor.link(self.rWheel)
		self.rFrontSensor.link(self.lWheel)

		self.lFrontSensor.activationObject.setRightBound(rightBound);
		self.rFrontSensor.activationObject.setRightBound(rightBound);
		self.lFrontSensor.activationObject.setLowerBound(lB)
		self.rFrontSensor.activationObject.setLowerBound(lB)
		self.rFrontSensor.activationObject.setUpperBound(uB)
		self.lFrontSensor.activationObject.setUpperBound(uB)
	
		#Correct values
		self.lWheel.setNaturalVelocity(vel)
		self.rWheel.setNaturalVelocity(vel)
			
breve.BraitenbergEightMaker = BraitenbergEightMaker
	
class BraitenbergHeavyVehicle( breve.BraitenbergVehicle ):
	'''A heavy duty version of OBJECT(BraitenbergVehicle), this vehicle is heavier and harder to control, but more stable at higher  speeds.'''

	def __init__( self ):
		breve.BraitenbergVehicle.__init__( self )

	def getDensity( self ):
		return 20.000000

	def getWheelRadius( self ):
		return 0.800000

	def getWheelWidth( self ):
		return 0.400000


breve.BraitenbergHeavyVehicle = BraitenbergHeavyVehicle
class BraitenbergLight( breve.Link):
	'''A BraitenbergLight is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Link.__init__( self )
		self.intensity = 1
		self.joint = None
		self.shape = None
		'''These two variables are used so when a monster catches the Pacman, it will put high bias in the wheels,
		   but one negative and the other positive. This way, the Pacman will jump and get out of the scenario!'''
		self.lSensor = None
		self.rSensor = None
		self.pacmanTexture = None
		BraitenbergLight.init( self )

	def init( self ):
		
		if isPacman:
			self.shape = breve.createInstances( breve.Shape, 1 ).initWithSphere( 1.50000 )
			self.shape.setDensity(0.00000000000000001)
			self.setShape( self.shape )
			self.setColor( breve.vector( 1, 1, 0 ) )
			self.pacmanTexture = breve.createInstances( breve.Image, 1 ).load( 'images/pacman.png' )
			self.setTextureImage( self.pacmanTexture )
			self.setTextureScale( 1.5000 )
		else:
			#self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.300000 ) )
			#self.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector(2.5,5,2.5) ) )
			self.setShape( breve.createInstances( breve.Shape, 1 ).initWithPolygonCone( 10,2, 2 ) )
			self.setColor( breve.vector( 1, 0, 0 ) )
		
	def getIntensity( self ):
		return self.intensity
		
	def setIntensity( self, itense ):
		self.intensity = itense
		
	def setLeftSensor ( self, s ):
		self.lSensor = s
	
	def setRightSensor ( self, s ):
		self.rSensor = s
		
	def setLeftSensorBias ( self, b ):
		self.lSensor.setBias(b)
	
	def setRightSensorBias ( self, b ):
		self.rSensor.setBias(b)


breve.BraitenbergLight = BraitenbergLight


class BraitenbergSound( breve.Mobile ):
	'''A BraitenbergSound is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		self.eaten = 0
		self.intensity = 1
		BraitenbergSound.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.300000 ) )
		if isPacman:
			self.setColor( breve.vector( 1, 1, 0 ) )
		else:
			self.setColor( breve.vector( 1, 0, 0 ) )
		
	def getIntensity( self ):
		return self.intensity
	
	def setIntensity( self, itense ):
		self.intensity = itense
		
	def isEaten ( self ):
		return self.eaten
		
	def setEaten ( self , e):
		self.eaten = e


breve.BraitenbergSound = BraitenbergSound


class BraitenbergOlfaction( breve.Link ):
	'''A BraitenbergOlfaction is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Link.__init__( self )
		self.intensity = 1
		self.joint = None
		self.shape = None
		BraitenbergOlfaction.init( self )

	def init( self ):
		if isPacman:
			self.shape = breve.createInstances( breve.Shape, 1 ).initWithSphere( 1.50000 )
			self.shape.setDensity(0.00000000000000001)
			self.setShape( self.shape )
			self.setColor( breve.vector( 0, 0, 1 ) )
		else:
			self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.30000 ) )
			self.setColor( breve.vector( 0, 0, 1 ) )
		
	def getIntensity( self ):
		return self.intensity
		
	def setIntensity( self, itense ):
		self.intensity = itense


breve.BraitenbergOlfaction = BraitenbergOlfaction

class BraitenbergWheel( breve.Link ):
	'''A BraitenbergWheel is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a wheel to the vehicle. <p> <b>NOTE: this class is included as part of the file "Braitenberg.tz".</b>'''

	def __init__( self ):
		breve.Link.__init__( self )
		self.joint = None
		self.naturalVelocity = 0
		self.newVelocity = 0
		self.oldVelocity = 0
		BraitenbergWheel.init( self )

	def activate( self, n ):
		'''Used internally.'''

		self.newVelocity = ( self.newVelocity + n )

	def init( self ):
		self.naturalVelocity = 0
		self.newVelocity = 0

	def postIterate( self ):
		if ( self.newVelocity > 30 ):
			self.newVelocity = 30

		if ( self.newVelocity == 0 ):
			self.joint.setJointVelocity( self.oldVelocity )
			self.oldVelocity = ( self.oldVelocity * 0.950000 )

		else:
			self.joint.setJointVelocity( self.newVelocity )
			self.oldVelocity = self.newVelocity


		self.newVelocity = self.naturalVelocity

	def setJoint( self, j ):
		'''Used internally.'''

		self.joint = j

	def setNaturalVelocity( self, n ):
		'''Sets the "natural" velocity of this wheel.  The natural velocity is the speed at which the wheel turns in the absence of sensor input.  '''

		self.naturalVelocity = n


breve.BraitenbergWheel = BraitenbergWheel

class BraitenbergMainSensor(breve.Link):

	def __init__( self ):
		breve.Link.__init__( self )
		self.activationObject = None
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.range = 0
		self.sensorType = None
		self.counter = 0
		self.wheels = breve.objectList()
		self.hasPlayed = 0
		self.PacmanEating =  breve.createInstances( breve.Sound, 1 ).load( 'sounds/Pacman/eatingShort.wav' )
		self.PacmanAlert =  breve.createInstances( breve.Sound, 1 ).load( 'sounds/Pacman/siren.wav' )
		self.PacmanCherry = breve.createInstances( breve.Sound, 1 ).load( 'sounds/Pacman/eating cherry.wav' )
		BraitenbergMainSensor.init( self )

	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 3.1

	def link( self, w ):
		'''Associates this sensor with wheel w.'''
		self.wheels.append( w )

	def setActivationObject( self, o ):
		'''This method specifies an activation method for the sensor.  An activation method is a method which takes as input the strength read by the sensor, and as output returns the strength of the  signal which will travel on to the motor. <p> Your activation function should be defined as: <pre> + to <i>activation-function-name</i> with-sensor-strength s (float): </pre> <p> The default activation method is linear, but more complex vehicles may require non-linear activation functions. '''
		self.activationObject = o

	def setBias( self, d ):
		'''Sets the "bias" of this sensor.  The default bias is 1, meaning that the sensor has a positive influence on associated wheels with strength 1.  You can change this to any magnitude, positive or negative.'''
		self.bias = d

	def setSensorAngle( self, n ):
		'''Sets the angle in which this sensor can detect light.  The default value of 1.5 means that the sensor can see most of everything in front of it.  Setting the value to be any higher leads to general wackiness, so I don't suggest it.'''
		self.sensorAngle = n
		
		
breve.BraitenbergMainSensor = BraitenbergMainSensor

class BraitenbergSensor( breve.BraitenbergMainSensor ):
	'''A BraitenbergLightSensor is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a sensor to the vehicle. <p> <b>NOTE: this class is included as part of the file "Braitenberg.tz".</b>'''
	
	'''This method can iterate over objects of type sound, olfaction or light.'''
	def iterate( self ):
		i = None
		lights = 0
		angle = 0
		strength = 0
		total = 0
		transDir = breve.vector()
		toLight = breve.vector()
		
		

		transDir = ( self.getRotation() * self.direction )
		'''It's by the sensorType string that we distinguish between a sound, olfaction or light sensor. '''
		for i in breve.allInstances( self.sensorType ):
			toLight = ( i.getLocation() - self.getLocation() )
			angle = breve.breveInternalFunctionFinder.angle( self, toLight, transDir )
			if ( angle < self.sensorAngle ):
				strength = breve.length( ( self.getLocation() - i.getLocation() ))
				
				'''The monster is getting closer.'''
				if self.activationObject.getName() == "MonsterSensorLeft" and breve.length(self.getLocation() - i.getLocation()) < 25 and not self.hasPlayed:
					self.PacmanAlert.play(1)
					self.hasPlayed = 1
					
				if self.activationObject.getName() == "PacmanLeft" or self.activationObject.getName() == "PacmanRight":
					if  breve.length(self.getLocation() - i.getLocation()) < 4 :
						i.setLeftSensorBias(-700)
						i.setRightSensorBias(700)
				
				'''We turn invisible the items as we pass by.'''
				if (self.activationObject.getName() == "SoundLeft" or self.activationObject.getName() == "SoundRight") and breve.length(self.getLocation() - i.getLocation()) < 2.5:
					
					if not i.isEaten():
						i.setTransparency(0)
						i.setEaten(1)
						if self.counter % 10 != 0:
							self.PacmanEating.play(1)
						else:
							self.PacmanCherry.play(1)
						self.counter += 1
						
						'''This means we played the sirene at least once.'''
						if self.hasPlayed:
							self.hasPlayed = (self.hasPlayed + 1 ) % 5
						#print str(self.counter)
				
				'''Avoid by zero exceptions.'''
				if (strength * strength > 0.0):
					strength = ( 1.000000 / ( strength * strength ) )* i.getIntensity()
					if ( self.activationObject ):
						strength = self.activationObject.activate(strength)

					if ( strength > 10 ):
						strength = 10

					total = ( total + strength )
					lights = ( lights + 1 )

		if ( lights != 0 ):
			total = ( total / lights )

		total = ( ( 50 * total ) * self.bias )
		self.wheels.activate( total )
	
	def setType( self , type ):
		self.sensorType = type
		
		if type == "BraitenbergLights":
			self.setColor( breve.vector( 1, 0, 0 ) )
		elif type == "BraitenbergSounds":
			self.setColor( breve.vector( 1, 1, 0 ) )
		elif type == "BraitenbergOlfactions":
			self.setColor( breve.vector( 0, 0, 1 ) )
			
		
		
breve.BraitenbergSensor = BraitenbergSensor


class BraitenbergBlockSensor( breve.BraitenbergMainSensor ):
	'''A BraitenbergBlockSensor is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a sensor to the vehicle. <p> <b>NOTE: this class is included as part of the file "Braitenberg.tz".</b>'''

	def iterate( self ):
		'''Calculates the signal strength according to the closest source that it finds within the it's range.'''
		i = None
		objects = 0
		angle = 0
		strength = 0
		total = 0
		transDir = breve.vector()
		dist = breve.vector()

		minDist=None
		
		transDir = ( self.getRotation() * self.direction )
		'''Only detects blocks.'''
		for i in breve.allInstances( "BraitenbergBlocks" ):
			dist = ( i.getLocation() - self.getLocation() )
			angle = breve.breveInternalFunctionFinder.angle( self, dist, transDir )
			'''It's inside the angle and it's closer than any other block analyzed so far.'''
			if angle < self.sensorAngle :
				t = breve.length(self.getLocation() - i.getLocation())
				
				'''Updates the min distance.'''
				if minDist == None or t < minDist:
					minDist = t
					
					strength = breve.length( ( self.getLocation() - i.getLocation() ))
					'''Avoid by zero exceptions.'''
					if (strength * strength > 0.0):
						strength = ( 1.000000 / ( strength * strength ) )* i.getReflection()
						
						if ( self.activationObject ):
							strength = self.activationObject.activate(strength)

						if ( strength > 10 ):
							strength = 10

						total = strength

		total = ( ( 50 * total ) * self.bias )
		self.wheels.activate( total )
	
	def setRange( self, range ):
		pass

breve.BraitenbergBlockSensor = BraitenbergBlockSensor
		
class BraitenbergBlock( breve.Stationary ):
	'''A BraitenbergBlock is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergBlockSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Stationary.__init__( self )
		self.reflection = 1
		BraitenbergBlock.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector(3,1,3) ) )
		#self.setColor( breve.vector( 0, 0,  0) )
		self.rockTexture = breve.createInstances( breve.Image, 1 ).load( 'images/rock.jpg' )
		self.setTextureImage( self.rockTexture )
	
	def getReflection( self ):
		return self.reflection
		
	def setReflection( self, r ):
		self.reflection = r

breve.BraitenbergBlock = BraitenbergBlock	

class BraitenbergActivationObject( breve.Abstract ):
	'''This class describes the type of activation function.'''
	
	def __init__( self ):
		breve.Abstract.__init__( self )
		self.type = None
		self.name = None
		self.lowerBound = 0
		self.upperBound = () #infinte by default
		self.leftBound = 0
		self.rightBound = () #infinte by default
		
		#Log parameters
		self.base = 2
		
		#Gaussian parameters
		self.gaussDev = 1
		self.gaussMed = 0
	
	def setType (self, type):
		self.type = type
		
	def activate(self, s):
		'''strength will be the returning value.'''
		#if self.name != "Sensor":
		#	print self.name + " begin: " + str(s)
		
		''' Adjust s according left and right bounds.'''
		if s < self.leftBound or s > self.rightBound:
			strength = 0
		else:
			'''Adequates the input s to a given funcation.'''
			if self.type == "linear":
				strength = s
			elif self.type == "gaussian":
				strength = self.gaussian(s,self.gaussDev,self.gaussMed)
			elif self.type == "exponential":
				strength = exp(s)
			elif self.type == "log":
				strength = log(self.base, s)
			else:
				strength = s
					
			
		'''Adjust the output according to the lower and upper bounds.'''
		if strength < self.lowerBound:
			strength = self.lowerBound
		elif strength > self.upperBound:
			strength = self.upperBound
			
		#if self.name != "Sensor":
		#	print self.name + " final: " + str(strength)
		return strength
	
	
	def gaussian(self, x, dev, med=0):
		return (1/(sqrt(2*pi)*dev))*exp(-(x-med)**2/2*(dev**2))
		
	def setGauss(self, dev, med =0):
		self.gaussDev = dev
		self.gaussMov = med
	
	def setExp(self, exp):
		self.exponent = exp
	
	
	def setLogBase(self, base):
		self.type = type
	
		
	def setLowerBound(self, bound):
		self.lowerBound = bound
		
	def setUpperBound(self, bound):
		self.upperBound = bound
	
	def setLeftBound(self, bound):
		self.leftBound = bound
	
	def setRightBound(self, bound):
		self.rightBound = bound

	def getName(self):
		return self.name
	
	def setName ( self, n):
		'''To distinguish sensors.'''
		self.name = n
	
	
breve.BraitenbergActivationObject = BraitenbergActivationObject

# Add our newly created classes to the breve namespace

breve.BraitenbergVehicles = BraitenbergVehicle
breve.BraitenbergHeavyVehicles = BraitenbergHeavyVehicle
breve.BraitenbergLights = BraitenbergLight
breve.BraitenbergSounds = BraitenbergSound
breve.BraitenbergOlfactions = BraitenbergOlfaction
breve.BraitenbergBlocks = BraitenbergBlock
breve.BraitenbergWheels = BraitenbergWheel
breve.BraitenbergSensors = BraitenbergSensor



