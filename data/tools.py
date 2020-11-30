import os
import pygame as pg
from . import constants as c
import random


class Game(object):
    """
    Class for handling entire project. Contains game, event and main loops.
    """

    # TODO
    def __init__(self, caption):
        self.caption = caption
        self.screen = pg.display.get_surface()
        self.fps = c.FPS
        self.clock = pg.time.Clock()
        self.done = False
        self.current_time = 0.0
        self.state = None  # GameState
        self.screen_dict = {}
        self.screen = None
        self.screen_name = None

    def update(self):
        """
        Updates time. Then checks if state.quit, if not changes current state.
        :return: None
        """
        # TODO
        pass

    def event_loop(self):
        """
        Handles event.
        :return: None
        """
        # TODO
        pass

    def main_loop(self):
        """
        Main loop
        :return: None
        """
        # TODO
        pass

    def set_screens(self, screen_dict, current_screen_name):
        """
        Sets self.screen_dict, self.screen_name, self.screen with data given
        :param screen_dict: dictionary of all screens
        :param current_state: starting state
        :return: None
        """
        # TODO
        pass


class GameState(object):
    """
    Contains current previous and next states of Game
    """

    # TODO
    def __init__(self):
        self.done = False


def load_all_words(directory, categories, extensions=()):
    """
    Loads all words of given categories from given directory.
    :param directory: Directory with words
    :param categories: Allowed categories for words
    :param extensions: Allowed extensions os files with words
    :return: List of words
    """
    # TODO
    file = open('words_list.txt', 'r')
    order = random.sample(range(1, 1063), 25)
    words = []
    for i in order:
        words.append(file.line(i))
    return words



def load_all_sounds(directory, extensions=()):
    """
    Loads all sounds from given directory
    :param directory: Directory with sounds
    :param extensions: Allowed extensions for sound files
    :return: List of sounds
    """
    # TODO
    sounds = []
    pass


def load_all_music(directory, extensions=()):
    """
    Loads all music from given directory
    :param directory: Directory with music
    :param extensions: Allowed extensions for music files
    :return: List of music
    """
    # TODO
    music = []
    pass


def load_all_sprites(directory, extensions=()):
    """
    Loads all sprites from given directory
    :param directory: Directory with sprites
    :param extensions: Allowed extensions for sprite files
    :return: List of sprites
    """
    # TODO
    sprites = []
    pass
