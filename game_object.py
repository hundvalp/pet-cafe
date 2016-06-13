class GameObject(object):
	"""
	Representation of a visual game object.
	
	This is anything requiring an image, such as backgrounds or characters.

	Properties:
		x (int): The x coordinate of this game object.
		y (int): The y coordinate of this game object.
		z (int): The z coordinate of this game object.
		width (int): The width of this game object.
		height (int): The height of this game object.
		image (int): The :class:`pyglet.image.AbstractImage` object for this game object.
	"""

	def __init__(self, image, x=0, y=0, z=0):
		"""
		Creates a new graphical game object.
		
		Arguments:
			image (object): An object with a blit(x,y,z) method,
			                and optionally an update(dt) method.

		Kawrgs:
			x (int): The x coordinate. Default is 0.
			y (int): The y coordinate. Default is 0.
			z (int): The z coordinate. Default is 0.
		"""
		super(GameObject, self).__init__()
		self._image = image
		self._x     = int(x)
		self._y     = int(y)
		self._z     = int(z)

	def draw(self):
		"""Draws the object to the screen."""
		self._image.blit(self._x, self._y, self._z)

	def update(self, dt):
		"""
		Updates the game object.

		If the given image has an update(dt) method,
		it will be called.

		Arguments:
			dt (float): The number of seconds that have passed
			            since the last update.
		"""
		update_method = getattr(self._image, "update", None)
		if callable(update_method):
			self._image.update(dt)

	@property
	def x(self):
		"""Get the x coordinate of the object."""
		return self._x

	@property
	def y(self):
		"""Get the y coordinate of the object."""
		return self._y

	@property
	def width(self):
		"""Get the width of the object."""
		return self.image.width

	@property
	def height(self):
		"""Get the height of the object."""
		return self.image.height

	@property
	def image(self):
		"""Get the image of the object."""
		if getattr(self._image, "image", None):
			return self._image.image
		return self._image
