import pygame as pg
pg.font.init()


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

    font_name = pg.font.match_font('arial')

    def create_button(self, x, y, width, height, text, button_image, size, color):
        """
        Adds button to given screen.
        :param x: top-left x position of button
        :param y: top-left y position of button
        :param width: Width of button
        :param height: Height of button
        :param text: Text on the button
        :param button_image: Image of button
        :param color: Color of text
        :return: Button object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.button_image = pg.Surface((self.width, self.height))
        font = pg.font.Font(Button.font_name, size)
        text_button = font.render(self.text, True, color)
        text_rect = text_button.get_rect()
        text_rect.center = self.button_image.center
        self.button_image.blit(text_button, text_rect)

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
