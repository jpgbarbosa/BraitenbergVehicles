# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.

# Modified by:
# Ivo Daniel Venhuizen Correia, no 2008110814
# João Pedro Gaioso Barbosa, no 200811830
# TP3 and PL1


import breve

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
		self.scenario = 'None'
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
			pass
		elif self.scenario == 'Attraction':
			breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector(14 , 1, 17))
			breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector(16 , 1, 21))
			breve.createInstances( breve.BraitenbergSound, 1 ).move( breve.vector(20, 1, 27))
			
		elif self.scenario == 'None':
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector(20 , 1, 4))
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector( 20, 1, 17))

		
		'''Creates the vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		self.vehicle.move(breve.vector(0,1,15))
		
		'''Adds wheels and sensors.'''
		lWheel = self.vehicle.addWheel (breve.vector( -0.5, 0, -1.5 ))
		rWheel = self.vehicle.addWheel (breve.vector( -0.5, 0, 1.5 ))
		lFrontSensor = self.vehicle.addBlockSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.3, 0, 1 ), 1.57000000, "exponential", -100, 100)
		rFrontSensor = self.vehicle.addBlockSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.3, 0, 1 ),  1.57000000, "exponential", -100, 100)
		
		'''WARNING: If we are adding sensor other than block sensors, we have to make the setType.'''
		
		'''Links the sensors to the wheels.'''
		lFrontSensor.link(lWheel)
		rFrontSensor.link(rWheel)
		
		lWheel.setNaturalVelocity(0.00000)
		rWheel.setNaturalVelocity(0.00000)
		
		lFrontSensor.setBias(2)
		rFrontSensor.setBias(2)


breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
