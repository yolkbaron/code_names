import pygame as pg
from ..game_components import button
from ..game_components import word_card
from .. import setup, tools
from .. import constants as c
import random


class SpyMaster(tools.GameState):
    """
    Spy master screen class
    """

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.SPYMASTER
        game_info = {}
        self.start(0.0, game_info)
        self.cursor_pos = pg.mouse.get_pos()
        self.fonts = setup.FONTS

    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info

        self.set_background()
        self.set_buttons()

    def set_background(self):
        self.background = setup.SPRITES["background3"]
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)

    def set_buttons(self):
        all_words = setup.WORDS["words_list"]
        words = []
        order = random.sample(range(0, 187), 20)
        for i in order:
            words.append(all_words[i])
        all = list(range(20))
        color = list(range(20))
        blue = random.sample(range(0, 20), 6)
        for i in blue:
            all.remove(i)
            color.remove(i)
            color.insert(i, "blue")
        red = random.sample(all, 7)
        for i in red:
            all.remove(i)
            color.remove(i)
            color.insert(i, "red")
        white = random.sample(all, 6)
        for i in white:
            all.remove(i)
            color.remove(i)
            color.insert(i, "light-yellow")
        color[all[0]] = "purple"

        word_cards = []

        for i in range(4):
            for j in range(5):
                word = word_card.WordCard(
                    int((190 + 310*j) * self.multiplier),
                    int((400 + 160*i) * self.multiplier),
                    int(300 * self.multiplier),
                    int(150 * self.multiplier),
                    words[5*i+j],
                    int(50 * self.multiplier),
                    "top secret text",
                    color[5*i+j]
                )
                word.captain = True
                word.set_captain(c.BLACK, setup.SPRITES[word.color])
                self.buttons["word" + str(5*i+j)] = word

    def update(self, surface, keys, mouse, current_time):
        surface.blit(self.background, (0, 0))
        self.draw_buttons(surface)
        self.cursor_pos = pg.mouse.get_pos()

        for key in self.buttons.keys():
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False

        self.buttons_processing()

    def draw_buttons(self, surface):
        for key in self.buttons.keys():
            self.buttons[key].draw(surface)

    def buttons_processing(self):
        for key in self.buttons.keys():
            if self.buttons[key].pressed:
                self.buttons[key].pressed = False
                if key == "exit":
                    self.quit = True
