import math

import pygame


class Bullet:
    def __init__(self, x_move, y_move, xpos, ypos):
        self.x_move = x_move
        self.y_move = y_move
        self.x = xpos
        self.y = ypos
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.rotate(
                self.image,
                math.degrees(math.atan2(-self.y_move, self.x_move)))
