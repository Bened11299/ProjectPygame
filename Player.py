import pygame
import Colors


class Player:
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score

    def draw_in(self, pygame_window):
        icon_player = pygame.image.load('player.png')
        pygame_window.blit(icon_player, (self.x, self.y))

    def move_in_LEFT(self, pygame_window):
        if self.x <= 0:
            self.x = 0
        else:
            self.x -= 3
        self.draw_in(pygame_window)

    def move_in_RIGTH(self, pygame_window):
        if self.x >= 736:
            self.x = 736
        else:
            self.x += 3
        self.draw_in(pygame_window)

    def ball(self, pygame_window, x, y):
        pos_x = x
        pos_y = y
        pygame.draw.rect(pygame_window, Colors.red, (pos_x + 27, pos_y, 10, 10))
        pos_y -= 10
    def points(self, value):
        self.score += value

    def show_score(self, pygame_window, x, y):
        font = pygame.font.Font('Minecraft.ttf', 32)
        score = font.render("Score: " + str(self.score), True, (255, 255, 255))
        pygame_window.blit(score, (x, y))
