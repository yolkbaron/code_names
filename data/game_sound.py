import pygame as pg
from . import setup
from . import constants as c


class Music(object):

    def __init__(self, overhead_info):
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()

    def set_music_mixer(self):

        if self.overhead_info.state == c.LEVEL:
            pg.mixer.music.load(self.music_dict['main_theme'])
            pg.mixer.music.play()
            self.state = c.NORMAL
        elif self.overhead_info.state == c.GAME_OVER:
            pg.mixer.music.load(self.music_dict['game_over'])
            pg.mixer.music.play()
            self.state = c.GAME_OVER

    def update(self, game_info):
        self.game_info = game_info

    def play_music(self, key, state):
        pg.mixer.music.load(self.music_dict[key])
        pg.mixer.music.play()
        self.state = state

    def stop_music(self):
        pg.mixer.music.stop()
