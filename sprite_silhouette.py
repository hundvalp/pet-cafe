from pyglet.image import Animation
from pyglet.sprite import Sprite

class SpriteSilhouette(Sprite):
	"""
	Silhouette of a sprite.

	This creates a copy of an existing Sprite in monotone,
	which functions exactly as any other Sprite would.
	"""

	def __init__(self, sprite, color, *args, **kwargs):
		"""
		Creates a silhouette of a Sprite.

		This works for animated sprites as well.

		Arguments:
			sprite (:class:`pyglet.sprite.Sprite`): The Sprite to create a silhouette from.
			color (tuple of int): RGB color value of the silhouette, values between 0 and 255.
		"""
		super(SpriteSilhouette, self).__init__(sprite.image, *args, **kwargs)

		# Cache of images which have already been created
		self._image_cache = {}

		if isinstance(sprite.image, Animation):
			frames   = [self._create_silhouette_from(frame.image, color) for frame in sprite.image.frames]
			duration = sprite.image.frames[0].duration
			loop     = not sprite.image.frames[-1].duration is None
			image_copy = Animation.from_image_sequence(frames, duration, loop=loop)
		else:
			image_copy = self._create_silhouette_from(sprite.image, color)

		self.image = image_copy

	def _create_silhouette_from(self, image, color):
		"""
		Creates a silhouette from the given :class:`pyglet.image.AbstractImage` object.

		Arguments:
			image (:class:`pyglet.image.AbstractImage`): The image to create a silhouette from.
			color (tuple of int): RGB color value of the silhouette, values between 0 and 255.

		Returns:
			A new :class:`pyglet.image.AbstractImage` object created from the original.
		"""
		# Create a copy of the original image
		image_copy = image.get_image_data()

		# Number of pixels in the original image
		pixels = image.width * image.height

		# Get the original alpha data
		alpha_data = image_copy.get_data("A", image.width)
		alpha_hash = hash(tuple(alpha_data))

		if alpha_hash in self._image_cache:
			return self._image_cache[alpha_hash]

		# Prepare the new RGBA data
		new_data = bytearray()
		for a in alpha_data:
			new_data.extend(color)
			new_data.append(a)

		# Set the color of the new image
		image_copy.set_data("RGBA", 4 * image.width, bytes(new_data))

		# Cache this image
		self._image_cache[alpha_hash] = image_copy

		return image_copy
