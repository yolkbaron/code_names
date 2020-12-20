import pygame as pg
from .. import setup
from ..game_components import button
from .. import constants


class InputBox(button.Button):

    def __init__(self, x, y, width, height, text_color, text_size, font_name, text='', max_length=-1):
        button.Button.__init__(self, x, y, width, height, text, text_size, font_name)
        self.text_color = text_color
        self.active = False
        self.color_inactive = constants.GRAY
        self.color_active = constants.FOREST_GREEN
        self.color = self.color_inactive
        self.txt_surface = self.font.render(text, True, self.text_color)
        self.max_length = max_length

    def update(self):
        self.color = self.color_active if self.active else self.color_inactive

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.x, self.y))
        if self.color:
            pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)

    def key_pressed(self, event):
        if self.active:
            if event.key == pg.K_RETURN:
                self.text = ''
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            elif self.max_length == -1 or self.max_length > len(
                    self.text):
                self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, self.text_color)
