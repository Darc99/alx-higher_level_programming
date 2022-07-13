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

	def update(self, *args, **kwargs):
		"""assigns an argument to each attribute"""
		attr_args = ["id", "size", "x", "y"]
		i = 0
		length = len(args)
		if length > 0:
			for arg in range(length):
				setattr(self, attr_args[i], args[i])
				i += 1
		else:
			for key, value in kwargs.items():
				setattr(self, key, value)
		
	def to_dictionary(self):
		"""the dictionary representation of a Rectangle"""
		dictionary_sq = {"id": self.id, "size": self.size, "x": self.__x, "y": self.__y}
		return dictionary_sq