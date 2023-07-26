import random
import pygame
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
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}

        for animation in self.animations.keys():
            full_path = images_path + animation
            self.animations[animation] = import_folder(full_path)
    def input(self):
        keys = pygame.key.get_pressed()
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.image.fill((red, green, blue))
        if keys[pygame.K_UP]:
            self.direction.y = -1
            print('up')
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            print('down')
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            print('right')
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            print('left')
        else:
            self.direction.x = 0
        pygame.event.pump()

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
        print(self.direction)
    def update(self, dt):
        self.input()
        self.move(dt)
