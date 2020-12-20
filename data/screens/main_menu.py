import pygame as pg
from ..game_components import button
from .. import setup, tools
from .. import constants as c
from ..game_components import player_module
from .. import game_sound


class MainMenu(tools.GameState):
    """
    Main menu screen class
    """

    def __init__(self):
        tools.GameState.__init__(self)
        self.name = c.MAIN_MENU
        team1 = player_module.Team("blue")
        team2 = player_module.Team("red")
        game_info = {
            c.TEAM1: team1,
            c.TEAM2: team2,
            c.CURRENT_TIME: None,
            c.GAME_OVER: False,
            c.WORD_CARDS: None,
            c.CLUE: None,
            c.NUMBER: None
        }
        self.start(0.0, game_info)
        self.fonts = setup.FONTS

    def start(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info
        self.next = self.get_next_screen()

        self.set_background()
        self.set_buttons()

    def set_background(self):
        self.background = setup.SPRITES["background1"]
        font = pg.font.Font(setup.FONTS["Marlboro"], int(300*self.multiplier))
        title = font.render("CODENAMES", True, c.GOLD)
        self.background = pg.transform.scale(self.background, c.SCREEN_SIZE)
        self.background.blit(title, (int(80*self.multiplier), int(80*self.multiplier)))

    def set_buttons(self):
        play_button = button.Button(
            int(400 * self.multiplier),
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
            int(400 * self.multiplier),
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
        self.cursor_pos = pg.mouse.get_pos()
        self.update_buttons(surface)

    def update_buttons(self, surface):
        for key in self.buttons.keys():
            if self.buttons[key].check_crossing(self.cursor_pos):
                self.buttons[key].active = True
            else:
                self.buttons[key].active = False
            if self.buttons[key].pressed:
                self.buttons[key].pressed = False
                if key == "exit":
                    self.quit = True
                if key == "play":
                    self.done = True
            self.buttons[key].draw(surface)
