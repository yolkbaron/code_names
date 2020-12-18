import pygame as pg
from .. import setup
from ..game_components import button


class InputBox(button.Button):

    def __init__(self, x, y, width, height, text_color, text_size, font_name, text=''):
        button.Button.__init__(self, x, y, width, height, text, text_size, font_name)
        self.text_color = text_color
        self.font = setup.FONTS[font_name]
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.COLOR_INACTIVE = pg.Color('lightskyblue3')
        self.COLOR_ACTIVE = pg.Color('dodgerblue2')
        self.color = self.COLOR_INACTIVE

    def update(self):
        self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
