import pygame
from Constants import DISPLAY, Size
from Game import Game

class HealthInterface:
    healthSprite = pygame.image.load("assets/images/heart.png").convert_alpha()
    healthSprite = pygame.transform.scale(healthSprite, (35, 35))
    rect = healthSprite.get_rect()
    image_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA, 32).convert_alpha()
    image_surface.blit(healthSprite, rect)

    @classmethod
    def draw(cls):
        for index in range(Game.player.health):
            DISPLAY.blit(cls.image_surface, ((Size.Width - 50) - 37 * index, 20))


class Button:
    def __init__(self, screen, pos: tuple, text, size: tuple[int, int], color= (0,0,0), font_color= (255, 255, 255), hover_color= (255, 255, 255), enabled= True):
        self.font_color = font_color
        self.color = color
        self.hover_color = hover_color
        self.size = size
        self.text = text
        self.x = pos[0]
        self.y = pos[1]
        self.enabled = enabled
        self.button_rect = pygame.Rect((self.x, self.y), self.size)
        self.button_rect.center = (self.x, self.y)

        self.draw(screen=screen)

    def draw(self, screen):
        font = pygame.font.SysFont("Calibri", 20)
        button_text = font.render(self.text, True, self.font_color)


        text_size = font.size(self.text)

        mousePos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mousePos):
            self.color = self.hover_color

        pygame.draw.rect(screen, self.color, self.button_rect, 0)
        screen.blit(button_text, (self.x - text_size[0]/2, self.y - text_size[1]/2))

    def get_click(self):
        mousePos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mousePos):
            self.color = "black"
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                return True


class InputBox:
    def __init__(self, screen, pos: tuple, size: tuple[int, int], color=(0, 0, 0), font_color=(255, 255, 255),
                 color_active=(255, 255, 255)):
        self.font = pygame.font.SysFont("Calibri", 20)
        self.font_color = font_color
        self.color = color
        self.color_active = color_active
        self.size = size
        self.x = pos[0]
        self.y = pos[1]
        self.field_rect = pygame.Rect((self.x, self.y), self.size)
        self.field_rect.center = (self.x, self.y)
        print(self.field_rect.center)
        self.active = False
        self.text = ""
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.screen = screen

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                if self.field_rect.collidepoint(event.pos):
                    print("OK")
                    self.active = True
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color
            if event.type == pygame.KEYDOWN:
                print("YEAH")
                self.update()
                print(self.active)
                if self.active:
                    print("HOOOOO")
                    if event.key == pygame.K_RETURN:
                        text = self.text
                        self.text = ""
                        print(text)
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        #self.text = self.text[:self.cursor_position] + self.text[self.cursor_position+1:]
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                        print(self.text)
                    self.txt_surface = self.font.render(self.text, True, self.font_color)

    def update(self):
        width = max(self.size[0], self.txt_surface.get_width() + 10)
        self.field_rect.w = width

    def draw(self, screen):#
        pygame.draw.rect(screen, self.color, self.field_rect)
        screen.blit(self.txt_surface, self.field_rect.center)
