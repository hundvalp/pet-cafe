from util import point_in_rectangle
from struct import unpack

class GameButton(object):
	"""
	Representation of a sprite which can be interacted with using the mouse.
	"""

	def __init__(self, inactive, hover=None, sync_hover_state=False):
		"""
		Creates a new graphical game button object.
		
		Arguments:
			inactive (:class:`pyglet.sprite.Sprite`): The sprite to display while the button
			                                          is inactive.

		Kwargs:
			hover (:class:`pyglet.sprite.Sprite`): The graphic to display while the button
			                                       is hovered over. If None, no special hover
										           state will be used.
		"""
		super(GameButton, self).__init__()
		self.inactive = inactive
		self.hover    = hover

		if not self.hover is None:
			self.hover.visible = False

		self.current_state = self.inactive
		self._state_label = 'inactive'

	def handle_mouse_motion(self, x, y):
		"""
		Updates the Game Button button according to where the mouse is.

		If the mouse is over a visible portion of the sprite, and a hover
		sprite was given, the sprite will be switched to the hover sprite.

		Arguments:
			x (int): The x coordinate of the mouse cursor.
			y (int): The y coordinate of the mouse cursor.
		"""
		# If a hover image was given and the mouse is within the game object's bounds
		if not self.hover is None and point_in_rectangle(self.inactive, x, y):
			pixel = self.current_state._texture.get_region(x-self.current_state.x, y-self.current_state.y, 1, 1)
			image_data = pixel.get_image_data().texture.get_image_data()
			alpha = bytes(image_data.get_data("RGBA", 4))[3]

			# Don't count the mouseover unless the image is visible under the mouse
			if alpha != 0:
				self.current_state = self.hover
				self._state_label = 'hover'

				self.inactive.visible = False
				self.hover.visible = True

				return

		self.current_state = self.inactive
		self._state_label = 'inactive'

		self.inactive.visible = True
		self.hover.visible = False
		
	def draw(self):
		"""
		Draws the current state of the button.
		
		This will be the hover image if one was given and the mouse is over the image.
		Otherwise, this will be the inactive image.
		"""
		self.current_state.draw()
