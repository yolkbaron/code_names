import pygame as pg
from ..game_components import button
from ..game_components import word_card
from ..game_components import text_box
from .. import setup, tools
from .. import constants as c
import random


class FieldOperative(tools.GameState):
    """
    Field operative screen class
    """

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.FIELD_OPERATIVE
        self.cursor_pos = pg.mouse.get_pos()
        self.fonts = setup.FONTS
        self.turn = "red"


    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info
        self.next = self.get_next_screen()

        self.set_background()
        self.set_buttons()
        self.set_cards()

    def set_background(self):
        self.background = setup.SPRITES["background3"].copy()
        font = pg.font.Font(self.fonts["top secret text"], int(100 * self.multiplier))
        txt_surface = font.render(self.game_info[c.CLUE].upper(), True, c.WHITE)
        number_surface = font.render(self.game_info[c.NUMBER], True, c.WHITE)
        self.background.blit(txt_surface, (0, 0))
        self.background.blit(number_surface, (int(800 * self.multiplier), 0))
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)

    def set_cards(self):
        self.word_cards = self.game_info[c.WORD_CARDS]

    def set_buttons(self):
        end_turn_button = button.Button(
            int(1670 * self.multiplier),
            int(20 * self.multiplier),
            int(220 * self.multiplier),
            int(50 * self.multiplier),
            "End Turn",
            int(50 * self.multiplier),
            "Marlboro"
        )
        end_turn_button.set_inactive(c.WHITE)
        end_turn_button.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["end turn"] = end_turn_button

    def update(self, surface, keys, mouse, current_time):
        surface.blit(self.background, (0, 0))
        self.cursor_pos = pg.mouse.get_pos()

        self.update_buttons()
        self.update_word_cards()

        self.draw_buttons(surface)
        self.draw_word_cards(surface)
        self.draw_text_boxes(surface)

    def draw_buttons(self, surface):
        for key in self.buttons.keys():
            self.buttons[key].draw(surface)

    def draw_word_cards(self, surface):
        for i in range(20):
            self.word_cards[i].draw_operative_screen(surface)

    def draw_text_boxes(self, surface):
        for key in self.text_boxes.keys():
            self.text_boxes[key].draw(surface)

    def update_buttons(self):
        for key in self.buttons.keys():
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False
            if self.buttons[key].pressed:
                self.buttons[key].pressed = False
                if key == "end turn" and self.game_info[c.CLUE]:
                    self.done = True

    def update_word_cards(self):
        for i in range(20):
            if self.word_cards[i].check_crossing(self.cursor_pos):
                self.word_cards[i].active = True
            else:
                self.word_cards[i].active = False
            if self.word_cards[i].pressed:
                self.word_cards[i].pressed = False
                self.word_cards[i].reveal()
                if (self.turn == "red") and (self.word_cards[i].type != c.RED_CARD) and (self.word_cards[i].type != c.ASSASSIN):
                    self.turn = "blue"
                    self.done = True
                if (self.turn == "blue") and (self.word_cards[i].type != c.BLUE_CARD) and (self.word_cards[i].type != c.ASSASSIN):
                    self.turn = "red"
                    self.done = True



            self.word_cards[i].update()
