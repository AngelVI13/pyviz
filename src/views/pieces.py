import os
import pyglet
from typing import Tuple
from models.square import Color
from models.pieces import Bishop, Rook, Queen, King, Knight, Piece


def load_and_scale_img(img_filename, width, height):
    # Load and rescale images
    img = pyglet.resource.image(img_filename)
    img.width = width
    img.height = height
    return img


class Pieces:
    PIECE_SIZE = 64

    # Load and rescale images
    KNIGHT_W = load_and_scale_img('knight_w.png', width=PIECE_SIZE, height=PIECE_SIZE)
    KNIGHT_B = load_and_scale_img('knight_b.png', width=PIECE_SIZE, height=PIECE_SIZE)
    BISHOP_W = load_and_scale_img('bishop_w.png', width=PIECE_SIZE, height=PIECE_SIZE)
    BISHOP_B = load_and_scale_img('bishop_b.png', width=PIECE_SIZE, height=PIECE_SIZE)
    ROOK_W = load_and_scale_img('rook_w.png', width=PIECE_SIZE, height=PIECE_SIZE)
    ROOK_B = load_and_scale_img('rook_b.png', width=PIECE_SIZE, height=PIECE_SIZE)
    QUEEN_W = load_and_scale_img('queen_w.png', width=PIECE_SIZE, height=PIECE_SIZE)
    QUEEN_B = load_and_scale_img('queen_b.png', width=PIECE_SIZE, height=PIECE_SIZE)
    KING_W = load_and_scale_img('king_w.png', width=PIECE_SIZE, height=PIECE_SIZE)
    KING_B = load_and_scale_img('king_b.png', width=PIECE_SIZE, height=PIECE_SIZE)
    
    @classmethod
    def get_sprite(cls, piece: Piece):
        image = None

        if isinstance(piece, Bishop):
            image = cls.BISHOP_W if piece.square.color == Color.WHITE else cls.BISHOP_B
        elif isinstance(piece, Knight):
            image = cls.KNIGHT_W if piece.square.color == Color.WHITE else cls.KNIGHT_B
        elif isinstance(piece, Rook):
            image = cls.ROOK_W if piece.square.color == Color.WHITE else cls.ROOK_B
        elif isinstance(piece, Queen):
            image = cls.QUEEN_W if piece.square.color == Color.WHITE else cls.QUEEN_B
        elif isinstance(piece, King):
            image = cls.KING_W if piece.square.color == Color.WHITE else cls.KING_B
        else:
            raise ValueError(f"Unsupported piece: {type(piece)}")

        return pyglet.sprite.Sprite(img=image)
