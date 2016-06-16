from pyglet.gl import glEnable, glBlendFunc, GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
from pyglet.image import Animation
from pyglet.sprite import Sprite
from pyglet import resource, window, clock, app
from game_button import GameButton
from sprite_silhouette import SpriteSilhouette

frame_rate = 120

resource.path = ['resources']
resource.reindex()

game_window = window.Window(800, 600, caption="Pet Cafe")
#game_window.set_icon(pyglet.resource.image('icon.png')) # TODO Load an icon

key_handler = window.key.KeyStateHandler()
game_window.push_handlers(key_handler)

# TODO Don't hardcode this
donut       = Sprite(resource.image("donut.png"),       x=400, y=300)
donut_hover = Sprite(resource.image("donut-hover.png"), x=400, y=300)
button = GameButton(donut, hover=donut_hover)

# TODO Don't hardcode this
ani_donut_frames = []
for x in range(1, 40+1):
	ani_donut_frames.append(resource.image('pink-trans-donut/trans-donut{0:04d}.png'.format(x)))

ani_donut_animation = Animation.from_image_sequence(
	ani_donut_frames, 1.0/24, loop=True)

ani_donut_hover_frames = []
for x in range(1, 40+1):
	ani_donut_hover_frames.append(resource.image('blue-trans-donut/trans-donut{0:04d}.png'.format(x)))

ani_donut_hover_animation = Animation.from_image_sequence(
	ani_donut_hover_frames, 1.0/24, loop=True)

ani_donut       = Sprite(ani_donut_animation,       x=100, y=100)
ani_donut_hover = Sprite(ani_donut_hover_animation, x=100, y=100)

ani_button = GameButton(ani_donut, hover=ani_donut_hover, sync_hover_state=True)

# TODO Don't hardcode this
donut_silhouette = SpriteSilhouette(donut, (255,255,150), x=500, y=100)

@game_window.event
def on_draw():
	# TODO It's possible that this could be removed if it's a significant performance bottleneck
	game_window.clear()

	# TODO Don't hardcode this
	button.draw()
	ani_button.draw()
	donut_silhouette.draw()

@game_window.event
def on_mouse_motion(x, y, dx, dy):
	# TODO Don't hardcode this
	button.handle_mouse_motion(x, y)
	ani_button.handle_mouse_motion(x, y)

def update(dt):
	pass

if __name__ == "__main__":
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	clock.schedule_interval(update, 1.0/frame_rate)
	app.run()
