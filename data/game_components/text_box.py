import pygame as pg
from .. import setup
from ..game_components import button
from .. import constants


class InputBox(button.Button):

    def __init__(self, x, y, width, height, text_color, text_size, font_name, text=''):
        button.Button.__init__(self, x, y, width, height, text, text_size, font_name)
        self.text_color = text_color
        self.active = False
        self.color_inactive = constants.GRAY
        self.color_active = constants.YELLOW
        self.color = self.color_inactive
        self.txt_surface = self.font.render(text, True, self.text_color)

    def update(self):
        pass
        self.color = self.color_active if self.active else self.color_inactive

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.x, self.y))
        # Blit the rect.
        if self.color:
            pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)
