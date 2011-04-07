
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
		'''Can take the values of 'Circle', 'Tunnel' or 'None'.'''
		self.scenario = 'Circle'
		self.block = None
		self.obj = None
		myBraitenbergControl.init( self )

	def init( self ):
		'''Several scenarios available.'''
		if self.scenario == 'Circle':
			self.n = 0
			while ( self.n < 40 ):
				breve.createInstances( breve.BraitenbergOlfaction, 1 ).move( breve.vector( ( 20 * breve.breveInternalFunctionFinder.sin( self, ( ( self.n * 1.570000 ) / 10 ) ) ), 2, ( 20 * breve.breveInternalFunctionFinder.cos( self, ( ( self.n * 1.570000 ) / 10 ) ) ) ) )
				self.n = ( self.n + 1 )
				
			self.n = 0
			while ( self.n < 20 ):
				breve.createInstances( breve.BraitenbergOlfaction, 1 ).move( breve.vector( ( 12 * breve.breveInternalFunctionFinder.sin( self, ( ( self.n * 3.140000 ) / 10 ) ) ), 1.5, ( 12 * breve.breveInternalFunctionFinder.cos( self, ( ( self.n * 3.140000 ) / 10 ) ) ) ) )
				self.n = ( self.n + 1 )
				
		elif self.scenario == 'Tunnel':
			#Blocks	
			for i in range(10):
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(i*4,0,5))
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(i*4,0,-5))
				
			for i in range(10,14):	
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(i*4,0,5))
			
			self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
			self.block.move( breve.vector(13*4,0,5))
			self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
			self.block.move( breve.vector(13*4,0,0))
			
			for i in range(7):
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(13*4,0,-5-i*4))
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(10*4,0,-5-i*4))
				
			for i in range(7,9):	
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(13*4,0,-5-i*4))
			
			
			for i in range(10):
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(i*4,0,-30))
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(i*4,0,-40))
			
			for i in range(10,14):	
				self.block = breve.createInstances( breve.BraitenbergOlfaction,1)
				self.block.move( breve.vector(i*4,0,-40))
			
		else:
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector(20 , 1, 4))
			breve.createInstances( breve.BraitenbergBlock, 1 ).move( breve.vector( 20, 1, 17))

		
		if self.scenario == 'Circle':
			'''Creates the first vehicle.'''
			self.vehicle = breve.createInstances( breve.BraitenbergTwoWheelsVehicle, 1 )
			self.watch( self.vehicle )
				
			self.vehicle.move(breve.vector(0,1,14))
			self.vehicle.rotate(breve.vector(0,1,0), 3.14)
		elif self.scenario == 'Tunnel':
			'''Creates the first vehicle.'''
			self.vehicle = breve.createInstances( breve.BraitenbergTwoWheelsVehicle, 1 )
			self.watch( self.vehicle )
				
			self.vehicle.move(breve.vector(0,1,0))
			self.vehicle.rotate(breve.vector(0,1,0), 0)
		else:
			'''Creates the first vehicle.'''
			self.vehicle = breve.createInstances( breve.BraitenbergTwoWheelsVehicle, 1 )
			self.watch( self.vehicle )
		
	
breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
