from enum import Enum, auto
from ctypes import c_uint64


class Color(Enum):
    WHITE = auto()
    BLACK = auto()


class Square:
    FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
    RANKS = list(range(1, 9)) # [1, 8] inclusive
    # Pre-computed 64-bit bitboard that has 1's where black squares are 
    COLOR_BITBOARD = c_uint64(0xAA55AA55AA55AA55) 

    def __init__(self, file: int, rank: int):
        if file not in range(8) or rank not in range(8):
            raise ValueError(f"Invalid rank/file: f-{file} r-{rank}")

        self.file = file
        self.rank = rank

    @property
    def color(self) -> Color:
        # convert file & rank to 64-based index
        is_black = (self.COLOR_BITBOARD.value >> self.index) & 1
        return Color.BLACK if is_black else Color.WHITE

    @property    
    def notation(self) -> str:
        return f"{self.FILES[self.file]}{self.RANKS[self.rank]}"

    @property
    def index(self) -> int:
        return self.rank * 8 + self.file

    @classmethod
    def from_index(cls, index: int):
        if not isinstance(index, int):
            raise TypeError(f"Index should by of type int. Got: {type(index)}")

        if index not in range(64):
            raise ValueError(f"Index should be in range [0,63] inclusive. Got: {index}")

        rank, file = divmod(index, 8)
        return cls(file, rank)

    @classmethod
    def from_notation(cls, notation: str):
        if not isinstance(notation, str):
            raise TypeError(f"Notation should be of type str. Got: {type(notation)}")

        if len(notation) != 2:
            raise ValueError(f"Wrong square format: {notation}")

        notation = notation.lower()
        file_str, rank_str = notation
        if file_str not in cls.FILES or int(rank_str) not in cls.RANKS:
            raise ValueError(f"Wrong square format: {notation}")

        file = cls.FILES.index(file_str)
        rank = cls.RANKS.index(int(rank_str))
        return cls(file, rank)

    def __eq__(self, other) -> bool:
        return self.file == other.file and self.rank == other.rank

    def __hash__(self):
        return hash((self.file, self.rank))

    def __repr__(self):
        return f"{self.__class__.__name__}(file={self.file}, rank={self.rank})"
