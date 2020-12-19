import pygame as pg
from .. import constants as c
from .. import setup


class Player:
    """Class for every player to store information about player"""
    def __init__(self, name, team, type):
        self.name = name
        self.team = team
        self.type = type


class Team:
    """Class for both teams to store information about teams"""
    def __init__(self, name):
        self.spy = None
        self.operatives = [None, None]
        self.name = name
        self.score = 0

    def set_spy(self, name):
        if name:
            self.spy = Player(name, self.name, "spy")
        else:
            self.spy = None

    def set_operative(self, name, number):
        if name:
            self.operatives[number]= Player(name, self.name, "field operative")
        else:
            self.operatives[number] = None

    def is_complete(self):
        if self.spy and self.operatives[0]:
            return True
        else:
            return False
