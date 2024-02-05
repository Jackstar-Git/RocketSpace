from Background import Background
from Objects.Bullet import Bullet
from Objects.Bullet2 import Bullet2
from Objects.Player import Player
from Objects.Coin import Coin
from Objects.Enemy import Enemy

from Objects.Rock import Rock
from utils.functions import *
import time


class Game:
    BG = Background()
    player = Player()
    rocks: [Rock] = []
    enemies: [Enemy] = []
    coins: [Coin] = []
    friendly_bullets: [Bullet] = []
    enemy_bullets: [Bullet2] = []
    points: int = 0
    highscore = read_highscore()
    debug = False
    enemy_shoot = True
    bullet_counter = 0
    paused = False
    last_td = time.time()
    frame_delta_time = 0
    start_time = time.time()
    speed_factor = 0
    state = 1

    @classmethod
    def reset(cls):
        cls.BG = Background()
        cls.BG.resize()
        cls.player = Player()
        cls.rocks: [Rock] = []
        cls.enemies: [Enemy] = []
        cls.coins: [Coin] = []
        cls.friendly_bullets: [Bullet] = []
        cls.enemy_bullets: [Bullet2] = []
        cls.points: int = 0
        cls.highscore = read_highscore()
        cls.debug = False
        cls.enemy_shoot = True
        cls.bullet_counter = 0
        cls.paused = False
        cls.last_td = time.time()
        cls.frame_delta_time = 0
        cls.start_time = time.time()



















