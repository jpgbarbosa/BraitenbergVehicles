
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


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
		self.scenario = 'Attraction'
		myBraitenbergControl.init( self )

	def init( self ):
		
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
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector(14 , 1, 17))
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector( 5 , 1, 20))
	
		
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		self.vehicle.move(breve.vector(0,1,15))
		
		lWheel = self.vehicle.addWheel (breve.vector( -0.5, 0, -1.5 ))
		rWheel = self.vehicle.addWheel (breve.vector( -0.5, 0, 1.5 ))
		lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.3, 0, 1 ), 1.57000000, "exponential", -100, 100)
		rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.3, 0, 1 ),  1.57000000, "exponential", -100, 100)
		
		lFrontSensor.setType("BraitenbergSounds")
		rFrontSensor.setType("BraitenbergSounds")
		
		lFrontSensor.link(rWheel)
		rFrontSensor.link(lWheel)
		
		lWheel.setNaturalVelocity(0.00000)
		rWheel.setNaturalVelocity(0.00000)
		
		lFrontSensor.setBias(5)
		rFrontSensor.setBias(5)

breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
