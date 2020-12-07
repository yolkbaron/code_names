import pygame as pg


class Button(object):
    """
    Class for handling mouse clicking event.
    """

    def create_button(self, x, y, width, height):
        """
        Adds button to given screen.
        :param state: GameState
        :param x: top-left x position of button
        :param y: top-left y position of button
        :param width: Width of button
        :param height: Height of button
        :return: Button object
        """
        # TODO

    def remove_button(self, screen):
        """
        Removes button from screen
        :param screen: Screen
        :return: None
        """
        # TODO

    def is_pressed(self, mouse_click_event):
        """
        Checks if pressed button.
        :param mouse_click_event: Event MOUSEBUTTONDOWN
        :return: True if cursor was above button when clicked, False if not
        """
        # TODO
