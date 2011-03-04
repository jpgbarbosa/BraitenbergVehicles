
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
		self.rightSensor = None
		self.rightWheel = None
		self.vehicle = None
		myBraitenbergControl.init( self )

	def init( self ):
		self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		self.light.move( breve.vector( 3, 1, -3 ) )
		self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		self.light.move( breve.vector( 5, 1, -4 ) )
		self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		self.light.move( breve.vector( 8, 1, -6 ) )
		self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		self.light.move( breve.vector( 12, 1, -9 ) )
		self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		self.light.move( breve.vector( 17, 1, -13 ) )
		self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		self.light.move( breve.vector( 23, 1, -18 ) )
		self.block = breve.createInstances( breve.BraitenbergBlock, 1 )
		self.block.move( breve.vector( 18, 1.5, 0 ) )
		
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		lFrontWheel = self.vehicle.addWheel (breve.vector( 1, 0, 1.5 ))
		rFrontWheel = self.vehicle.addWheel (breve.vector( 1, 0, -1.5 ))
		lBackWheel = self.vehicle.addWheel (breve.vector( -1, 0, 1.5 ))
		rBackWheel = self.vehicle.addWheel (breve.vector( -1, 0, -1.5 ))
		lFrontSensor = self.vehicle.addBlockSensor (breve.vector( 2.2, 0, 1 ), 1.57000000, "gaussian", 0.1, 100)
		rFrontSensor = self.vehicle.addBlockSensor (breve.vector( 2.2, 0, -1 ), 1.57000000, "gaussian", 0.1, 100)
		
		lFrontSensor.link(rFrontWheel)
		rFrontSensor.link(lFrontWheel)
		lFrontSensor.link(rBackWheel)
		rFrontSensor.link(lBackWheel)
		
		#lFrontSensor.setBias(10)
		rFrontSensor.setBias(10)

breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
