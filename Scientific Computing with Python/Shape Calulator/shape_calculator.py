import math

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return 2 * (self.width + self.height)

	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2) ** 0.5

	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return 'Too big for picture.'
		output = ''
		for i in range(self.height):
			for j in range(self.width):
				output += '*'
			output += '\n'
		return output

	def get_amount_inside(self, shape):
		if shape.width <= self.width and shape.height <= self.height:
			return (self.height // shape.height)*(self.width // shape.width)
		return 0

class Square(Rectangle):
	def __init__(self, side):
		Rectangle.__init__(self, side, side)
		self.side = self.width


	def __str__(self):
		return f'Square(side={self.side})'

	def set_side(self ,side):
		self.width = side
		self.height = side
		self.side = side

	def set_width(self, side):
		self.width = side
		self.side = side

	def set_height(self, side):
		self.height = side
		self.side = side