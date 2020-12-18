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
        self.next = self.get_next_screen()

    def set_background(self):
        self.background = setup.SPRITES["background2"]
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
        rad = random.sample(all, 7)
        for i in rad:
            all.remove(i)
            color.remove(i)
            color.insert(i, "red")
        white = random.sample(all, 6)
        for i in white:
            all.remove(i)
            color.remove(i)
            color.insert(i, "light-yellow")
        color[all[0]] = "purple"


        word1 = word_card.WordCard(
            int(150 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[0],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[0]
        )
        word1.capitane = True
        word1.set_capitane(c.BLACK, setup.SPRITES[word1.color])
        self.buttons["word1"] = word1

        word2 = word_card.WordCard(
            int(450 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[1],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[1]
        )
        word2.capitane = True
        word2.set_capitane(c.BLACK, setup.SPRITES[word2.color])
        self.buttons["word2"] = word2

        word3 = word_card.WordCard(
            int(750 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[2],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[2]
        )
        word3.capitane = True
        word3.set_capitane(c.BLACK, setup.SPRITES[word3.color])
        self.buttons["word3"] = word3

        word4 = word_card.WordCard(
            int(1050 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[3],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[3]
        )
        word4.capitane = True
        word4.set_capitane(c.BLACK, setup.SPRITES[word4.color])
        self.buttons["word4"] = word4

        word5 = word_card.WordCard(
            int(1350 * self.multiplier),
            int(300 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[4],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[4]
        )
        word5.capitane = True
        word5.set_capitane(c.BLACK, setup.SPRITES[word5.color])
        self.buttons["word5"] = word5

        word6 = word_card.WordCard(
            int(150 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[5],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[5]
        )
        word6.capitane = True
        word6.set_capitane(c.BLACK, setup.SPRITES[word6.color])
        self.buttons["word6"] = word6

        word7 = word_card.WordCard(
            int(450 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[6],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[6]
        )
        word7.capitane = True
        word7.set_capitane(c.BLACK, setup.SPRITES[word7.color])
        self.buttons["word7"] = word7

        word8 = word_card.WordCard(
            int(750 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[7],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[7]
        )
        word8.capitane = True
        word8.set_capitane(c.BLACK, setup.SPRITES[word8.color])
        self.buttons["word8"] = word8

        word9 = word_card.WordCard(
            int(1050 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[8],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[8]
        )
        word9.capitane = True
        word9.set_capitane(c.BLACK, setup.SPRITES[word9.color])
        self.buttons["word9"] = word9

        word10 = word_card.WordCard(
            int(1350 * self.multiplier),
            int(460 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[9],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[9]
        )
        word10.capitane = True
        word10.set_capitane(c.BLACK, setup.SPRITES[word10.color])
        self.buttons["word10"] = word10

        word11 = word_card.WordCard(
            int(150 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[10],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[10]
        )
        word11.capitane = True
        word11.set_capitane(c.BLACK, setup.SPRITES[word11.color])
        self.buttons["word11"] = word11

        word12 = word_card.WordCard(
            int(450 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[11],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[11]
        )
        word12.capitane = True
        word12.set_capitane(c.BLACK, setup.SPRITES[word12.color])
        self.buttons["word12"] = word12

        word13 = word_card.WordCard(
            int(750 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[12],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[12]
        )
        word13.capitane = True
        word13.set_capitane(c.BLACK, setup.SPRITES[word13.color])
        self.buttons["word13"] = word13

        word14 = word_card.WordCard(
            int(1050 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[13],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[13]
        )
        word14.capitane = True
        word14.set_capitane(c.BLACK, setup.SPRITES[word14.color])
        self.buttons["word14"] = word14

        word15 = word_card.WordCard(
            int(1350 * self.multiplier),
            int(620 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[14],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[14]
        )
        word15.capitane = True
        word15.set_capitane(c.BLACK, setup.SPRITES[word15.color])
        self.buttons["word15"] = word15

        word16 = word_card.WordCard(
            int(150 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[15],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[15]
        )
        word16.capitane = True
        word16.set_capitane(c.BLACK, setup.SPRITES[word16.color])
        self.buttons["word16"] = word16

        word17 = word_card.WordCard(
            int(450 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[16],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[16]
        )
        word17.capitane = True
        word17.set_capitane(c.BLACK, setup.SPRITES[word17.color])
        self.buttons["word17"] = word17

        word18 = word_card.WordCard(
            int(750 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[17],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[17]
        )
        word18.capitane = True
        word18.set_capitane(c.BLACK, setup.SPRITES[word18.color])
        self.buttons["word18"] = word18

        word19 = word_card.WordCard(
            int(1050 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[18],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[18]
        )
        word19.capitane = True
        word19.set_capitane(c.BLACK, setup.SPRITES[word19.color])
        self.buttons["word19"] = word19

        word20 = word_card.WordCard(
            int(1350 * self.multiplier),
            int(780 * self.multiplier),
            int(300 * self.multiplier),
            int(150 * self.multiplier),
            words[19],
            int(50 * self.multiplier),
            "Bullpen3D",
            color[19]
        )
        word20.capitane = True
        word20.set_capitane(c.BLACK, setup.SPRITES[word20.color])
        self.buttons["word20"] = word20

        play_button = button.Button(
            int(1100 * self.multiplier),
            int(60 * self.multiplier),
            int(400 * self.multiplier),
            int(200 * self.multiplier),
            "Next",
            int(150 * self.multiplier),
            "Bullpen3D"
        )
        play_button.set_inactive(c.BLACK)
        play_button.set_active(c.BLACK, setup.SPRITES["button_active"])
        self.buttons["next"] = play_button



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
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False
            if self.buttons[key].pressed:
                self.buttons[key].pressed = False
                if key == "next":
                    self.done = True
