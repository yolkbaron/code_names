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
        self.image_button = None

    def create_button(self, x, y, width, height, text, image_button):
        """
        Adds button to given screen.
        :param state: GameState
        :param x: top-left x position of button
        :param y: top-left y position of button
        :param width: Width of button
        :param height: Height of button
        :param text: Text on the button
        :param image_button: Image of button
        :return: Button object
        """
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.image_button = pygame.Rect(self.x, self.y, self.height, self.width)
        text_button = settings.font_text.render(self.text, True, color)
        text_rect = text_button.get_rect()
        text_rect.center = self.rect_image_button.center
        self.image_button.blit(text_button, text_rect)

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

