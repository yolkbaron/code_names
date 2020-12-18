import pygame as pg
from .. import setup
from ..game_components import button


class InputBox(button.Button):

    def __init__(self, x, y, width, height, text_color, text_size, font_name, text=''):
        button.Button.__init__(self, x, y, width, height, text, text_size, font_name)
        self.text_color = text_color
        print(type(self.font))
        self.txt_surface = self.font.render(text, True, self.text_color)
        self.active = False
        self.COLOR_INACTIVE = pg.Color('lightskyblue3')
        self.COLOR_ACTIVE = pg.Color('dodgerblue2')
        self.color = self.COLOR_INACTIVE

    def update(self):
        self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.x, self.y))
        # Blit the rect.
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)
