class Ball :
	def _init_(self, diameter, color):
		self.diameter = diameter
        self.color = color
    def roll(self,distance):
        print("The ball has rolled" + str(distance))
    def bounce(self,bounce):
        print("The ball has bounced" + str(bounce) + "times.")


aBall = Ball(6, 'pink')
aBall.roll(4)
aBall.bounce(3)
