import pygame
import threading
import time
import random

from Game import Game
from Objects import Coin, Enemy, Rock
from Constants import Size

def enemy_shoot_cycle():
    while True:
        time.sleep(2)
        for enemy in Game.enemies:
            Game.enemy_bullets.append(enemy.shoot())

def initial_load():
    Game.BG.scroll()
    Game.player.move()

    while len(Game.coins) < round(Size.Width / 150):
        x_pos = random.randint(0, Size.Width)
        y_pos = random.randint(0, 100)
        velocity = abs((random.random() + 0.2) / 1.95)
        Game.coins.append(Coin(x_pos, y_pos, velocity))

    while len(Game.rocks) < round((Size.Width / 30) * 1):
        x_pos = random.randint(0, Size.Width)
        y_pos = random.randint(0, 25)
        velocity = abs((random.random() + 0.1) / 2.75)
        Game.rocks.append(Rock(x_pos, y_pos, velocity))

    while len(Game.enemies) < round((Size.Width / 150) * 1):
        x_pos = random.randint(0, Size.Width)
        y_pos = random.randint(0, 25)
        velocity = abs((random.random() + 0.2) / 2.3)
        bullet_velocity = velocity * 1.75
        Game.enemies.append(Enemy(x_pos, y_pos, velocity, bullet_velocity))

