import os
import pygame as pg
from . import constants as c

class Game(object):
    """
    Class for handling entire project. Contains game and event loops.
    """
    def __init__(self, caption):
        self.caption = caption
        self.screen = pg.display.get_surface()
        self.fps = c.FPS
        self.clock = pg.time.Clock()
        self.done = False
        self.current_time = 0.0
        self.state = None # GameState
    def update(self):
        """
        Updates time. Then checks if state.quit, if not changes current state.
        :return: None
        """
        #TODO
        pass
    def event_loop(self):
        """
        Handles event.
        :return:
        """
        #TODO
        pass



class GameState(object):
    """
    Contains current previous and next states of Game
    """
    def __init__(self):
        self.done = False

def load_all_words(directory, extensions = ()):
    words = []
    pass
def load_all_sounds(directory, extensions = ()):
    sounds = []
    pass
def load_all_sprites(directory, extensions = ()):
    sprites = []
    pass