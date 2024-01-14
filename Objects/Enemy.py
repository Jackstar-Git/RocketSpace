import pygame
from .Bullet2 import Bullet2

from Constants import DISPLAY



class Enemy:
    def __init__(self, x_pos, y_pos, velocity, bullet_velocity):
        self.enemySprite = pygame.image.load("assets/images/enemie.png")
        self.enemySprite = pygame.transform.scale(self.enemySprite, (67, 67))
        self.position = pygame.Vector2()
        self.position.xy = x_pos, y_pos
        self.velocity = velocity
        self.bullet_velocity = bullet_velocity
        self.was_hit = False
        self.has_hit = False

        self.rect = self.enemySprite.get_rect()
        self.image_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA, 32).convert_alpha()
        self.image_surface.blit(self.enemySprite, self.rect)


    def fly(self, frame_delta_time):
        self.position.y += self.velocity * frame_delta_time
        DISPLAY.blit(self.image_surface, self.position)

    def shoot(self):
        return Bullet2(self.position.x + self.enemySprite.get_width() / 3, self.position.y + 20, self.bullet_velocity)



    

