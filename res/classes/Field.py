import pygame
import random
from ..classes import *
from ..Scripts.getnearest import getNearest


class Field:
    def __init__(self, width, height, bombs, scale):
        # load images
        tile_tileset = pygame.image.load('res/images/tiles.png')
        self.tile_images = Cutter().load(tile_tileset)

        # variables
        self.left_clicked = False
        self.buttons = []
        self.scale = scale
        self.width = width
        self.height = height
        self.left_clicked_timer = 0
        self.bomb_meter = bombs
        self.bomb_count = bombs
        self.closed = width * height
        self.smile_state = 0
        self.timer = True
        self.bombed = False
        self.bombs = bombs
        self.stopped = False

        # create field
        for row in range(height):
            temp = []
            for tile in range(width):
                s = Tile(self.tile_images, tile * 16 + 10, row * 16 + 50, [row, tile])
                temp.append(s)
            self.buttons.append(temp)

    def bombGenerator(self, exclude):
        # create bombs
        temp = []
        bomb_list = []
        temp += exclude

        for i in range(self.bombs):
            bomb = random.choice(random.choice(self.buttons)).index
            while bomb in temp:
                bomb = random.choice(random.choice(self.buttons)).index

            temp.append(bomb)
            bomb_list.append(bomb)

        for bomb in bomb_list:
            self.buttons[bomb[0]][bomb[1]].bomb = True
            nearest = getNearest(bomb)
            for nearRow in nearest:
                for nearTile in nearRow:
                    if -1 in nearTile or self.width == nearTile[1] or self.height == nearTile[0] or self.buttons[nearTile[0]][nearTile[1]].index == bomb:
                        continue
                    self.buttons[nearTile[0]][nearTile[1]].count += 1

    def update(self, left_click, right_click, screen):
        # check for win
        win = False
        if self.closed <= self.bomb_count and not self.stopped:
            win = True
            for row in self.buttons:
                for button in row:
                    if button.destroyed and button.bomb:
                        win = False
                        break
        if win:
            self.stopped = True
            self.winGame()

        # update buttons
        if self.left_clicked:
            self.left_clicked_timer += 1
        for row in self.buttons:
            for button in row:
                button.draw(screen)
                if button.preclicked and not button.opened:
                    button.preclicked = False
                    button.image = button.images[0]
                if left_click or right_click or self.left_clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    if button.rect.colliderect(pygame.Rect(mouse_pos[0] // self.scale, mouse_pos[1] // self.scale, 1, 1)):
                        if right_click:
                            button.click_right(self)
                            right_click = False
                        elif left_click:
                            self.left_clicked = True
                            button.preclick(self)
                        elif not left_click:
                            if self.left_clicked:
                                self.left_clicked = False
                                if button.opened and self.left_clicked_timer > 5:
                                    pass
                                else:
                                    button.click_left(self)
                                self.left_clicked_timer = 0
        return right_click, self.timer

    def endGame(self):
        self.stopped = True
        self.timer = False
        self.smile_state = 4
        for row in self.buttons:
            for tile in row:
                tile.open()

    def winGame(self):
        self.timer = False
        self.smile_state = 3
        for row in self.buttons:
            for tile in row:
                tile.open(True, self)
