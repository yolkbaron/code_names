import pygame as pg
from ..game_components import button
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
        self.background = setup.SPRITES["background2"]
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)

    def set_buttons(self):
        all_words = setup.WORDS["words_list"]
        words = []
        order = random.sample(range(0, 187), 20)
        for i in order:
            words.append(all_words[i])
        print(words)

        word1 = button.Button(
            int(150 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[0],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word1.set_inactive(c.WHITE)
        word1.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word1"] = word1

        word2 = button.Button(
            int(450 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[1],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word2.set_inactive(c.WHITE)
        word2.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word2"] = word2

        word3 = button.Button(
            int(750 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[2],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word3.set_inactive(c.WHITE)
        word3.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word3"] = word3

        word4 = button.Button(
            int(1050 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[3],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word4.set_inactive(c.WHITE)
        word4.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word4"] = word4

        word5 = button.Button(
            int(1350 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[4],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word5.set_inactive(c.WHITE)
        word5.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word5"] = word5

        word6 = button.Button(
            int(150 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[5],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word6.set_inactive(c.WHITE)
        word6.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word6"] = word6

        word7 = button.Button(
            int(450 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[6],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word7.set_inactive(c.WHITE)
        word7.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word7"] = word7

        word8 = button.Button(
            int(750 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[7],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word8.set_inactive(c.WHITE)
        word8.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word8"] = word8

        word9 = button.Button(
            int(1050 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[8],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word9.set_inactive(c.WHITE)
        word9.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word9"] = word9

        word10 = button.Button(
            int(1350 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[9],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word10.set_inactive(c.WHITE)
        word10.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word10"] = word10

        word11 = button.Button(
            int(150 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[10],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word11.set_inactive(c.WHITE)
        word11.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word11"] = word11

        word12 = button.Button(
            int(450 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[11],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word12.set_inactive(c.WHITE)
        word12.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word12"] = word12

        word13 = button.Button(
            int(750 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[12],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word13.set_inactive(c.WHITE)
        word13.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word13"] = word13

        word14 = button.Button(
            int(1050 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[13],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word14.set_inactive(c.WHITE)
        word14.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word14"] = word14

        word15 = button.Button(
            int(1350 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[14],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word15.set_inactive(c.WHITE)
        word15.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word15"] = word15

        word16 = button.Button(
            int(150 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[15],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word16.set_inactive(c.WHITE)
        word16.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word16"] = word16

        word17 = button.Button(
            int(450 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[16],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word17.set_inactive(c.WHITE)
        word17.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word17"] = word17

        word18 = button.Button(
            int(750 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[17],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word18.set_inactive(c.WHITE)
        word18.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word18"] = word18

        word19 = button.Button(
            int(1050 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[18],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word19.set_inactive(c.WHITE)
        word19.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word19"] = word19

        word20 = button.Button(
            int(1350 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[19],
            int(50 * self.multiplier),
            "Bullpen3D"
        )
        word20.set_inactive(c.WHITE)
        word20.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["word20"] = word20



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