import time
import pygame
from ..classes import *


class Game:
    def __init__(self, scale, cfg):
        self.screen = None
        self.config = cfg
        self.size = [164, 204]
        self.mode = cfg['default_mode']
        self.field = None
        self.start_time = time.time()
        self.bombs_disp = Display(10, 13)
        self.time_disp = Display(self.size[0] - 39 - 10, 13)
        self.scale = scale
        self.smile = Smile(70, 13)
        self.screen_resize = False
        self.menuButton = MenuButton(0, 0)
        self.timer = True

        # configure presence
        if cfg['presence']:
            self.presence = Presence()
            self.presence_use = self.presence.checkUse()


    def startGame(self):
        self.field = Field(self.mode[0], self.mode[1], self.mode[2], self.scale)
        self.start_time = time.time()
        temp = [self.mode[0] * 16 + 20, self.mode[1] * 16 + 60]
        if self.mode[0] < 7:
            self.bombs_disp.visible = False
            self.time_disp.visible = False
        else:
            self.bombs_disp.visible = True
            self.time_disp.visible = True
        if temp != self.size:
            self.size = temp
            self.smile.rect.x = (self.size[0] - 24) // 2
            self.time_disp.rect.x = self.size[0] - 39 - 10
            self.screen_resize = True

    def update(self, left_click, right_click, screen):
        # presence
        if self.presence_use:
            self.presence_use = self.presence.update(start=int(self.start_time),
                                 state=f'Width: {self.mode[0]} | Height: {self.mode[1]} | Bombs: {self.mode[2]}',
                                 details=f'Bombs left: {self.field.bomb_meter}',
                                 large_image='img')

        # update displays
        if self.timer:
            self.time_disp.setValue(int(time.time() - self.start_time))
        self.time_disp.draw(screen)
        self.bombs_disp.setValue(self.field.bomb_meter)
        self.bombs_disp.draw(screen)

        # smile
        self.smile.setState(self.field.smile_state)
        mouse_pos = pygame.mouse.get_pos()
        if self.smile.rect.colliderect(pygame.Rect(mouse_pos[0] // self.scale, mouse_pos[1] // self.scale, 1, 1)):
            if pygame.mouse.get_pressed(3)[0]:
                self.smile.setState(1)
                self.startGame()
            elif self.smile.state == 1:
                self.smile.setState(0)
        elif self.smile.state == 1:
            self.smile.setState(0)
        self.smile.draw(screen)

        # menu button
        self.menuButton.draw(screen)
        if self.menuButton.rect.colliderect(pygame.Rect(mouse_pos[0] // self.scale, mouse_pos[1] // self.scale, 1, 1)):
            if pygame.mouse.get_pressed(3)[0]:
                menu = Menu(self.config)
                self.mode = menu.mode
                self.startGame()

        # update field
        right_click, self.timer = self.field.update(left_click, right_click, screen)
        return right_click
