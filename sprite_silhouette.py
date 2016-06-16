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

		Arguments:
			sprite (:class:`pyglet.sprite.Sprite`): The Sprite to create a silhouette from.
			color (tuple of int): RGB color value of the silhouette, values between 0 and 255.
		"""
		super(SpriteSilhouette, self).__init__(sprite.image, *args, **kwargs)
		
		# Create a copy of the original image
		image_region = self.image.get_region(0, 0, self.image.width, self.image.height)
		image_copy = image_region.get_image_data().texture.get_image_data()

		# Number of pixels in the original image
		pixels = self.image.width * self.image.height

		# Get the original alpha data
		alpha_data = bytes(image_copy.get_data("A", 1 * self.image.width))

		# Prepare the new RGBA data
		new_data = list(color) * pixels

		# Insert the original alpha data into the new RGBA data as every 4th element
		index = 3
		for x in range(pixels):
			new_data.insert(index, alpha_data[x])
			index += 4

		# Set the color of the new image
		image_copy.set_data("RGBA", 4 * self.image.width, bytes(new_data))

		self.image = image_copy
