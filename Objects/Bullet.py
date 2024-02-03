import pygame
from .Rock import Rock
from .Enemy import Enemy

from Constants import DISPLAY
from utils.functions import collide_circle_rect

class Bullet:
    def __init__(self, x_pos, y_pos, velocity):
        self.bulletSprite = pygame.image.load("assets/images/bullet.png").convert_alpha()
        self.bulletSprite = pygame.transform.scale(self.bulletSprite, (20, 20))
        self.position = pygame.Vector2()
        self.position.xy = x_pos, y_pos
        self.velocity = velocity
        self.has_hit = False
        self.rect = self.bulletSprite.get_rect()
        self.image_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA, 32).convert_alpha()
        self.image_surface.blit(self.bulletSprite, self.rect)

    def fly(self, frame_delta_time):
        self.position.y += self.velocity * (frame_delta_time * (-1))
        DISPLAY.blit(self.image_surface, self.position)

    def rock_hit(self, rock: Rock, Game_rocks: list):
        rock = rock

        rect = self.bulletSprite.get_rect()
        hitbox = rect.inflate(1, 1)
        hitbox.center = (
            (self.position.x + self.bulletSprite.get_width() / 2),
            (self.position.y + self.bulletSprite.get_height() / 2))

        rockRect = rock.rockSprite.get_rect()
        rockHitbox = rockRect.inflate(-4, -4)
        rockHitbox.center = (
            (rock.position.x + rock.hitbox_width), (rock.position.y + rock.hitbox_height))

        collide = hitbox.colliderect(rockHitbox)

        if collide and not self.has_hit:
            self.has_hit = True
            rock.was_hit = True
            for r in Game_rocks:
                if not r.was_hit:
                    r.was_hit = collide_circle_rect((self.position[0], self.position[1]), 800, r.position, r.hitbox.size)

    def enemy_hit(self, enemy: Enemy):
        enemy = enemy

        rect = self.bulletSprite.get_rect()
        hitbox = rect.inflate(1, 1)
        hitbox.center = (
            (self.position.x + self.bulletSprite.get_width() / 2),
            (self.position.y + self.bulletSprite.get_height() / 2))

        enemyRect = enemy.enemySprite.get_rect()
        enemyHitbox = enemyRect.inflate(-4, -4)
        enemyHitbox.center = (
            (enemy.position.x + enemy.enemySprite.get_width() / 2), (enemy.position.y + enemy.enemySprite.get_height() / 2))

        collide = hitbox.colliderect(enemyHitbox)

        if collide and not self.has_hit:
            self.has_hit = True
            enemy.was_hit = True






