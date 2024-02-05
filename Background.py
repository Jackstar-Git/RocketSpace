import pygame

from Constants import DISPLAY, Size


class Background:
    def __init__(self):
        self.image = pygame.image.load("assets/images/backgroundimg.png").convert()
        self.main_background_y = 0
        self.backup_background_y = -Size.Height + 5
        self.image_surface = (pygame.Surface((self.image.get_width(), self.image.get_height()), pygame.SRCALPHA, 16)
                              .convert_alpha())
        self.image_surface.blit(self.image, self.image.get_rect())

    def resize(self):
        self.image_surface = pygame.transform.scale(self.image_surface, (Size.Width, Size.Height+10))

    def adjust_backup_height(self):
        self.backup_background_y = -Size.Height + 5

    def scroll(self):
        self.main_background_y += 0.1
        self.backup_background_y += 0.1
        DISPLAY.blit(self.image_surface, (0, self.main_background_y))
        DISPLAY.blit(self.image_surface, (0, self.backup_background_y))

        if self.main_background_y > Size.Height:
            self.main_background_y = -Size.Height
        if self.backup_background_y > Size.Height:
            self.backup_background_y = -Size.Height
