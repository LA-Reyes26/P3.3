import os

PIECE_VALUES = {
    'pawn': 1.0,
    'knight': 3.0,
    'bishop': 3.001,
    'rook': 5.0,
    'queen': 8.0,
    'king': 10000000.0
}

class Piece:
    def __init__(self, name, color, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1
        self.value = PIECE_VALUES.get(name, 0.0) * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.texture_rect = texture_rect
        self.set_texture()

    def set_texture(self, size=80):
        self.texture = os.path.join(f'images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_moves(self, move):
        self.moves.append(move)

    def clear_moves(self):
         self.moves = []

        
class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("pawn", color)
    def add_move(self, move):
            self.moves.append(move)

class Knight(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("knight", color)
        
    def add_move(self, move):
            self.moves.append(move)

class Bishop(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("bishop", color)
    def add_move(self, move):
            self.moves.append(move)

class Rook(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("rook", color)
    def add_move(self, move):
            self.moves.append(move)

class Queen(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("queen", color)
    def add_move(self, move):
            self.moves.append(move)

class King(Piece):
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        self.dir = -1 if color == "white" else 1
        super().__init__("king", color)
    def add_move(self, move):
            self.moves.append(move)
