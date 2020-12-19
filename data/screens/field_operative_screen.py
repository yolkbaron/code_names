import pygame as pg
from ..game_components import button
from ..game_components import word_card
from .. import setup, tools
from .. import constants as c
import random


class FieldOperative(tools.GameState):
    """
    Field operative screen class
    """
    def __init__(self):
        tools.GameState.__init__(self)
        self.quit = False
