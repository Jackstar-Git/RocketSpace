import pygame

from Constants import DISPLAY

class Bullet2:
    def __init__(self, x_pos, y_pos, velocity):
        self.bulletSprite = pygame.image.load("assets/images/bullet.png").convert_alpha()
        self.bulletSprite = pygame.transform.flip(self.bulletSprite, 0 ,1)
        self.bulletSprite = pygame.transform.scale(self.bulletSprite, (20, 20))
        self.position = pygame.Vector2()
        self.position.xy = x_pos, y_pos
        self.velocity = velocity
        self.has_hit = False

    def fly(self, frame_delta_time):
        self.position.y += self.velocity*frame_delta_time
        DISPLAY.blit(self.bulletSprite, self.position)


    def player_hit(self, player):
        player = player

        rect = self.bulletSprite.get_rect()
        hitbox = rect.inflate(1, 1)
        hitbox.center = (
            (self.position.x + self.bulletSprite.get_width() / 2),
            (self.position.y + self.bulletSprite.get_height() / 2))

        playerHitbox = player.hitbox
        playerHitbox.center = (
            (player.position.x + player.hitbox_width), (player.position.y + player.hitbox_height))

        collide = hitbox.colliderect(playerHitbox)

        if collide and not self.has_hit:
            self.has_hit = True
            print("Hit a player")
            player.health -= 1
