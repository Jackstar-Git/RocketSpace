import pygame
import time
import sys

from Constants import Size, WHITE, DISPLAY, clock
from Game import Game
from Interface import Button


def game_over_screen():
    font = pygame.font.SysFont("Arial", 21)
    font2 = pygame.font.SysFont("Arial", 28)

    time_spent = time.time() - Game.start_time
    fade = pygame.Surface((Size.Width, Size.Height))
    fade.set_alpha(200)
    fade.fill((0, 0, 0))
    DISPLAY.blit(fade, (0, 0))
    pygame.display.update()

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

        font_face_game_over = font2.render(f"Game Over", True, WHITE)
        font_face_game_over_rect = font_face_game_over.get_rect(midtop=(Size.Width / 2, 100))

        font_face_highscore = font.render(f"Highscore: {Game.highscore}", False, WHITE)
        font_face_highscore_rect = font_face_highscore.get_rect(midtop=(Size.Width / 2, 130))

        font_face_score = font.render(f"Score: {Game.points}", False, WHITE)
        font_face_score_rect = font_face_score.get_rect(midtop=(Size.Width / 2, 150))

        font_face_time_spent = font.render(f"Seconds Played: {round(time_spent)}", False, WHITE)
        font_face_time_spent_rect = font_face_time_spent.get_rect(midtop=(Size.Width / 2, 170))

        DISPLAY.blit(font_face_game_over, font_face_game_over_rect)
        DISPLAY.blit(font_face_highscore, font_face_highscore_rect)
        DISPLAY.blit(font_face_score, font_face_score_rect)
        DISPLAY.blit(font_face_time_spent, font_face_time_spent_rect)

        play_again_button = Button(DISPLAY, (Size.Width / 2, 350), "Play Again", (350, 50), (82, 77, 77), "white",
                                   (36, 35, 35))
        back_to_title_screen = Button(DISPLAY, (Size.Width / 2, 420), "Back to title screen", (350, 50), (82, 77, 77),
                                      "white", (36, 35, 35))
        quit_button = Button(DISPLAY, (Size.Width / 2, 490), "Quit", (350, 50), (82, 77, 77), "white", (36, 35, 35))

        if play_again_button.get_click():
            Game.reset()
            break
        if back_to_title_screen.get_click():
            title_screen()
        if quit_button.get_click():
            pygame.quit()
            sys.exit()

        pygame.display.update()

        clock.tick(60)


def title_screen():
    pygame.display.set_caption("RocketSpace")

    font2 = pygame.font.SysFont("Comic Sans MS", 25)
    DISPLAY.fill("black")

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
                Game.BG.resize()
                Game.BG.adjust_backup_height()

        font_face_title = font2.render(f"RocketSpace", False, WHITE)
        font_face_title_rect = font_face_title.get_rect(midtop=(Size.Width / 2, 50))
        DISPLAY.blit(font_face_title, font_face_title_rect)

        play_button = Button(DISPLAY, (Size.Width / 2, 350), "Play", (350, 50), (82, 77, 77), "white", (36, 35, 35))
        options_button = Button(DISPLAY, (Size.Width / 2, 420), "Options", (350, 50), (82, 77, 77), "white",
                                (36, 35, 35))
        quit_button = Button(DISPLAY, (Size.Width / 2, 490), "Quit", (350, 50), (82, 77, 77), "white", (36, 35, 35))

        if play_button.get_click():
            break
        if options_button.get_click():
            options_screen()
        if quit_button.get_click():
            pygame.quit()
            sys.exit()

        pygame.display.update()

        clock.tick(60)


def options_screen():
    pygame.display.update()
    font2 = pygame.font.SysFont("Comic Sans MS", 35)

    while True:
        DISPLAY.fill("black")
        Game.frame_delta_time = (time.time() - Game.last_td)
        Game.last_td = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                Size.Width = event.w
                Size.Height = event.h

        font_face_title = font2.render(f"Options", False, WHITE)
        font_face_title_rect = font_face_title.get_rect(midtop=(Size.Width / 2, 50))

        DISPLAY.blit(font_face_title, font_face_title_rect)
        back_button = Button(DISPLAY, (Size.Width / 2, Size.Height - 100), "Back", (350, 50), (82, 77, 77), "white", (36, 35, 35))

        if back_button.get_click():
            title_screen()
        pygame.display.update()

        clock.tick(60)
