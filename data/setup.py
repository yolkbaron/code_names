"""
Initializes the game screen and creates dictionaries of sounds, sprites and music, list of words
"""

import os
import pygame as pg
from . import tools
from . import constants

pg.init()
pg.event.set_allowed(constants.ALLOWED_EVENTS)
pg.display.set_caption(constants.BASIC_CAPTION)
SCREEN = pg.display.set_mode(constants.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

SPRITES = tools.load_all_sprites(os.path.join("resources", "sprites"))
SOUNDS = tools.load_all_sounds(os.path.join("resources", "sounds"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
WORDS = tools.load_all_words(os.path.join("resources", "words"))
