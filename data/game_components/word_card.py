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
        pg.draw.rect(spy_active, c.FOREST_GREEN, spy_active.get_rect(), int(5 * c.MULTIPLIER))
        self.spy_button.set_active(c.BLACK, spy_active)
        self.operative_button.set_inactive(c.BLACK, setup.SPRITES["hidden"])
        operative_active = self.operative_button.inactive_image.copy()
        pg.draw.rect(operative_active, c.FOREST_GREEN, operative_active.get_rect(), int(5 * c.MULTIPLIER))
        self.operative_button.set_active(c.BLACK, operative_active)

    def reveal(self):
        self.status = c.REVEALED
        self.spy_button.text = None
        self.operative_button.text = None
        self.spy_button.set_inactive(c.BLACK, setup.SPRITES[self.type])
        self.operative_button.set_inactive(c.BLACK, setup.SPRITES[self.type])
        active = self.spy_button.inactive_image.copy()
        pg.draw.rect(active, c.FOREST_GREEN, active.get_rect(), int(5*c.MULTIPLIER))
        self.spy_button.set_active(c.BLACK, active)
        self.operative_button.set_active(c.BLACK, active)

    def draw_spy_screen(self, surface):
        self.spy_button.draw(surface)

    def draw_operative_screen(self, surface):
        self.operative_button.draw(surface)

    def update(self):
        self.spy_button.active = self.active
        self.operative_button.active = self.active
        self.spy_button.pressed = self.pressed
        self.operative_button.pressed = self.pressed
        self.pressed = False
        if self.spy_button.pressed:
            self.spy_button.pressed = False
        if self.operative_button.pressed:
            self.operative_button.pressed = False
            self.status = c.REVEALED
