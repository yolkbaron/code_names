import pygame as pg

FPS = 60

SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ALLOWED_EVENTS = [pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN, pg.KEYUP, pg.KEYDOWN, pg.QUIT]

BASIC_CAPTION = 'Code Names'
MENU_CAPTION = 'Main Menu'

WORD_CATEGORIES = ["words_list"]  # TODO should be chosen on the starting screen

# Colors

#               R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = (60,  60,  100)
WHITE        = (255, 255, 255)
RED          = (255, 0,   0)
GREEN        = (0,   255, 0)
FOREST_GREEN = (31,  162, 35)
BLUE         = (0,   0,   255)
SKY_BLUE     = (39,  145, 251)
YELLOW       = (255, 255, 0)
ORANGE       = (255, 128, 0)
PURPLE       = (255, 0, 255)
CYAN         = (0,   255, 255)
BLACK        = (0,   0,   0)
NEAR_BLACK   = (19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215, 0)

BGCOLOR = BLACK

MULTIPLIER = SCREEN_HEIGHT/1080

# WordCard states
COVERED = 'covered'
UNCOVERED = 'uncovered'

# Screen states
MAIN_MENU = 'main menu'
FIELD_OPERATIVE = 'field operative'
SPYMASTER = 'spymaster'
STARTING_SCREEN = 'starting screen'

# Game info dictionary keys
TEAM1 = 'first team'
TEAM2 = 'second team'
CURRENT_TIME = 'current time'
GAME_OVER = 'game over'
WORD_CARDS = 'word cards'
CLUE = 'clue'

# Word card
# Statuses
REVEALED = 'revealed'
HIDDEN = 'hidden'
# Type
RED_CARD = 'red'
BLUE_CARD = 'blue'
BYSTANDER = 'bystander'
ASSASSIN = 'assassin'

# Text boxes types
WORD = 'word'
NUMBER = 'number'

# Sound states
# TODO
