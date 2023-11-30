import pygame
from constants import *
from board import Board
from square import Square
from dragger import Dragger
from configuration import Config
from square import Square

class Game:
    def __init__(self):
        self.next_player = 'white'
        self.hovered_square = None
        self.board = Board()
        self.dragger = Dragger()
        self.configuration = Config()

    def show_bg(self, surface):
        theme = self.configuration.theme

        for row in range(rows):
            for column in range(columns):
                #color
                color = theme.bg.light if (row + column) % 2 == 0 else theme.bg.dark
                #rect
                rect = (column * sq_size, row * sq_size, sq_size, sq_size)
                #blit
                pygame.draw.rect(surface, color, rect)

                if column == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.configuration.font.render(str(rows-row), 1, color)
                    lbl_pos = (5, 5 + row * sq_size)
                    # blit
                    surface.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = theme.bg.dark if (row + column) % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.configuration.font.render(Square.get_alphacol(column), 1, color)
                    lbl_pos = (column * sq_size + sq_size - 20, height - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)

    def show_pieces(self, surface):
        for row in range(rows):
            for column in range(columns):
                if self.board.squares[row][column].has_piece():
                    piece = self.board.squares[row][column].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)

                        img = pygame.image.load(piece.texture)
                        img = pygame.transform.scale(img, (sq_size, sq_size))

                        img_center = (
                            column * sq_size + sq_size // 2,
                            row * sq_size + sq_size // 2
                        )

                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        theme = self.configuration.theme
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
            # Determine the color based on the sum of row and column
                color = theme.moves.light if (move.final.row + move.final.column) % 2 == 0 else theme.moves.dark
            
            # Define the rectangle based on the move's final position
                rect = (move.final.column * sq_size, move.final.row * sq_size, sq_size, sq_size)
            
            # Draw the rectangle on the Pygame surface
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme = self.configuration.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                #color
                color = theme.trace.light if (pos.row + pos.column) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.column * sq_size, pos.row * sq_size, sq_size, sq_size)
                # blit
                pygame.draw.rect(surface, color, rect)


    def show_hover(self,surface):
        if self.hovered_square:
                # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_square.column * sq_size, self.hovered_square.row * sq_size, sq_size, sq_size)
            # blit
            pygame.draw.rect(surface, color, rect, width = 5)
            
    #necxt player
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, column):
        self.hovered_square = self.board.squares[row][column]

    def change_themes(self):
        self.configuration.change_themes()

    def play_sound(self, captured=False):
        if captured:
            self.configuration.capture_sound.play()
        else:
            self.configuration.move_sound.play()

    def reset(self):
        self.__init__()



