import pygame

from playStatusConfig import *
from settings import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down'
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                           'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
                           'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}

        for animation in self.animations.keys():
            full_path = images_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = Status.up
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = Status.down
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = Status.right
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = Status.left
        else:
            self.direction.x = 0
        pygame.event.pump()

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.statusToIdle()

    def statusToIdle(self):
        self.status = self.status.split('_')[0] +  Status.idle

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
        print(self.direction)

    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)