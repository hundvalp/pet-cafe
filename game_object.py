class GameObject(object):
	"""
	Representation of a visual game object.
	
	This is anything requiring an image, such as backgrounds or characters.

	Properties:
		x (int): The x coordinate of this game object.
		y (int): The y coordinate of this game object.
		width (int): The width of this game object.
		height (int): The height of this game object.
		image (int): The image object for this game object.
	"""

	def __init__(self, sprite):
		"""Creates a new graphical game object."""
		super(GameObject, self).__init__()
		self.sprite = sprite

	def draw(self):
		"""Draws the object to the screen."""
		self.sprite.draw()

	@property
	def x(self):
		"""Get the x coordinate of the object."""
		return self.sprite.x

	@property
	def y(self):
		"""Get the y coordinate of the object."""
		return self.sprite.y

	@property
	def width(self):
		"""Get the width of the object."""
		return self.sprite.width

	@property
	def height(self):
		"""Get the height of the object."""
		return self.sprite.height

	@property
	def image(self):
		"""Get the image of the object."""
		return self.sprite.image
