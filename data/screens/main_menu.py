import pygame as pg
from .. import setup, tools
from .. import constants as c


class MainMenu(tools.GameState):
    """
    Main menu screen class
    """
    def __init__(self):
        tools.GameState.__init__(self)
        self.quit = False
