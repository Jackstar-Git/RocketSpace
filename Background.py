import pygame

from Constants import DISPLAY, Size


class Background:
    def __init__(self):
        self.image = pygame.image.load("assets/images/backgroundimg.png")
        self.main_background_y = 0
        self.backup_background_y = -(Size.Height)

    def scroll(self):
        self.main_background_y += 0.1
        self.backup_background_y += 0.1
        DISPLAY.blit(self.image, (0, self.main_background_y))
        DISPLAY.blit(self.image, (0, self.backup_background_y))

        if self.main_background_y > (Size.Height):
            self.main_background_y = -(Size.Height)
        if self.backup_background_y > (Size.Height):
            self.backup_background_y = -(Size.Height)

