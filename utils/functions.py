import pygame
import math


def collide_circles(point1: tuple[float, float], point2: tuple[float, float], radius1: float, radius2: float):
    distance = math.sqrt(abs(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2)))

    return distance < radius1+radius2


def collide_circle_rect(circle: tuple[float, float], circle_radius: float, rect_pos: tuple[float, float], rect_size: tuple[float, float]):
    circleDistance_x = abs(circle[0] - rect_pos[0])
    circleDistance_y = abs(circle[1] - rect_pos[1])


    if circleDistance_x > (rect_size[0]/2 + circle_radius):
        return False
    if circleDistance_y > (rect_size[1]/2 + circle_radius):
        return False

    if circleDistance_x <= rect_size[0]/2:
        return True

    if circleDistance_y <= (rect_size[1]/2):
        return True

    cornerDistance_sq = (circleDistance_x - rect_size[0]/2)**2 + (circleDistance_y - rect_size[1]/2)**2
    return (cornerDistance_sq <= (circle_radius**2))



def read_highscore():
    with open("highscore.txt", "r") as file:
        return int(file.read())

def new_highscore_end(highscore):
    with open("highscore.txt", "w") as file:
        file.write(str(highscore))



def debug_mode(player, rocks, enemies, coins, friendly_bullets, display: pygame.display):
    rect = player.playerSprite.get_rect()
    hitbox = rect.inflate(-35, -25)
    hitbox.center = (
        (player.position.x + player.playerSprite.get_width() / 2.1),
        (player.position.y + player.playerSprite.get_height() / 3))
    pygame.draw.rect(display, (0, 255, 0), hitbox)

    for enemy in enemies:
        enemyRect = enemy.enemySprite.get_rect()
        enemyHitbox = enemyRect.inflate(-29, -19)
        enemyHitbox.center = (
            (enemy.position.x + enemy.enemySprite.get_width() / 2),
            (enemy.position.y + enemy.enemySprite.get_height() / 2))
        pygame.draw.rect(display, (120, 120, 120), enemyHitbox)

    for rock in rocks:
        rockRect = rock.rockSprite.get_rect()
        rockHitbox = rockRect.inflate(-24, -11)
        rockHitbox.center = (
            (rock.position.x + rock.rockSprite.get_width() / 2), (rock.position.y + rock.rockSprite.get_height() / 2))
        pygame.draw.rect(display, (255, 0, 0), rockHitbox)

    for coin in coins:
        coinRect = coin.coinSprite.get_rect()
        coinHitbox = coinRect.inflate(-8, -8)
        coinHitbox.center = (
            (coin.position.x + coin.coinSprite.get_width() / 2),
            (coin.position.y + coin.coinSprite.get_height() / 2))

        pygame.draw.rect(display, (255, 255, 0), coinHitbox)

    for friendly_bullet in friendly_bullets:
        bulletRect = friendly_bullet.bulletSprite.get_rect()
        bulletHitbox = bulletRect.inflate(1, 1)
        bulletHitbox.center = (
            (friendly_bullet.position.x + friendly_bullet.bulletSprite.get_width() / 2),
            (friendly_bullet.position.y + friendly_bullet.bulletSprite.get_height() / 2))

        pygame.draw.rect(display, (220, 15, 255), bulletHitbox)

