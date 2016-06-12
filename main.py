from pyglet.gl import glEnable, glBlendFunc, GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
from pyglet.sprite import Sprite
from game_object import GameObject
from game_button import GameButton
import pyglet

frame_rate = 120

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

donut_r       = pyglet.resource.image("donut.png")
donut_hover_r = pyglet.resource.image("donut-hover.png")
donut       = GameObject(pyglet.sprite.Sprite(img=donut_r, x=400, y=300))
donut_hover = GameObject(pyglet.sprite.Sprite(img=donut_hover_r, x=400, y=300))

game_window = pyglet.window.Window(800, 600, caption="Pet Cafe")
#game_window.set_icon(pyglet.resource.image('icon.png')) # TODO Load an icon

key_handler = pyglet.window.key.KeyStateHandler()
game_window.push_handlers(key_handler)

# TODO Don't hardcode this
button = GameButton(donut, hover=donut_hover)

@game_window.event
def on_draw():
	# TODO It's possible that this could be removed if it's a significant performance bottleneck
	game_window.clear()

	# TODO Don't hardcode this
	button.draw()

@game_window.event
def on_mouse_motion(x, y, dx, dy):
	# TODO Don't hardcode this
	button.update(x, y)

def update(dt):
	pass

if __name__ == "__main__":
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	pyglet.clock.schedule_interval(update, 1.0/frame_rate)
	pyglet.app.run()
