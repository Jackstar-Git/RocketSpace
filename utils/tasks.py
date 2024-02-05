import pygame
import threading
import time

from Game import Game


def enemy_shoot_cycle():
    while True:
        time.sleep(2)
        for enemy in Game.enemies:
            Game.enemy_bullets.append(enemy.shoot())



