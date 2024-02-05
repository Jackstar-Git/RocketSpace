import pygame

from Constants import DISPLAY

class Coin:
    def __init__(self, x_pos, y_pos, velocity):
        self.coinSprite = pygame.transform.scale(pygame.image.load("assets/images/coin.png"), (40, 40)).convert_alpha()
        self.position = pygame.Vector2()
        self.position.xy = x_pos, y_pos
        self.velocity = velocity
        self.was_collected = False



    def fall(self,frame_delta_time):
        self.position.y += self.velocity*frame_delta_time

        DISPLAY.blit(self.coinSprite, self.position)



