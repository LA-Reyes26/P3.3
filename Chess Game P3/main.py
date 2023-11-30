import pygame
import sys

from constants import *
from game import Game
from board import Board
from dragger import Dragger
from square import Square
from move import Move
class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CheckMate!")
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        FPS = 60
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // sq_size
                    clicked_column = dragger.mouseX // sq_size

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_column].has_piece():
                        piece = board.squares[clicked_row][clicked_column].piece
                        #if valid piece (color) ?
                        if piece.color == game.next_player:

                            board.calculate_moves(piece, clicked_row, clicked_column, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                                # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                            

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // sq_size
                    motion_column = event.pos[0] // sq_size

                    game.set_hover(motion_row, motion_column)
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // sq_size
                        released_column = dragger.mouseX // sq_size

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_column)
                        final = Square(released_row, released_column)
                        move = Move(initial, final)

                            # valid move ?
                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_column].has_piece()
            # normal capture
                            board.move(dragger.piece, move)
                            game.play_sound(captured)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            #next turn
                            game.next_turn()

                    dragger.undrag_piece()

                #keypress
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        print("T key pressed")
                        game.change_themes()


                    if event.key == pygame.K_r:
                        print("r key pressed")
                        game.reset()
                        screen = self.screen
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger
                        FPS = 60
                        clock = pygame.time.Clock()


                # Quit event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
