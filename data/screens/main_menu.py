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
        self.background = setup.SPRITES["background"]
        font = pg.font.Font(setup.FONTS["Marlboro"], int(300*self.multiplier))
        title = font.render("CODE NAMES", True, c.GOLD)
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)
        self.background.blit(title, (int(80*self.multiplier), int(80*self.multiplier)))

    def set_buttons(self):
        play_button = button.Button(
            int(450 * self.multiplier),
            int(400 * self.multiplier),
            int(400 * self.multiplier),
            int(200 * self.multiplier),
            "Play",
            int(150 * self.multiplier),
            "Bullpen3D"
        )
        play_button.set_inactive(c.WHITE)
        play_button.set_active(c.WHITE, setup.SPRITES["button_active"])
        exit_button = button.Button(
            int(450 * self.multiplier),
            int(700 * self.multiplier),
            int(400 * self.multiplier),
            int(200 * self.multiplier),
            "Exit",
            int(150 * self.multiplier),
            "Bullpen3D"
        )
        exit_button.set_inactive(c.WHITE)
        exit_button.set_active(c.WHITE, setup.SPRITES["button_active"])
        self.buttons["play"] = play_button
        self.buttons["exit"] = exit_button

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
