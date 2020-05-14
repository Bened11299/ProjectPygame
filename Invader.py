import pygame


class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_in(self, pygame_window):
        icon_invader = pygame.image.load('invaderP.png')
        pygame_window.blit(icon_invader, (self.x, self.y))

    def board(self):
        val = 1
        if self.x >= 736:
            self.x = 736
            return True
        elif self.x <= 0:
            self.x = 0
            return True
        return False

    def move_invader_x(self, pygame_window, val):
        self.x += val
        self.draw_in(pygame_window)

    def move_in_down(self, pygame_window):
        self.y += 35
        self.draw_in(pygame_window)

    def dead_invader(self):
        self.y = 802

    def collision(self, inv_x, inv_y):
        if self.x - 8 <= inv_x + 16 <= self.x + 55 and self.y <= inv_y <= self.y + 64:
            return True
        else:
            return False

    def game_over(self, pygame_window):
        pygame_window.fill((0, 0, 0))
        font = pygame.font.Font('Minecraft.ttf', 64)
        game = font.render("GAME OVER", True, (255, 255, 255))
        pygame_window.blit(game, (300, 280))
