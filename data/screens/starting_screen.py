import pygame as pg
from ..game_components import button
from .. import setup, tools
from .. import constants as c
from ..game_components import text_box


class StartingScreen(tools.GameState):

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.STARTING_SCREEN
        game_info = {
            c.TEAM1_SCORE: 0,
            c.TEAM2_SCORE: 0,
            c.TEAM1_SPY: None,
            c.TEAM1_OPERATIVE1: None,
            c.TEAM1_OPERATIVE2: None,
            c.TEAM2_OPERATIVE1: None,
            c.TEAM2_OPERATIVE2: None
        }
        self.start(0.0, game_info)
        self.fonts = setup.FONTS

    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info
        self.next = self.get_next_screen()

        self.set_background()
        self.set_textboxes()
        self.set_buttons()

    def set_background(self):
        self.background = setup.SPRITES["background2"]
        font = pg.font.Font(setup.FONTS["Top Secret"], int(100 * self.multiplier))
        team_blue = font.render("Team blue", True, c.BLUE)
        team_red = font.render("Team red", True, c.RED)
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)
        self.background.blit(team_blue, (int(260 * self.multiplier), int(270 * self.multiplier)))
        self.background.blit(team_red, (int(1100 * self.multiplier), int(100 * self.multiplier)))

    def set_buttons(self):
        start_button = button.Button(
            int(180 * self.multiplier),
            int(820 * self.multiplier),
            int(600 * self.multiplier),
            int(200 * self.multiplier),
            "START",
            int(150 * self.multiplier),
            "Top Secret"
        )
        start_button.set_inactive(c.GRAY)
        start_button.set_active(c.RED)
        self.buttons["start"] = start_button

    def set_textboxes(self):
        spy1 = text_box.InputBox(220, 435, 500, 100, c.BLUE, 100, "top secret text")
        spy2 = text_box.InputBox(1100, 250, 500, 100, c.RED, 100, "top secret text")
        team1_operative1 = text_box.InputBox(220, 555, 500, 100, c.BLUE, 100, "top secret text")
        team2_operative1 = text_box.InputBox(1100, 370, 500, 100, c.RED, 100, "top secret text")
        team1_operative2 = text_box.InputBox(220, 675, 500, 100, c.BLUE, 100, "top secret text")
        team2_operative2 = text_box.InputBox(1100, 490, 500, 100, c.RED, 100, "top secret text")
        self.text_boxes["team1_spy"] = spy1
        self.text_boxes["team2_spy"] = spy2
        self.text_boxes["team1_operative1"] = team1_operative1
        self.text_boxes["team2_operative1"] = team2_operative1
        self.text_boxes["team1_operative2"] = team1_operative2
        self.text_boxes["team2_operative2"] = team2_operative2

    def update(self, surface, keys, mouse, current_time):
        surface.blit(self.background, (0, 0))
        self.cursor_pos = pg.mouse.get_pos()
        self.update_text_boxes(surface)
        self.update_buttons(surface)

    def update_text_boxes(self, surface):
        for key in self.text_boxes.keys():
            self.text_boxes[key].update()
            self.text_boxes[key].draw(surface)

    def update_buttons(self, surface):
        for key in self.buttons.keys():
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False
            if self.buttons[key].pressed:
                self.buttons[key].pressed = False
                if key == "start":
                    self.done = True
            self.buttons[key].draw(surface)
