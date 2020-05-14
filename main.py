import pygame
import Colors
from Invader import Invader
from Player import Player
from Ball import Ball

# Inicializamos el pygame
pygame.init()

# Creamos la pantalla
window_width = 800
window_height = 600
window_size = (window_width, window_height)
main_window = pygame.display.set_mode(window_size)

# Asignamos un titulo/nombre
pygame.display.set_caption("Space Invader")

# Tambien podemos asignar un icono, que si bien no es imprescindible
# Los detalles hacen la diferencia ;)
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# movimiento en x, del invader
inv_rigth = 1
inv_left = -1
# Player
player = Player(368, 500, 0)
# Fondo del juego
background = pygame.image.load('fondo.jpg')
# Invaders
inv_1 = [Invader(153, 0), Invader(237, 0), Invader(321, 0), Invader(405, 0),
         Invader(489, 0), Invader(573, 0), Invader(657, 0)]
inv_2 = [Invader(153, 84), Invader(237, 84), Invader(321, 84), Invader(405, 84),
         Invader(489, 84), Invader(573, 84), Invader(657, 84)]
inv_3 = [Invader(153, 163), Invader(237, 163), Invader(321, 163), Invader(405, 163),
         Invader(489, 163), Invader(573, 163), Invader(657, 163)]
inv_x = 0
inv_y = 0
inv = Invader(inv_x, inv_y)
sw_vel_inv = True
sww_vel_inv = True
# Score
value = 5
num_invader_dead = 0
# bala
new_ball = Ball(600, 800, False)
# Game
running_game = True
while running_game:

    pygame.time.delay(1)
    # Fondo del juego
    main_window.fill(Colors.black)
    main_window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            break
    player.draw_in(main_window)
    for k in range(0, 7, 1):
        inv_1[k].draw_in(main_window)
        inv_2[k].draw_in(main_window)
        inv_3[k].draw_in(main_window)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_in_LEFT(main_window)

    if keys[pygame.K_RIGHT]:
        player.move_in_RIGTH(main_window)

    if keys[pygame.K_SPACE]:
        if not new_ball.state:
            bullet = Ball(player.x, player.y, True)
            new_ball = bullet
            new_ball.ball(main_window)
    # Invader
    for k in range(0, 7, 1):
        inv_1[k].move_invader_x(main_window, inv_rigth)
        inv_2[k].move_invader_x(main_window, inv_left)
        inv_3[k].move_invader_x(main_window, inv_rigth)

    if inv_1[6].board() or inv_1[0].board():
        if inv_1[6].x >= 736:
            aux = inv_rigth
            inv_rigth = inv_left
            inv_left = aux
            for l in range(0, 7, 1):
                inv_1[l].move_in_down(main_window)
                inv_2[l].move_in_down(main_window)
                inv_3[l].move_in_down(main_window)
            inv_y += 35
            inv = Invader(0, inv_y)
        elif inv_1[0].x <= 0:
            aux = inv_rigth
            inv_rigth = inv_left
            inv_left = aux
            for l in range(0, 7, 1):
                inv_1[l].move_in_down(main_window)
                inv_2[l].move_in_down(main_window)
                inv_3[l].move_in_down(main_window)
            inv_y += 35
            inv = Invader(0, inv_y)

    # Bullet
    if new_ball.y <= 0:
        new_ball.ball_dead()
    if new_ball.state:
        new_ball.move_in_up(main_window)

    # Collision
    if new_ball.state:
        for l in range(0, 7, 1):
            if inv_1[l].collision(new_ball.x, new_ball.y):
                new_ball.ball_dead()
                inv_1[l].dead_invader()
                player.points(value)
                num_invader_dead += 1
            if inv_2[l].collision(new_ball.x, new_ball.y):
                new_ball.ball_dead()
                inv_2[l].dead_invader()
                player.points(value)
                num_invader_dead += 1
            if inv_3[l].collision(new_ball.x, new_ball.y):
                new_ball.ball_dead()
                inv_3[l].dead_invader()
                player.points(value)
                num_invader_dead += 1
    if player.score > 120 and sw_vel_inv:
        inv_rigth *= 2
        inv_left *= 2
        sw_vel_inv = False
        value = 20
    elif player.score > 45 and sww_vel_inv:
        sww_vel_inv = False
        inv_rigth *= 3
        inv_left *= 3
        value = 10

    player.show_score(main_window,10, 10)
    if num_invader_dead == 21:
        inv.game_over(main_window)
        running_game = False
    elif inv.y >= 500:
        inv.game_over(main_window)
        running_game = False

    pygame.display.update()

pygame.quit()
