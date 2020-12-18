import pygame as pg
from .. import constants
from .. import setup
from ..game_components import button


class Letter(pg.sprite.Sprite):
    """
    Single letter for words
    """

    def __init__(self, image):
        super(Letter, self).__init__()
        self.image = image
        self.rect = image.get_rect()

    def draw(self, x, y):
        pass


class Word():
    """
    A word to draw on card
    """

    # TODO add sprite logic
    def __init__(self, x, y, word):
        self.x = x
        self.y = y
        self.word = str(word)
        self.create_letter_dict()
        self.create_letter_list()

    def get_image(self, x, y, width, height):
        """
        Extracts requred image from sprite file
        :return:
        """
        # TODO
        pass

    def create_letter_dict(self):
        """
        Creates dictionary of all letters' images
        :return:
        """
        # TODO
        pass

    def create_letter_list(self):
        """
        Creates list of letter images based on word received
        :return:
        """
        # TODO
        pass

    def update(self, word):
        """
        Updates word
        :param word:
        :return:
        """
        # TODO
        pass

    def draw(self):
        """
        Draws word.
        :return:
        """
        # TODO


class WordCard(button.Button):
    # TODO add sprite logic
    def __init__(self, x, y, width, height, text, text_size, font_name, color):
        super(button.Button, self).__init__()
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
        self.captain = False
        self.capitane_image = None
        self.color = color
        self.fonts = setup.FONTS
        self.font = pg.font.Font(self.fonts[font_name], self.text_size)

    def set_captain(self, text_color, button_image=None):
        self.capitane_image = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_image:
            button_image = pg.transform.scale(button_image, (self.width, int(self.height)))
            button_rect = button_image.get_rect()
            button_rect.center = self.capitane_image.get_rect().center
            self.capitane_image.blit(button_image, button_rect)
        text_button = self.font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.capitane_image.get_rect().center
        self.capitane_image.blit(text_button, text_rect)

    def set_inactive(self, text_color, button_image=None):
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


    def draw(self, surface):
        if self.captain:
            surface.blit(self.capitane_image, (self.x, self.y))

    def get_image(self, x, y, width, height):
        """
        Extracts required image from sprite file
        :return:
        """
        # TODO
        pass


