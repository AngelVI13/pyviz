import pyglet
pyglet.resource.path = ["../media"]
pyglet.resource.reindex()

from models.game_state import GameState
from views.board import Board
from views.overlay import Overlay

window = pyglet.window.Window(800, 600)


game_model = GameState()
game_model.setup_pre_game()
board = Board(window, game_model)
overlay = Overlay(
    size=(window.width // 2, window.height // 2), 
    position=(window.width // 4, window.height // 4)
)

@window.event
def on_draw():
    window.clear()
    board.update()
    board.batch.draw()
    for piece in board.pieces:
        piece.draw()

    overlay.batch.draw()

pyglet.app.run()