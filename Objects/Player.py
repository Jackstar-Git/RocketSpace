import pygame
from .Rock import Rock
from .Coin import Coin
from .Bullet import Bullet
from .Enemy import Enemy

from Constants import DISPLAY, Size


class Player:
    def __init__(self):
        self.boosted = False
        self.playerSprite = pygame.image.load("assets/images/rocket.png").convert_alpha()
        self.playerSprite = pygame.transform.scale(self.playerSprite, (67, 67))
        self.position = pygame.Vector2()
        self.position.xy = 200 - round(self.playerSprite.get_width() / 2), 650 - round(self.playerSprite.get_height() / 2)
        self.health = 10
        self.bullets = 10

        self.rect = self.playerSprite.get_rect()
        self.hitbox = self.rect.inflate(-35, -25)
        self.hitbox.center = (
            (self.position.x + self.playerSprite.get_width() / 2.1),
            (self.position.y + self.playerSprite.get_height() / 3))

    def move(self):
        if self.position.x > Size.Width:
            self.position.x = Size.Width-self.hitbox.size[0]*1.5

        self.hitbox.center = (self.position.x + self.playerSprite.get_width() / 2.1), (
                    self.position.y + self.playerSprite.get_height() / 3)

        DISPLAY.blit(self.playerSprite, self.position)

    def change_skin(self):
        if self.boosted:
            self.playerSprite = pygame.image.load("../assets/images/rocket_boost.png")
        else:
            self.playerSprite = pygame.image.load("../assets/images/rocket.png")

        self.playerSprite = pygame.transform.scale(self.playerSprite, (67, 67))

    def shoot(self):
        self.bullets -= 1
        return Bullet(self.position.x + self.playerSprite.get_width() / 3, self.position.y, 1)

    def check_boarder_collision(self):
        width, height = self.hitbox.size

        blocked = [True, True, True, True]

        if (self.hitbox.center[0] - width/2) <= 0:
            blocked[0] = False
        if (self.hitbox.center[0] + width/2) >= Size.Width:
            blocked[1] = False
        if (self.hitbox.center[1] - height/2) <= 0:
            blocked[2] = False
        if (self.hitbox.center[1] + height/2) >= Size.Height:
            blocked[3] = False

        return blocked

    def rock_collision(self, rock: Rock):
        rock = rock

        rockRect = rock.rockSprite.get_rect()
        rockHitbox = rockRect.inflate(-24, -11)
        rockHitbox.center = (
            (rock.position.x + rock.rockSprite.get_width() / 2), (rock.position.y + rock.rockSprite.get_height() / 1.5))

        collide = self.hitbox.colliderect(rockHitbox)

        if collide and not rock.has_hit:
            rock.has_hit = True
            self.health -= 1

    def coin_collide(self, coin: Coin):
        coin = coin

        coinRect = coin.coinSprite.get_rect()
        coinHitbox = coinRect.inflate(-8, -8)
        coinHitbox.center = (
            (coin.position.x + coin.coinSprite.get_width() / 2), (coin.position.y + coin.coinSprite.get_height() / 2))

        collide = self.hitbox.colliderect(coinHitbox)

        if collide and not coin.was_collected:
            coin.was_collected = True

            return True

    def enemy_collision(self, enemy: Enemy):
        enemy = enemy

        enemyRect = enemy.enemySprite.get_rect()
        enemyHitbox = enemyRect.inflate(-33, -22)
        enemyHitbox.center = (
            (enemy.position.x + enemy.enemySprite.get_width() / 2),
            (enemy.position.y + enemy.enemySprite.get_height() / 2))

        collide = self.hitbox.colliderect(enemyHitbox)

        if collide and not enemy.has_hit:
            enemy.has_hit = True
            self.health -= 1
