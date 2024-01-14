import random
import sys
import threading
import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame.time
from Objects import Coin, Enemy, Rock


from Constants import *
from Game import Game
from Interface import HealthInterface
from utils.functions import *
from utils.tasks import enemy_shoot_cycle


import utils.screens as screens



def play():
    font = pygame.font.SysFont("Arial", 18)
    
    enemy_shoot_thread = threading.Thread(target=enemy_shoot_cycle, daemon=True)
    enemy_shoot_thread.start()
    Game.start_time = time.time()

    while True:
        Game.frame_delta_time = (time.time() - Game.last_td) * 360
        Game.last_td = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                Size.Width = event.w
                Size.Height = event.h
                Game.BG.image = pygame.transform.scale(Game.BG.image, (Size.Width, Size.Height+150))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Game.player.bullets >= 1:
                    Game.friendly_bullets.append(Game.player.shoot())
                if event.key == pygame.K_F3:
                    if Game.debug:
                        Game.debug = False
                    else:
                        Game.debug = True
                if event.key == pygame.K_p:
                    if not Game.paused:
                        Game.paused = True
                    else:
                        Game.paused = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    Game.player.boosted = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a]) and Game.player.check_boarder_collision()[0]:
            Game.player.position.x += -1 * Game.frame_delta_time
        if keys[pygame.K_s] and Game.player.check_boarder_collision()[3]:
            Game.player.position.y += 1 * Game.frame_delta_time
        if keys[pygame.K_d] and Game.player.check_boarder_collision()[1]:
            Game.player.position.x += 1 * Game.frame_delta_time
        if keys[pygame.K_w] and Game.player.check_boarder_collision()[2]:
            Game.player.position.y += -1 * Game.frame_delta_time

        if Game.paused:
            font_face_paused = font.render(f"PAUSED", False, WHITE)
            DISPLAY.blit(font_face_paused, (240, 350))
            pygame.display.update()
            continue

        DISPLAY.fill("red")
        Game.BG.scroll()
        font_face_highscore = font.render(f"Highscore: {Game.highscore}", True, WHITE)
        font_face_score = font.render(f"Score: {Game.points}", True, WHITE)
        font_face_bullets = font.render(f"Bullets: {Game.player.bullets}", True, WHITE)
        font_face_fps = font.render(f"FPS: {round(clock.get_fps())}", True, WHITE)

        Game.player.move()

        # ---------------------- Coins ----------------------
        for index, coin in enumerate(Game.coins):
            if (coin.position.y > Size.Height) or (coin.position.y < 0) or coin.was_collected:
                del Game.coins[index]
            else:
                if Game.player.coin_collide(coin):
                    Game.bullet_counter += 1
                    Game.points += 1

                coin.fall(Game.frame_delta_time)

        if Game.bullet_counter == 5:
            Game.player.bullets += 1
            Game.bullet_counter = 0

        while len(Game.coins) < round(Size.Width / 110):
            x_pos = random.randint(0, Size.Width)
            y_pos = random.randint(0, 100)
            velocity = abs((random.random() + 0.2) / 1.95)
            Game.coins.append(Coin(x_pos, y_pos, velocity))

        # ---------------------- Rocks ----------------------
        for index, rock in enumerate(Game.rocks):
            if rock.position.y > Size.Height or rock.was_hit or rock.has_hit:
                del Game.rocks[index]
            else:
                Game.player.rock_collision(rock)
                rock.fall(Game.frame_delta_time)

        while len(Game.rocks) < round(Size.Width / 37):
            x_pos = random.randint(0, Size.Width)
            y_pos = random.randint(0, 25)
            velocity = abs((random.random() + 0.1) / 2.75)
            Game.rocks.append(Rock(x_pos, y_pos, velocity))

        # -------------------- Enemies and Enemy-Bullets--------------------
        for index, enemy_bullet in enumerate(Game.enemy_bullets):
            if (enemy_bullet.position.y > Size.Height) or enemy_bullet.has_hit:
                del Game.enemy_bullets[index]
            else:
                enemy_bullet.player_hit(Game.player)
                enemy_bullet.fly(Game.frame_delta_time)

        for index, enemy in enumerate(Game.enemies):
            if enemy.position.y > Size.Height or enemy.was_hit or enemy.has_hit:
                del Game.enemies[index]
            else:
                Game.player.enemy_collision(enemy)
                enemy.fly(Game.frame_delta_time)

        while len(Game.enemies) < round(Size.Width / 183):
            x_pos = random.randint(0, Size.Width)
            y_pos = random.randint(0, 25)
            velocity = abs((random.random() + 0.2) / 2.3)
            bullet_velocity = velocity * 1.75
            Game.enemies.append(Enemy(x_pos, y_pos, velocity, bullet_velocity))

        # ----------------- Friendly Bullets -----------------
        for index, friendly_bullet in enumerate(Game.friendly_bullets):
            if (friendly_bullet.position.y < 0) or friendly_bullet.has_hit:
                del Game.friendly_bullets[index]
                break
            else:
                for rock in Game.rocks:
                    friendly_bullet.rock_hit(rock)
                for enemy in Game.enemies:
                    friendly_bullet.enemy_hit(enemy)

                friendly_bullet.fly(Game.frame_delta_time)

        DISPLAY.blit(font_face_highscore, (20, 20))
        DISPLAY.blit(font_face_score, (20, 40))
        DISPLAY.blit(font_face_bullets, (20, 60))
        DISPLAY.blit(font_face_fps, (20, 80))

        HealthInterface.draw()

        if Game.points > Game.highscore:
            Game.highscore = Game.points

        if Game.player.health <= 0:
            new_highscore_end(Game.highscore)
            Game.reset()
            screens.game_over_screen()


        if Game.debug:
            debug_mode(Game.player, Game.rocks, Game.enemies, Game.coins, Game.friendly_bullets, DISPLAY)

        pygame.display.update()

        clock.tick(0)

if __name__ == '__main__':
    pygame.init()
    screens.title_screen()
