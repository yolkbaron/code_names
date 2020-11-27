import os
import pygame as pg
from . import constants as c


class Game(object):
    """
    Class for handling entire project. Contains game, event and main loops.
    """

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
        #TODO
        pass


class GameState(object):
    """
    Contains current previous and next states of Game
    """

    def __init__(self):
        self.done = False


def load_all_words(directory, extensions=()):
    # TODO
    words = []
    pass


def load_all_sounds(directory, extensions=()):
    # TODO
    sounds = []
    pass


def load_all_sprites(directory, extensions=()):
    # TODO
    sprites = []
    pass
