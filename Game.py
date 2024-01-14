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
    start_time = 0





















    #@classmethod
    #def save(cls):
    #    with open("save.txt", "w") as file:
    #        data = {
    #            "BG": cls.BG,
    #            "player": cls.player,
    #            "rocks": cls.rocks,
    #            "enemies": cls.enemies,
    #            "coins": cls.coins,
    #            "friendly_bullets": cls.friendly_bullets,
    #            "enemy_bullets": cls.enemy_bullets,
    #            "points": cls.points,
    #            "highscore": cls.highscore,
    #            "debug": cls.debug,
    #            "enemy_shoot": cls.enemy_shoot,
    #            "bullet_counter": cls.bullet_counter,
    #            "paused": cls.paused,
    #            "last_td": cls.last_td,
    #            "frame_delta_time": cls.frame_delta_time}
#
    #        json.dump(data, file, indent=4)
#