from game_object import GameObject
from copy import copy

class GameObjectSilhouette(GameObject):
	"""
	Silhouette of a visual game object.

	This creates a copy of an existing GameObject in monotone,
	which functions exactly as any other GameObject would.
	
	Properties:
		x (int): The x coordinate of this game object.
		y (int): The y coordinate of this game object.
		z (int): The z coordinate of this game object.
		width (int): The width of this game object.
		height (int): The height of this game object.
		image (object): An object with a blit(x,y,z) method,
			            an update(dt) method, and an image property
						of the type :class:`pyglet.image.AbstractImage`.
	"""

	def __init__(self, game_object, color, *args, **kwargs):
		"""
		Creates a silhouette of a GameObject.

		Arguments:
			game_object (:class:`GameObject`): The GameObject to create a silhouette from.
			color (tuple of int): RGB color value of the silhouette, values between 0 and 255.

		Kawrgs:
			x (int): The x coordinate. Default is 0.
			y (int): The y coordinate. Default is 0.
			z (int): The z coordinate. Default is 0.
		"""
		super(GameObjectSilhouette, self).__init__(game_object._image, *args, **kwargs)
		
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

		self._image = copy(self._image)
		self._image.image = image_copy
