import pygame as pg

pg.font.init()


class Button(object):
    """
    Class for handling mouse clicking event.
    """
    font_name = pg.font.match_font('arial')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = None
        self.pressed = False
        self.button_image = None

    def set_button(self, text, text_size, text_color, button_color=None):
        """
        Adds button to given screen.
        :param button_color: color of button background
        :param text_size: Size of font
        :param text: Text on the button
        :param text_color: Color of text
        :return: Button object
        """
        self.text = text
        self.button_image = pg.Surface((self.width, self.height), flags=pg.SRCALPHA)
        if button_color:
            self.button_image.fill(button_color)
        font = pg.font.Font(Button.font_name, text_size)
        text_button = font.render(self.text, True, text_color)
        text_rect = text_button.get_rect()
        text_rect.center = self.button_image.get_rect().center
        self.button_image.blit(text_button, text_rect)

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

    def draw(self, surface):
        surface.blit(self.button_image, (self.x, self.y))
