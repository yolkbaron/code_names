import pygame as pg
from .. import setup


class Button(object):
    """
    Class for handling mouse clicking event.
    """

    def __init__(self, x, y, width, height, text, text_size, font_name):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.text_size = text_size
        self.pressed = False
        self.active = False
        self.inactive_image = None
        self.active_image = None
        self.fonts = setup.FONTS
        self.font_name = self.fonts[font_name]

    def set_inactive(self, text_color, button_image=None):
        """
        Adds button to given screen.
        :param button_image: Image of button background
        :param text_color: Color of text
        :return: Button object
        """
        self.inactive_image = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_image:
            button_image = pg.transform.scale(button_image, (self.width, int(self.height)))
            button_rect = button_image.get_rect()
            button_rect.center = self.inactive_image.get_rect().center
            self.inactive_image.blit(button_image, button_rect)
        font = pg.font.Font(self.font_name, self.text_size)
        text_button = font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.inactive_image.get_rect().center
        self.inactive_image.blit(text_button, text_rect)

    def set_active(self, text_color, button_image=None):
        """
        Adds button to given screen.
        :param button_image: Image of button background
        :param text_color: Color of text
        :return: Button object
        """
        self.active_image = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_image:
            button_image = pg.transform.scale(button_image, (self.width, int(self.height)))
            button_rect = button_image.get_rect()
            button_rect.center = self.active_image.get_rect().center
            self.active_image.blit(button_image, button_rect)
        font = pg.font.Font(self.font_name, self.text_size)
        text_button = font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.active_image.get_rect().center
        self.active_image.blit(text_button, text_rect)

    def check_crossing(self, pos):
        """
        Checks if pressed button.
        :param pos
        :return: True if cursor was above button when clicked, False if not
        """
        x, y = pos
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        else:
            return False

    def draw(self, surface):
        if self.active:
            surface.blit(self.active_image, (self.x, self.y))
        else:
            surface.blit(self.inactive_image, (self.x, self.y))
