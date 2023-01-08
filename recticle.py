"""
recticle.py
"""
import pygame

class Recticle:
    def __init__(self, x, y, w, h):

        self.x: int = x
        self.y: int = y
        self.w: int = w
        self.h: int = h

        self.image = pygame.Surface((100, 100),pygame.SRCALPHA)
        self.image.set_colorkey((0,0,0))

        self.shoot_alpha = 255
        self.shoot_size = self.w // 2
        self.normal_size = self.w // 6

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        pygame.draw.circle(
                self.image,
                (60, 60, 60),
                (self.normal_size, self.normal_size),
                self.normal_size,
                2)

        # Default shooting parameters
        self.do_shoot = False
        self.shoot_width = 3


        self.shoot_surface = pygame.Surface(
                (self.shoot_size,
                 self.shoot_size),
                pygame.SRCALPHA)

        self.shoot_color = (255,255,255)
        self.shoot_current_size = self.normal_size # (w // 6)
        self.shoot_surface.set_colorkey((0, 0, 0)) 

    def reset_shooter(self):
        """ Reset shooter parameters """
        self.do_shoot = False
        self.shoot_width = 3
        self.shoot_alpha = 255
        self.shoot_color = (60, 60, 60)

        self.shoot_size = self.w // 2
        self.shoot_current_size = self.normal_size # (w // 6)

        self.shoot_surface = pygame.Surface(
                (self.shoot_size, self.shoot_size),
                pygame.SRCALPHA)

    def update(self):
        if self.do_shoot:
            if self.shoot_alpha <= 0:
                self.reset_shooter()
                return;

            self.shoot_alpha -= 5
            self.shoot_current_size += 5

            pygame.draw.circle(
                    self.shoot_surface,
                    self.shoot_color,
                    (self.shoot_current_size,
                     self.shoot_current_size),
                    self.shoot_current_size, 1)

            self.shoot_surface.set_alpha(self.shoot_alpha)
            self.image.blit(
                    self.shoot_surface,
                    (self.shoot_surface.get_width() // 2,
                     self.shoot_surface.get_height() // 2))

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)
