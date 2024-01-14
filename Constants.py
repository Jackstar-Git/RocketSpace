import pygame


class Size:
    Width = 550
    Height = 780


DISPLAY = pygame.display.set_mode((Size.Width, Size.Height), pygame.RESIZABLE)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

