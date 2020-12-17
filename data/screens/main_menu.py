import pygame as pg
from .. import setup, tools
from .. import constants as c


class MainMenu(tools.GameState):
    """
    Main menu screen class
    """

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.MAIN_MENU
        self.quit = False
        game_info = {}
        self.start(0.0, game_info)

    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info

        self.set_background()
        self.set_buttons()

    def set_background(self):
        self.background = setup.SPRITES["background"]
        self.background_rect = self.background.get_rect()

        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)

    def set_buttons(self):
        self.buttons = {}

    def update(self, surface, keys, current_time):
        surface.blit(self.background, (0, 0))
