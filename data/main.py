from . import tools
from .screens import field_operative_screen, main_menu, spymaster_screen, starting_screen
from . import constants


def main():
    game = tools.Game(constants.BASIC_CAPTION)
    screen_dict = {constants.FIELD_OPERATIVE: field_operative_screen.FieldOperative(),
                   constants.MAIN_MENU: main_menu.MainMenu(),
                   constants.SPYMASTER: spymaster_screen.SpyMaster(),
                   constants.STARTING_SCREEN: starting_screen.StartingScreen()
                   }
    game.set_screens(screen_dict, constants.MAIN_MENU)
    game.main_loop()
