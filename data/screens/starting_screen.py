import pygame as pg
from .. import setup, tools
from .. import constants as c


class StartingScreen(tools.GameState):

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.STARTING_SCREEN
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

        """self.screen = pg.display.set_mode((1000, 1000))  # FIXME screen size is in constants
        f1 = pg.font.Font(None, 80)
        f2 = pg.font.Font(None, 50)
        text1 = f1.render('Приветствую вас странники!', True, c.RED)
        text2 = f2.render('Если ты хотел сыграть в CodeNames,', True, c.RED)
        text3 = f2.render('то ты попал прямо по адресу.', True, c.RED)
        text4 = f2.render('Для начала игры ознакомтесь с инсрукцией.', True, c.RED)
        text5 = f2.render('Теперь смело жми на старт!', True, c.RED)
        self.screen.blit(text1, (120, 100))  # FIXME
        self.screen.blit(text2, (200, 200))  # FIXME
        self.screen.blit(text3, (260, 250))  # FIXME
        self.screen.blit(text4, (130, 500))  # FIXME
        self.screen.blit(text5, (260, 550))  # FIXME"""

