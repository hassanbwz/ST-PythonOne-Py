 class Circle():
	def __init__(self, radius):
		self.radius = radius
	def get_area(self):
		return self.radius**2*3.14
	def get_perimeter(self):
		return 2*3.14*self.radius

	
circle = Circle(11)
circle.get_area()
circle.get_perimeter

circle = Circle(4.44)
circle.get_area()
circle.get_perimeter()
