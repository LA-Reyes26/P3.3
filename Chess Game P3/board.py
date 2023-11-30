from constants import *
from square import Square
from pieces import *
from move import Move
import copy

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for column in range(columns)]
        self.last_move = None
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
    
    def move(self, piece, move):
        initial = move.initial
        final = move.final

        self.squares[initial.row][initial.column].piece = None
        self.squares[final.row][final.column].piece = piece

        #pawn promotion
        if isinstance(piece, Pawn):
            self.check_promotion(piece, final)

        #king castling
        if isinstance(piece, King):
            if self.castling(initial, final):
                diff = final.column - initial.column
                rook = piece.left_rook if (diff < 0) else piece.right_rook
                self.move(rook, rook.moves[-1])

        # move
        piece.moved = True

        # clear valid moves
        piece.clear_moves()

        # set last move
        self.last_move = move

    def in_check(self, piece, move):
        temp_piece = copy.deepcopy(piece)
        temp_board = copy.deepcopy(self)
        temp_board.move(temp_piece, move)
        
        for row in range(rows):
            for col in range(columns):
                if temp_board.squares[row][col].has_enemy_piece(piece.color):
                    p = temp_board.squares[row][col].piece
                    temp_board.calculate_moves(p, row, col, bool=False)
                    for m in p.moves:
                            if isinstance(m.final.piece, King):
                                return True
        
        return False

    def valid_move(self, piece, move):
        return move in piece.moves
    
    def check_promotion(self, piece, final):
        if final.row == 0 or final.row == 7:
            self.squares[final.row][final.column].piece = Queen(piece.color)

    def castling(self, initial, final):
        return abs(initial.column - final.column) == 2

    def calculate_moves(self, pieces, row, column, bool=True): 
        
         
        def pawn_moves(self, row, column, pieces):
            if pieces.moved:
                steps = 1
            else:
                steps = 2

            start = row + pieces.dir
            end = row + (pieces.dir * (1 + steps))

            for move_row in range(start, end, pieces.dir):
                if Square.in_range(move_row):
                    if self.squares[move_row][column].is_empty():
                        initial = Square(row, column)
                        final = Square(move_row, column)
                        move = Move(initial, final)
                        # check potencial checks
                        if bool:
                            if not self.in_check(pieces, move):
                                # append new move
                                pieces.add_move(move)
                        else:
                            # append new move
                            pieces.add_move(move)

                    else:
                # Break if the square is occupied
                        break
                else:
            # Break if the move is out of range
                    break
            
            possible_move_row = row + pieces.dir
            possible_move_columns = [column-1, column+1]
            for possible_move_column in possible_move_columns:
                if Square.in_range(possible_move_row, possible_move_column):
                    if self.squares[possible_move_row][possible_move_column].has_enemy_piece(pieces.color):
                        # create initial and final move squares
                        initial = Square(row, column)
                        final_piece = self.squares[possible_move_row][possible_move_column].piece
                        final = Square(possible_move_row, possible_move_column,final_piece)
                        # create a new move
                        move = Move(initial, final)
                        pieces.add_move(move)

                 

        def knight_moves():
    # 8 possible moves
            possible_moves = [
                (row - 2, column + 1),
                (row - 1, column + 2),
                (row + 1, column + 2),
                (row + 2, column + 1),
                (row + 2, column - 1),
                (row + 1, column - 2),
                (row - 1, column - 2),
                (row - 2, column - 1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_column = possible_move

        # Check if the possible move is within the valid range
                if Square.in_range(possible_move_row, possible_move_column):
            # Check if the destination square is empty or occupied by a rival piece
                    if self.squares[possible_move_row][possible_move_column].is_empty_or_enemy(pieces.color):
                        initial = Square(row, column)
                        final_piece = self.squares[possible_move_row][possible_move_column].piece
                        final = Square(possible_move_row, possible_move_column,final_piece)

                # Create a Move object and add it to the list of moves for the piece
                        move = Move(initial, final)
                        pieces.add_move(move)

        def straightline_moves(incrs):
            for increase in incrs:
                row_increase, column_increase = increase
                possible_move_row = row + row_increase
                possible_move_column = column + column_increase

                while True:
                    if Square.in_range(possible_move_row, possible_move_column):
                        # create squares of the possible new move
                        initial = Square(row, column)
                        final_piece = self.squares[possible_move_row][possible_move_column].piece
                        final = Square(possible_move_row, possible_move_column, final_piece)
                        # create a possible new move
                        move = Move(initial, final)

                        # empty = continue looping
                        if self.squares[possible_move_row][possible_move_column].is_empty():
                            # check potencial checks
                                # append new move
                    
                                pieces.add_move(move)
                                

                        # has enemy piece = add move + break
                        elif self.squares[possible_move_row][possible_move_column].has_enemy_piece(pieces.color):
                            # check potencial checks
                                pieces.add_move(move)
                                

                        # has team piece = break
                        elif self.squares[possible_move_row][possible_move_column].has_team_piece(pieces.color):
                            break
                    
                    # not in range
                    else: break

                    # incrementing incrs
                    possible_move_row = possible_move_row + row_increase
                    possible_move_column = possible_move_column + column_increase


        def king_moves():
            adjs = [
                (row-1, column+0), # up
                (row-1, column+1), # up-right
                (row+0, column+1), # right
                (row+1, column+1), # down-right
                (row+1, column+0), # down
                (row+1, column-1), # down-left
                (row+0, column-1), # left
                (row-1, column-1), # up-left
            ]

            # normal moves
            for possible_move in adjs:
                possible_move_row, possible_move_column = possible_move

                if Square.in_range(possible_move_row, possible_move_column):
                    if self.squares[possible_move_row][possible_move_column].is_empty_or_enemy(pieces.color):
                        # create squares of the new move
                        initial = Square(row, column)
                        final = Square(possible_move_row, possible_move_column) # piece=piece
                        # create new move
                        move = Move(initial, final)
                        # check potencial checks
                            # append new move
                        if bool:
                            if not self.in_check(pieces, move):
                                pieces.add_move(move)
                            else: break

                        else:
                            pieces.add_move(move)

            # castling moves
            if not pieces.moved:
                # queen castling
                left_rook = self.squares[row][0].piece
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            # castling is not possible because there are pieces in between ?
                            if self.squares[row][c].has_piece():
                                break

                            if c == 3:
                                # adds left rook to king
                                pieces.left_rook = left_rook

                                # rook move
                                initial = Square(row, 0)
                                final = Square(row, 3)
                                moveR = Move(initial, final)
                                

                                # king move
                                initial = Square(row, column)
                                final = Square(row, 2)
                                moveK = Move(initial, final)
                                

                                if bool:
                                    if not self.in_check(pieces, moveK) and not self.in_check(left_rook, moveR):

                                        left_rook.add_move(moveR)
                                        pieces.add_move(moveK)
                                    

                                else:
                                    left_rook.add_move(moveR)
                                    pieces.add_move(moveK)

                # king castling
                right_rook = self.squares[row][7].piece
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            # castling is not possible because there are pieces in between ?
                            if self.squares[row][c].has_piece():
                                break

                            if c == 6:
                                # adds right rook to king
                                pieces.right_rook = right_rook

                                # rook move
                                initial = Square(row, 7)
                                final = Square(row, 5)
                                moveR = Move(initial, final)
                                

                                # king move
                                initial = Square(row, column)
                                final = Square(row, 6)
                                moveK = Move(initial, final)
                                
                                if bool:
                                    if not self.in_check(pieces, moveK) and not self.in_check(right_rook, moveR):

                                        right_rook.add_move(moveR)
                                        pieces.add_move(moveK)
                                    

                                else:
                                    right_rook.add_move(moveR)
                                    pieces.add_move(moveK)

        if isinstance(pieces, Pawn): 
                pawn_moves(self, row, column, pieces)

        elif isinstance(pieces, Knight): 
                knight_moves()

        elif isinstance(pieces, Bishop): 
                straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])

        elif isinstance(pieces, Rook): 
                straightline_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])

        elif isinstance(pieces, Queen): 
                straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ])
        elif isinstance(pieces, King): 
            king_moves()

    def _create(self):
        for row in range(rows):
            for column in range(columns):
                self.squares[row][column] = Square(row, column)
    
    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        for column in range(columns):
            self.squares[row_pawn][column] = Square(row_pawn, column, Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other,2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
