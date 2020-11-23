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
    def update(self):
        #TODO
        pass
    def event_loop(self):
        #TODO
        pass



class Screen(object):
    def __init__(self):
        pass
def load_all_words(directory, extensions = []):
    words = []
    pass
def load_all_sounds(directory, extensions = []):
    sounds = []
    pass
def load_all_sprites(directory, extensions = []):
    sprites = []
    pass