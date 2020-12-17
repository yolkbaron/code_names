import pygame as pg
from ..game_components import button
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
        start = button.Button()
        start.create_button(20, 20, 300, 200, "start", 100, c.BLUE)
        surface.blit(start.button_image, (start.x, start.y))
