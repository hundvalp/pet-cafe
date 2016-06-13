from game_object import GameObject
from util import point_in_rectangle
from struct import unpack

class GameButton(object):
	"""
	Representation of a game object which can be interacted with using the mouse.
	"""

	def __init__(self, inactive, hover=None):
		"""Creates a new graphical game button object."""
		super(GameButton, self).__init__()
		self.inactive = inactive
		self.hover    = hover

		self.current_state = self.inactive

	def update(self, dt):
		self.current_state.update(dt)

	def handle_mouse_motion(self, x, y):
		"""
		Updates the Game Button button according to where the mouse is.

		If the mouse is over a visible portion of the game object, and a hover
		object was given, the object will be switched to the hover object.

		Arguments:
			x (int): The x coordinate of the mouse cursor.
			y (int): The y coordinate of the mouse cursor.
		"""
		# If a hover image was given and the mouse is within the game object's bounds
		if not self.hover is None and point_in_rectangle(self.inactive, x, y):
			pixel = self.current_state.image.get_region(x-self.current_state.x, y-self.current_state.y, 1, 1)
			image_data = pixel.get_image_data().texture.get_image_data()
			alpha = bytes(image_data.get_image_data().get_data("RGBA", 4))[3]

			# Don't count the mouseover unless the image is visible under the mouse
			if alpha != 0:
				self.current_state = self.hover
				return

		self.current_state = self.inactive
		
	def draw(self):
		"""
		Draws the current state of the button.
		
		This will be the hover image if one was given and the mouse is over the image.
		Otherwise, this will be the inactive image.
		"""
		self.current_state.draw()
