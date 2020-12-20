import pygame as pg
from .. import constants as c
from .. import setup
from ..game_components import button


class WordCard(button.Button):
    def __init__(self, x, y, width, height, type, text, text_size, font_name):
        button.Button.__init__(self, x, y, width, height, text, text_size, font_name)
        self.spy_button = button.Button(x, y, width, height, text, text_size, font_name)
        self.operative_button = button.Button(x, y, width, height, text, text_size, font_name)
        self.status = c.HIDDEN
        self.type = type
        self.spy_button.set_inactive(c.BLACK, setup.SPRITES[self.type])
        spy_active = self.spy_button.inactive_image.copy()
        pg.draw.rect(spy_active, c.GREEN, spy_active.get_rect(), int(5*c.MULTIPLIER))
        self.spy_button.set_active(c.BLACK, spy_active)
        self.operative_button.set_inactive(c.BLACK, setup.SPRITES["hidden"])
        operative_active = self.operative_button.inactive_image.copy()
        pg.draw.rect(spy_active, c.GREEN, operative_active.get_rect(), int(5*c.MULTIPLIER))
        self.operative_button.set_active(c.BLACK, operative_active)

    def set_captain(self, text_color, button_image=None):
        self.type = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_image:
            button_image = pg.transform.scale(button_image, (self.width, int(self.height)))
            button_rect = button_image.get_rect()
            button_rect.center = self.type.get_rect().center
            self.type.blit(button_image, button_rect)
        text_button = self.font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.type.get_rect().center
        self.type.blit(text_button, text_rect)

    def set_default(self, text_color, button_image=None):
        self.inactive_image = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_image:
            button_image = pg.transform.scale(button_image, (self.width, int(self.height)))
            button_rect = button_image.get_rect()
            button_rect.center = self.inactive_image.get_rect().center
            self.inactive_image.blit(button_image, button_rect)
        text_button = self.font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.inactive_image.get_rect().center
        self.inactive_image.blit(text_button, text_rect)

    def set_pressed(self, text_color, button_image=None):
        self.inactive_image = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_image:
            button_image = pg.transform.scale(button_image, (self.width, int(self.height)))
            button_rect = button_image.get_rect()
            button_rect.center = self.inactive_image.get_rect().center
            self.inactive_image.blit(button_image, button_rect)
        text_button = self.font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.inactive_image.get_rect().center
        self.inactive_image.blit(text_button, text_rect)

    def draw_spy_screen(self, surface):
        self.spy_button.draw(surface)

    def draw_operative_screen(self, surface):
        self.operative_button.draw(surface)

    def update(self):
        self.spy_button.active = self.active
        self.operative_button.active = self.active