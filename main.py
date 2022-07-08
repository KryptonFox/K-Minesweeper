import pygame
import time
from res.classes import *
from res.classes.Game import Game

# init pygame
pygame.init()
pygame.display.set_icon(pygame.image.load('res/images/icon.png'))

WINDOW_SIZE = (328, 408)
screen = pygame.Surface((164, 204))
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
SCALE = WINDOW_SIZE[1] // 164

left_click = False
right_click = False

game = Game(SCALE)
game.startGame()

run = True

while run:
    screen.fill((174, 174, 174))

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
            elif event.button == 3:
                right_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
            elif event.button == 3:
                right_click = False

    # update
    right_click = game.update(left_click, right_click, screen)
    if game.screen_resize:
        game.screen_resize = False
        WINDOW_SIZE = (game.size[0] * SCALE, game.size[1] * SCALE)
        window = pygame.display.set_mode(WINDOW_SIZE)
        screen = pygame.Surface(game.size)

    # general update
    pygame.display.set_caption(f'K-Minesweeper {clock.get_fps():.1f} FPS')
    clock.tick(30)
    window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
    pygame.display.update()

pygame.quit()
