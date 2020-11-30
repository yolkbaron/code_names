from . import tools
from .screens import field_operative_screen, main_menu, spymaster_screen, starting_screen
from . import constants as c


def main():
    game = tools.Game(c.BASIC_CAPTION)
    screen_dict = {c.FIELD_OPERATIVE: field_operative_screen.FiledOperative,
                   c.MAIN_MENU: main_menu.MainMenu,
                   c.SPYMASTER: spymaster_screen.SpyMaster,
                   c.STARTING_SCREEN: starting_screen.StartingScreen
                   }
    game.set_screens(screen_dict, c.STARTING_SCREEN)
    game.main()
    print loa
