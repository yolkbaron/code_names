import os
import pygame as pg
from . import constants


class Game(object):
    """
    Class for handling entire project. Contains game, event and main loops.
    """

    def __init__(self, caption):
        self.caption = caption
        self.display = pg.display.get_surface()
        self.fps = constants.FPS
        self.clock = pg.time.Clock()
        self.done = False
        self.current_time = 0.0
        self.state = None  # GameState
        self.screen_dict = {}
        self.screen_name = None
        self.keys = pg.key.get_pressed()  # List of all keys pressed
        self.mouse = pg.mouse.get_pressed(3)

    def switch_state(self):
        """
        State switching logic
        :return: None
        """
        self.screen_name = self.state.next
        self.state = self.screen_dict[self.screen_name]
        self.state.start(self.current_time, self.state.game_info)

    def update(self):
        """
        Updates time. Then checks if state.quit, if not changes current state.
        :return: None
        """
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.switch_state()
        self.state.update(self.display, self.keys, self.mouse, self.current_time)

    def event_loop(self):
        """
        Handles event.
        :return: None
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.state.mouse_button_pressed(event)
            elif event.type == pg.KEYDOWN:
                self.state.key_pressed(event)

    def main_loop(self):
        """
        Main loop.
        :return: None
        """
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
        pg.quit()

    def set_screens(self, screen_dict, current_screen_name):
        """
        Sets self.screen_dict, self.screen_name, self.screen with data given.
        :param screen_dict: dictionary of all screens
        :param current_screen_name: starting state
        :return: None
        """
        self.screen_dict = screen_dict
        self.screen_name = current_screen_name
        self.state = self.screen_dict[self.screen_name]


class GameState(object):
    """
    Contains current and next states of Game.
    """

    def __init__(self):
        self.multiplier = constants.MULTIPLIER
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.game_info = {}
        self.buttons = {}
        self.cards = {}
        self.text_boxes = {}
        self.cursor_pos = pg.mouse.get_pos()

    def mouse_button_pressed(self, event):
        if event.button == 1:
            for key in self.buttons.keys():
                if self.buttons[key].check_crossing(self.cursor_pos):
                    self.buttons[key].pressed = True
            for key in self.cards.keys():
                if self.cards[key].check_crossing(self.cursor_pos):
                    self.cards[key].pressed = True
            for key in self.text_boxes.keys():
                if self.text_boxes[key].check_crossing(self.cursor_pos):
                    self.text_boxes[key].active = True
                else:
                    self.text_boxes[key].active = False

    def key_pressed(self, event):
        for key in self.text_boxes.keys():
            if self.text_boxes[key].active:
                if event.key == pg.K_RETURN:
                    self.text_boxes[key].text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text_boxes[key].text = self.text_boxes[key].text[:-1]
                else:
                    self.text_boxes[key].text += event.unicode
                self.text_boxes[key].txt_surface = self.text_boxes[key].font.render(self.text_boxes[key].text, True,
                                                                                    self.text_boxes[key].text_color)

    def update(self, surface, keys, mouse, current_time):
        """
        Depends from the specific screen
        :return: None
        """
        pass

    def start(self, current_time, game_info):
        """
        Depends from the specific screen
        :param current_time: Absolute time of the game
        :param game_info: GameInfo object
        :return: None
        """
        self.game_info = game_info
        self.start_time = current_time

    def get_next_screen(self):
        """
        Returns next screen according to the name of current screen
        :return: Next screen from constants
        """
        if self.name == constants.MAIN_MENU:
            next = constants.STARTING_SCREEN
        if self.name == constants.STARTING_SCREEN:
            next = constants.SPYMASTER
        if self.name == constants.SPYMASTER:
            next = constants.FIELD_OPERATIVE
        if self.name == constants.FIELD_OPERATIVE:
            next = constants.SPYMASTER
        return next


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


def load_all_sprites(directory, extensions=(".jpg", ".png")):
    """
    Loads all sprites from given directory.
    :param directory: Directory with sprites
    :param extensions: Allowed extensions for sprite files
    :return: Sprite dictionary
    """
    sprites = {}
    for sprite_file in os.listdir(directory):
        name, extension = os.path.splitext(sprite_file)
        if extension.lower() in extensions:
            sprites[name] = pg.image.load(os.path.join(directory, sprite_file))
    return sprites


def load_all_fonts(directory, extensions=(".ttf", ".otf")):
    """
    Loads all sprites from given directory.
    :param directory: Directory with sprites
    :param extensions: Allowed extensions for sprite files
    :return: Sprite dictionary
    """
    fonts = {}
    for font_file in os.listdir(directory):
        name, extension = os.path.splitext(font_file)
        if extension.lower() in extensions:
            fonts[name] = os.path.abspath(os.path.join(directory, font_file))
    return fonts
