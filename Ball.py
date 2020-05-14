import pygame


class Ball:
    def __init__(self, x, y, sw):
        self.x = x
        self.y = y
        self.state = sw

    def draw_in(self, pygame_window):
        icon_player = pygame.image.load('ball16.png')
        pygame_window.blit(icon_player, (self.x + 20, self.y - 16))

    def ball(self, pygame_window):
        if self.state:
            self.draw_in(pygame_window)

    def move_in_up(self, pygame_window):
        self.y -= 10
        self.draw_in(pygame_window)

    def ball_dead(self):
        self.state = False
