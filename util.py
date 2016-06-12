def value_in_range(value, min, max):
	"""
	Returns True if the value is within given range, False otherwise.
	
	Arguments:
		value (number): The number to check.
		min (number): The minimum value in the range.
		max (number): The maximum value in the range.
	"""
	return (value >= min) and (value <= max)

def point_in_rectangle(rect, x, y):
	"""
	Returns True if the point is within the given rectange, False otherwise.

	Arguments:
		rect (pyglet.sprite.Sprite): A Sprite object, which will have its rectangular
		                             bounding box checked. The x, y, width, and height
									 properties will be used.
		x (int): The x coordinate of the point.
		y (int): The y coordinate of the point.
	"""
	return value_in_range(x, rect.x, rect.x + rect.width) and value_in_range(y, rect.y, rect.y + rect.height)
