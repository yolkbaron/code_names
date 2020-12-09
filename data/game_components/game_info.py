import pygame as pg
from .. import constants as c
from .. import setup


class Player:
    """Class for every player to store information about player"""

    # TODO
    def __init__(self, name, team, type):
        self.name = name
        self.team = team
        self.type = type


class Team:
    # TODO
    """Class for both teams to store information about teams"""

    def __init__(self, name):
        self.spy = None
        self.field_operative = None
        self.color = None

    def set_spy(self, name):
        self.spy = Player(name, self.color, "spy")

    def set_field_operative(self, name):
        self.field_operative = Player(name, self.color, "field operative")


def create_team(name, team_order, spy_name, field_operative_name):
    team = Team(name)
    team.set_spy(spy_name)
    team.set_field_operative(field_operative_name)
    if team_order == 1:
        team.color = "red"
    elif team_order == 2:
        team.color = "blue"
    else:
        raise ValueError("Only 2 teams possible")
    return team


class GameInfo(object):
    """Class to store and draw game information like options, time remaining, tables of players, text in every screen"""

    # TODO game design required
    def __init__(self):
        self.sprite = setup.SPRITES['font_sprite']
        self.char_image_dict = {}

    def load_char_images(self):
        """Loads character image dictionary with images of characters"""
        pass
