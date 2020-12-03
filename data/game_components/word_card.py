import pygame as pg
from .. import constants as c
from .. import setup


class Letter(pg.sprite.Sprite):
    """
    Single letter for words"
    """

    def __init__(self, image):
        super(Letter, self).__init__()
        self.image = image
        self.rect = image.get_rect()


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


class WordCard():
    # TODO add sprite logic
    def __init__(self, x, y, word):
        self.x = x
        self.y = y
        self.word = word  # Word class

    def get_image(self, x, y, width, height):
        """
        Extracts requred image from sprite file
        :return:
        """
        # TODO
        pass

    def draw(self):
        """
        Draws a card and word on this card
        :return:
        """
        # TODO
        pass
