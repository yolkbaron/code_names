import pygame as pg
from ..game_components import button
from .. import setup, tools
from .. import constants as c
from ..game_components import text_box


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
        self.set_textboxes()
        self.set_buttons()

    def set_background(self):
        self.background = setup.SPRITES["background"]
        font = pg.font.Font(setup.FONTS["Marlboro"], int(300 * self.multiplier))
        title = font.render("CODE NAMES", True, c.GOLD)
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)
        self.background.blit(title, (int(80 * self.multiplier), int(80 * self.multiplier)))

    def set_buttons(self):
        start_button = button.Button(
            int(450 * self.multiplier),
            int(400 * self.multiplier),
            int(400 * self.multiplier),
            int(200 * self.multiplier),
            "Start",
            int(150 * self.multiplier),
            "Bullpen3D"
        )
        start_button.set_inactive(c.WHITE)
        start_button.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["start"] = start_button

    def set_textboxes(self):
        spy1 = text_box.InputBox(0, 0, 200, 200, c.WHITE, 50, "Bullpen3D")
        self.text_boxes["spy_1"] = spy1

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