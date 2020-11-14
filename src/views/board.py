import pyglet

from models.square import Square
from models.game_state import GameState
from views.tile import Tile
from views.pieces import Pieces


class Board:
    def __init__(self, window: pyglet.window.Window, game_model: GameState):
        self.screen = window
        self.game_model = game_model

        self.screen_width = self.screen.width
        self.screen_height = self.screen.height

        self.board_offset_x = (self.screen_width - 8 * Tile.TILE_SIZE) // 2
        self.board_offset_y = (self.screen_height - 8 * Tile.TILE_SIZE) // 2

        self.batch = pyglet.graphics.Batch()
        
        # Create board tiles
        self.tiles = []
        for file in range(8):
            for rank in range(8):
                tile = Tile(
                    square=Square(file, rank),
                    offsets=(self.board_offset_x, self.board_offset_y),
                    batch=self.batch
                )
                self.tiles.append(tile)

        self.pieces = []

    def update(self):
        # reset all pieces
        self.pieces_batch = pyglet.graphics.Batch()

        for tile in self.tiles:
            piece = self.game_model.board.get_piece_at_square(tile.square)

            # show pieces only if we are in pre-game state or when the game is over
            if piece: # and self.game_model.current_state != States.PLAY:
                piece_sprite = Pieces.get_sprite(piece)
                piece_sprite.x = tile.sprite.x
                piece_sprite.y = tile.sprite.y
                self.pieces.append(piece_sprite)
