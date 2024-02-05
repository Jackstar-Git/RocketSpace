import pygame

from Constants import DISPLAY


class Rock:
    def __init__(self, x_pos, y_pos, velocity):
        self.rockSprite = pygame.transform.scale(pygame.image.load("assets/images/rock.png"), (40, 40)).convert_alpha()
        self.hitbox_width = self.rockSprite.get_width() / 2
        self.hitbox_height = self.rockSprite.get_width() / 1.5
        self.position = pygame.Vector2()
        self.position.xy = x_pos, y_pos
        self.velocity = velocity
        self.has_hit = False
        self.was_hit = False
        self.rect = self.rockSprite.get_rect()
        self.image_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA, 16).convert_alpha()
        self.image_surface.blit(self.rockSprite, self.rect)
        self.hitbox = self.rect.inflate(-24, -11)


    def fall(self, frame_delta_time):
        self.position.y += self.velocity*frame_delta_time
        DISPLAY.blit(self.image_surface, self.position)
