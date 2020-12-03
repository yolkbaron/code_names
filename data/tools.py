import os
import pygame as pg
from . import constants as c


class Game(object):
    """
    Class for handling entire project. Contains game, event and main loops.
    """

    # TODO
    def __init__(self, caption):
        self.caption = caption
        self.screen = pg.display.get_surface()
        self.fps = c.FPS
        self.clock = pg.time.Clock()
        self.done = False
        self.current_time = 0.0
        self.state = None  # GameState
        self.screen_dict = {}
        self.screen = None
        self.screen_name = None

    def update(self):
        """
        Updates time. Then checks if state.quit, if not changes current state.
        :return: None
        """
        # TODO
        pass

    def event_loop(self):
        """
        Handles event.
        :return: None
        """
        # TODO
        pass

    def main_loop(self):
        """
        Main loop.
        :return: None
        """
        # TODO
        pass

    def set_screens(self, screen_dict, current_screen_name):
        """
        Sets self.screen_dict, self.screen_name, self.screen with data given.
        :param screen_dict: dictionary of all screens
        :param current_screen_name: starting state
        :return: None
        """
        # TODO
        pass


class GameState(object):
    """
    Contains current previous and next states of Game.
    """

    # TODO
    def __init__(self):
        self.done = False


def load_all_words(directory, extensions='.txt'):
    """
    Loads all words of given categories from given directory.
    :param directory: Directory with words
    :param extensions: Allowed extensions os files with words
    :return: List of words
    """
    words = {}
    for word_file in os.listdir(directory):
        path = os.path.join(directory, word_file)
        with open(path, encoding="utf-8") as file:
            category_key, extension = os.path.splitext(word_file)
            category = []
            if extension in extensions:
                for line in file:
                    category.append(line.rstrip())
                words[category_key] = category
    return words


def load_all_sounds(directory, extensions=()):
    """
    Loads all sounds from given directory.
    :param directory: Directory with sounds
    :param extensions: Allowed extensions for sound files
    :return: Sounds dictionary
    """
    sounds = {}
    for sound_file in os.listdir(directory):
        name, extension = os.path.splitext(sound_file)
        if extension.lower() in extensions:
            sounds[name] = pg.mixer.Sound(os.path.join(directory, sound_file))
    return sounds


def load_all_music(directory, extensions=()):
    """
    Loads all music from given directory.
    :param directory: Directory with music
    :param extensions: Allowed extensions for music files
    :return: Music dictionary
    """
    music = {}
    for music_file in os.listdir(directory):
        name, extension = os.path.splitext(music_file)
        if extension.lower() in extensions:
            music[name] = os.path.join(directory, music_file)
    return music


def load_all_sprites(directory, extensions=()):
    """
    Loads all sprites from given directory.
    :param directory: Directory with sprites
    :param extensions: Allowed extensions for sprite files
    :return: Sprite dictionary
    """
    sprites = {}
    for sprite_file in os.listdir(directory):
        name, extension = os.path.splitext(sprite_file)
        if name.lower() in extensions:
            sprites[name] = pg.image.load(os.path.join(directory, sprite_file))
    return sprites
