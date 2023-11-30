import pygame
from constants import *


class Dragger:

    def __init__(self):
        self.dragging = False
        self.piece = None
        self.initial_row = 0
        self.initial_column = 0
        self.mouseX = 0 
        self.mouseY = 0

    def update_blit(self, surface):
        self.piece.set_texture(size=130)
        texture = self.piece.texture

        img = pygame.image.load(texture)
        img = pygame.transform.scale(img, (130, 130))
        img_center = (self.mouseX, self.mouseY)
        
        self.piece.texture_rect = img.get_rect(center = img_center)
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // sq_size
        self.initial_column = pos[0] // sq_size

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False