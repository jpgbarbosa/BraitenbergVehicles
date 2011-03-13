
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.

# Modified by:
# Ivo Daniel Venhuizen Correia, no 2008110814
# João Pedro Gaioso Barbosa, no 200811830
# TP3 and PL1

import breve
import random

from math import *

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
		self.enableShadows()
		self.enableReflections()
		self.cloudTexture = breve.createInstances( breve.Image, 1 ).load( 'images/clouds.png' )
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
		BraitenbergVehicle.init( self )

	def addSensor( self, location , axis, angle, function, lowerBound = -1000, upperBound = 1000):
		'''Adds a sensor at location on the vehicle.  This method returns the sensor which is created, a OBJECT(BraitenbergLightSensor).  You'll use the returned object to connect it to the vehicle's wheels.'''

		'''This sensor can interact with light, smell and sound. The final type of the sensor is defined by a method of the sensor itself.'''
		joint = None
		sensor = None

		sensor = breve.createInstances( breve.BraitenbergSensor, 1 )
		sensor.setShape( self.sensorShape )
		
		activationFunction = breve.createInstances(breve.BraitenbergActivationObject, 1)
		activationFunction.setType(function)
		activationFunction.setLowerBound(lowerBound)
		activationFunction.setUpperBound(upperBound)
		sensor.setActivationObject( activationFunction )
		
		joint = breve.createInstances( breve.RevoluteJoint, 1 )
		joint.setRelativeRotation( axis, angle )
			
		joint.link( breve.vector( 1, 0, 0 ), location, breve.vector( 0, 0, 0 ), sensor, self.bodyLink )
		joint.setDoubleSpring( 300, 0.010000, -0.010000 )
		self.addDependency( joint )
		self.addDependency( sensor )
		sensor.setColor( breve.vector( 0, 0, 0 ) )
		self.sensors.append( sensor )
		return sensor
		
	def addBlockSensor( self, location , axis, ang, function, lowerBound = -1000, upperBound = 1000):
		'''Adds a sensor at location on the vehicle.  This method returns the sensor which is created, a OBJECT(BraitenbergSensor).  You'll use the returned object to connect it to the vehicle's wheels.'''

		''' This sensor only interacts  with blocks. '''
		joint = None
		sensor = None

		sensor = breve.createInstances( breve.BraitenbergBlockSensor, 1 )
		sensor.setShape( self.sensorShape )
		
		activationFunction = breve.createInstances(breve.BraitenbergActivationObject, 1)
		activationFunction.setType(function)
		activationFunction.setLowerBound(lowerBound)
		activationFunction.setUpperBound(upperBound)
		sensor.setActivationObject( activationFunction )
		
		joint = breve.createInstances( breve.RevoluteJoint, 1 )
		joint.setRelativeRotation( axis, ang )
			
		joint.link( breve.vector( 1, 0, 0 ), location, breve.vector( 0, 0, 0 ), sensor, self.bodyLink )
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
		wheel.setColor( breve.vector( 0.600000, 0.600000, 0.600000 ) )
		wheel.setMu( 100000 )
		self.addDependency( joint )
		self.addDependency( wheel )
		self.wheels.append( wheel )
		return wheel

	def destroy( self ):
		breve.deleteInstances( self.sensorShape )
		breve.deleteInstances( self.wheelShape )
		breve.deleteInstances( self.bodyShape )
		breve.MultiBody.destroy( self )

	def getDensity( self ):
		return 1.000000

	def getWheelRadius( self ):
		return 0.600000

	def getWheelWidth( self ):
		return 0.100000

	def init( self ):
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
		self.setTextureScale( 1.500000 )


breve.BraitenbergVehicle = BraitenbergVehicle
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
class BraitenbergLight( breve.Mobile ):
	'''A BraitenbergLight is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergLight.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.300000 ) )
		self.setColor( breve.vector( 1, 0, 0 ) )


breve.BraitenbergLight = BraitenbergLight


class BraitenbergSound( breve.Mobile ):
	'''A BraitenbergSound is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergSound.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.300000 ) )
		self.setColor( breve.vector( 0, 1, 0 ) )


breve.BraitenbergSound = BraitenbergSound


class BraitenbergOlfaction( breve.Mobile ):
	'''A BraitenbergOlfaction is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergOlfaction.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.300000 ) )
		self.setColor( breve.vector( 0, 0, 1 ) )


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
		self.wheels = breve.objectList()
		BraitenbergMainSensor.init( self )

	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.600000

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
				strength = breve.length( ( self.getLocation() - i.getLocation() ) )
				strength = ( 1.000000 / ( strength * strength ) )
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
					
				strength = breve.length( ( self.getLocation() - i.getLocation() ) )
				strength = ( 1.000000 / ( strength * strength ) )

				total = strength

		total = ( ( 50 * total ) * self.bias )
		self.wheels.activate( total )
	
	def setRange( self, range ):
		pass

breve.BraitenbergBlockSensor = BraitenbergBlockSensor
		
class BraitenbergBlock( breve.Link ):
	'''A BraitenbergBlock is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergBlockSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergBlock.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector(3,3,3) ) )
		self.setColor( breve.vector( 10, 0,  0) )


breve.BraitenbergBlock = BraitenbergBlock	

class BraitenbergActivationObject( breve.Abstract ):
	'''This class describes the type of activation function.'''
	
	def __init__( self ):
		breve.Abstract.__init__( self )
		self.type = None
		self.lowerBound = 0
		self.upperBound = 0
	
	def setType (self, type):
		self.type = type
	
	def activate(self, s):
		'''strength will be the returning value.'''
		
		'''Adequates the input s to a given funcation.'''
		if self.type == "linear":
			strength = s
		elif self.type == "gaussian":
			strength = random.gauss(s, 0.1)
		elif self.type == "exponencial":
			strength = s**2
		else:
			strength = s
			
		'''Adjust the output according to the lower and upper bounds.'''
		if strength < self.lowerBound:
			strength = self.lowerBound
		elif strength > self.upperBound:
			strength = self.upperBound

		return strength
		
		
	def setLowerBound (self, bound):
		self.lowerBound = bound
		
	def setUpperBound (self, bound):
		self.upperBound = bound
		
			
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



