"""
player.py
"""

import math

import pygame


class Player:
    def __init__(self, x, y, w, h):
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.active = True

        pygame.draw.circle(self.image,
                (255,255,255),
                (self.w // 2, self.h // 2), ((self.w // 2) - 15 ))

        self.image.fill((180, 255, 100))
        self.image.set_colorkey((0,0,0))

        self.position = pygame.math.Vector2(self.x, self.y)
        self.dir = pygame.math.Vector2()
        self.acc = pygame.math.Vector2()
        self.vel = pygame.math.Vector2()

        self.size = (self.w, self.h)

        self.rect: pygame.rect.Rect = pygame.Rect(
                self.x,
                self.y,
                self.w,
                self.h)

    def draw(self, surface, mx, my):
        self.dir = (mx - self.x, my - self.y)
        length = math.hypot(self.dir[0], self.dir[1])
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        pygame.transform.rotate(self.image, angle)
        self.update() # reset box before bliting to display
        surface.blit(self.image, self.rect)
        

    def update(self):
        """ Reattatch collision box """
        self.rect.x = self.x
        self.rect.y = self.y
