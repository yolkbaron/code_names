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
        self.cursor_pos = pg.mouse.get_pos()
        self.fonts = setup.FONTS

    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info
        self.next = self.get_next_screen()

        self.set_background()
        self.set_buttons()
        self.set_cards()

    def set_background(self):
        self.background = setup.SPRITES["background3"]
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)

    def set_cards(self):
        words = setup.WORDS["words_list"]
        random.shuffle(words)
        types = ["blue"]*6 + ["red"]*7 + ["bystander"]*6 + ["assassin"]
        random.shuffle(types)

        word_cards = []

        for i in range(4):
            for j in range(5):
                word = word_card.WordCard(
                    int((190 + 310*j) * self.multiplier),
                    int((400 + 160*i) * self.multiplier),
                    int(300 * self.multiplier),
                    int(150 * self.multiplier),
                    types[5*i+j],
                    words[5*i+j],
                    int(50 * self.multiplier),
                    "top secret text"

                )
                word_cards.append(word)

        self.word_cards = word_cards

    def set_buttons(self):
        play_button = button.Button(
             int(450 * self.multiplier),
             int(60 * self.multiplier),
             int(400 * self.multiplier),
              int(200 * self.multiplier),
              "Next",
              int(150 * self.multiplier),
              "Bullpen3D"
        )
        play_button.set_inactive(c.WHITE)
        play_button.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["next"] = play_button

    def update(self, surface, keys, mouse, current_time):
        surface.blit(self.background, (0, 0))
        self.cursor_pos = pg.mouse.get_pos()
        self.update_buttons()

        for key in self.buttons.keys():
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False

        self.update_buttons()
        self.update_word_cards()

        self.draw_buttons(surface)
        self.draw_word_cards(surface)

    def draw_buttons(self, surface):
        for key in self.buttons.keys():
            self.buttons[key].draw(surface)

    def draw_word_cards(self, surface):
        for i in range(20):
            self.word_cards[i].draw_spy_screen(surface)

    def update_buttons(self):
        for key in self.buttons.keys():
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False
            if self.buttons[key].pressed:
                self.buttons[key].pressed = False

    def update_word_cards(self):
        for i in range(20):
            if self.word_cards[i].check_crossing(self.cursor_pos):
                self.word_cards[i].active = True
            else:
                self.word_cards[i].active = False
            if self.word_cards[i].pressed:
                self.word_cards[i].pressed = False
            self.word_cards[i].update()