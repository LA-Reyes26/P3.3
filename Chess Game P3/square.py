class Square:

    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, column, piece=None):
        self.row = row
        self.column = column
        self.piece = piece
        self.alphacol = self.ALPHACOLS[column]

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def has_piece(self):
        return self.piece != None
    
    def is_empty(self):
        return not self.has_piece()
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color
    
    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color

    def is_empty_or_enemy(self, color):
        return self.is_empty() or self.has_enemy_piece(color)
    
    @staticmethod
    def in_range(*arguments):
        for argument in arguments:
            if argument < 0 or argument > 7:
                return False
            
        return True 
    
    @staticmethod
    def get_alphacol(column):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[column]

