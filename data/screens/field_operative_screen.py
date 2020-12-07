import pygame as pg
from .. import setup, tools
from .. import constants as c


class FieldOperative(tools.GameState):
    """
    Field operative screen class
    """
    def __init__(self):
        tools.GameState.__init__(self)
        self.quit = False
