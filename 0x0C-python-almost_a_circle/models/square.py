#!/usr/bin/python3
"""
This contains the square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
	"""Square class"""
	def __init__(self, size, x=0, y=0, id=None):
		"""
		Init the square
		Attributes:
      width, height, x, y, id 
		"""
		super().__init__(size, size, x, y, id)
	
	@property
	def size(self):
		"""size getter"""
		return self.width

	@size.setter
	def size(self, value):
		"""size setter"""
		self.width = value
		self.height = value

	def __str__(self):
		"""overloading method"""
		return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

		