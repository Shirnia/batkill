import pygame
from pygame.locals import *
import cevent
import os

backgrounds = os.path.join('static', 'backgrounds')
adventurer = os.path.join('static', 'sprites', 'adventurer', 'adventurer-idle-01.png')

worldx = 928
worldy = 793

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

ani = 4
fps = 40


class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(adventurer).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[(self.frame // ani) + 4]


class App(cevent.CEvent):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.x = 0
        self.y = 50

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((worldx, worldy), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load(os.path.join(backgrounds, 'forest', 'background.png')).convert()
        self.player = Player()
        self.player.rect.x = 0
        self.player.rect.y = 0
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.player)

    def on_loop(self):
        pygame.display.flip()
        pygame.display.update()
        self.player_list.draw(self._display_surf)


    def on_render(self):
        self._display_surf.blit(self._image_surf, (0, 0))
        pygame.display.flip()

    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def on_key_down(self, event):
        self._display_surf.blit(self._display_surf, (self.x, self.y))
        if event.key == pygame.K_a:
            self.x -= 1
        if event.key == pygame.K_d:
            self.x += 1
        self._display_surf.blit(self._display_surf, (self.x, self.y))


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
