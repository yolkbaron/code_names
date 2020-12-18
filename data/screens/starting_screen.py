import pygame as pg
from ..game_components import button
from ..game_components import text_bocks
from .. import setup, tools
from .. import constants as c


class StartingScreen(tools.GameState):

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.STARTING_SCREEN
        game_info = {}
        self.start(0.0, game_info)
        self.fonts = setup.FONTS

    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info
        self.next = self.get_next_screen()

        self.set_background()
        self.set_textbocks()

    def set_background(self):
        self.background = setup.SPRITES["background"]
        font = pg.font.Font(setup.FONTS["Marlboro"], int(300 * self.multiplier))
        title = font.render("CODE NAMES", True, c.GOLD)
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)
        self.background.blit(title, (int(80 * self.multiplier), int(80 * self.multiplier)))

    def set_textbocks(self):
        pass

    def update(self, surface, keys, mouse, current_time):
        surface.blit(self.background, (0, 0))
        self.cursor_pos = pg.mouse.get_pos()

        for key in self.text_boxes.keys():
            self.text_boxes[key].update()
            self.text_boxes[key].draw()




