import pygame
import os

from sound import Sound
from themes import Themes


class Config:

    def __init__(self,):
        self.themes= []
        self._add_themes()
        self.index = 0
        self.theme = self.themes[self.index]
        self.font =pygame.font.SysFont("monospace", 18, bold = True)

        self.move_sound = Sound(os.path.join("sounds/move.wav"))
        self.capture_sound = Sound(os.path.join("sounds/capture.wav"))


    def change_themes(self):
        self.index += 1
        self.index %= len(self.themes)

    def _add_themes(self):
        green = Themes((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Themes((150, 75, 0),(245, 245, 220), (244,247,116), (172, 195, 51), "#00bf63", "#7ed957")
        blue = Themes((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        red = Themes((139, 0, 0), (255, 99, 71), (0, 255, 255), (0, 128, 128), '#ff914d', "#ffdb59" )
        gray = Themes((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')
        purple = Themes( (72, 0, 72),(160, 120, 255), (255, 255, 0),(160, 120, 255), '#5271ff', '#004aad')

        self.themes =[green,brown, blue, red, gray, purple]