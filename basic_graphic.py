from pyglet import resource

class BasicGraphic(object):
	"""
	A basic graphic.
	
	Attributes:
		image (:class:`pyglet.image.AbstractImage`): The image.
	"""

	def __init__(self, image):
		"""
		Creates a new graphic.

		Arguments:
			image (:class:`pyglet.image.AbstractImage`): The image resource for this graphical object.
		"""
		super(BasicGraphic, self).__init__()
		self.image = image

	def update(self, dt):
		"""
		This method does nothing and exists for compatibility.

		Arguments:
			dt (float): The number of seconds between the current frame and the previous frame.
		"""
		pass

	def blit(self, x=0, y=0, z=0):
		"""
		Draws the graphic with its anchor point (usually the bottom left corner) at the given coordinates.

		Kwargs:
			x (int): The x coordinate to draw the animation's anchor point at.
			         Defaults to 0.
			y (int): The y coordinate to draw the animation's anchor point at.
			         Defaults to 0.
			z (int): The z coordinate to draw the animation's anchor point at.
			         Defaults to 0.
		"""
		self.image.blit(x, y, z)

	@classmethod
	def from_image(cls, image, *args, **kwargs):
		"""
		Creates an graphic from an image.

		Arguments:
			image (str): The path to the image file in the resources directory.

		Returns:
			A :class:`BasicGraphic` object.
		"""
		return cls(resource.image(image), *args, **kwargs)
