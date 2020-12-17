import pygame as pg


class Button(object):
    """
    Class for handling mouse clicking event.
    """

    def __init__(self):
        self.x = None
        self.y = None
        self.height = None
        self.width = None
        self.text = None
        self.pressed = False
        self.button_image = None

    def create_button(self, x, y, width, height, text, button_image, settings, color):
        """
        Adds button to given screen.
        :param x: top-left x position of button
        :param y: top-left y position of button
        :param width: Width of button
        :param height: Height of button
        :param text: Text on the button
        :param button_image: Image of button
        :param settings: Something?
        :param color: Color of button?
        :return: Button object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.button_image = pg.Rect(self.x, self.y, self.width, self.height)
        text_button = settings.font_text.render(self.text, True, color)  # FIXME what is settings?
        text_rect = text_button.get_rect()
        text_rect.center = self.button_image.center  # FIXME no such attribute in class Button!
        self.button_image.blit(text_button, text_rect)  # FIXME

    def remove_button(self, screen):
        """
        Removes button from screen
        :param screen: Screen
        :return: None
        """
        # TODO

    def is_pressed(self, pos):
        """
        Checks if pressed button.
        :param pos
        :return: True if cursor was above button when clicked, False if not
        """
        x, y = pos
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        else:
            return False
