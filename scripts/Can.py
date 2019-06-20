

class Can:
	def __init__(self,vol,color):
		self.vol = vol
		self.color = color
		self.level = self.vol
		self.open = False

	def Open(self):
		if(self.open is False):
			self.open=True

	def Pour(self,amount):
		if(self.open):
			if(self.level>0):
				self.level-=amount
				if(self.level<0):
					self.level=0
			else:
				pass
		else:
			print "NOT OPEN!!"


firstcan = Can(16,'white')
secondcan = Can(16,'blue')

print firstcan.level

firstcan.Open()
firstcan.Pour(4)

print firstcan.level
