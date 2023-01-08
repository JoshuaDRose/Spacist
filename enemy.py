"""
enemy.py
"""

import math
import random

import utils
from consts import *

import pygame


class Enemy:
    def __init__(self, x, y, w, h, colorkey=(0, 0, 0)):
        self.x = x
        self.y = y
        self.w = h
        self.h = h
        self.colorkey = colorkey

        self.rect: pygame.rect.Rect = pygame.Rect(x, y, w, h)
        self.rect.center = (x + (w // 2), y + (h // 2))

        self.image: pygame.surface.Surface = pygame.Surface((w, h), pygame.SRCALPHA)
        self.image.set_colorkey((self.colorkey))

        self.dir = pygame.math.Vector2()
        self.acc = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.size = (w, h)

        self.vel = random.randint(2, 4)
        self.color = utils.generate_color()

        self.active = True

    def draw(self, surface) -> None:
        pygame.draw.circle(
                self.image,
                self.color,
                (self.w//2, self.h//2),
                 self.w//2)
        surface.blit(self.image, self.rect)

    def update(self, target: pygame.rect.Rect):
        dx = target.centerx - self.rect.x
        dy = target.centery - self.rect.y
        dist = math.sqrt(dx * dx + dy * dy)
        if dist > 0:
            self.rect.x += self.vel * dx / dist # pyright: ignore
            self.rect.y += self.vel * dy / dist # pyright: ignore
            if pygame.Rect.colliderect(self.rect, target): # pyright: ignore
                self.active = False
        else:
            self.active = False
