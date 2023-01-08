import random
import pygame


class Particle:
    doParticles: bool = False

    def __init__(self, pos, color) -> None:
        """ Instance constructor """
        self.pos = pos
        self.alpha = 255
        self.color = color
        self.active = True

        self.pos: pygame.math.Vector2 = pygame.math.Vector2(self.pos)
        self.acc = self.vel = pygame.math.Vector2()
        self.vel.x, self.vel.y = random.randint(0, 20) / 10 - 1, 2

        self.size = random.randint(4, 7)
        self.width, self.height = self.size, self.size

        self.rect: pygame.rect.Rect = pygame.Rect(
            self.width,
            self.height,
            self.pos.x,
            self.pos.y)

        self.image: pygame.surface.Surface = pygame.Surface(
                (self.width,
                 self.height),
                 pygame.SRCALPHA)
        self.image.set_colorkey((0,0,0))

    def move(self) -> None:
        """ Do particle  movement """
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.vel.y += 0.05 * (self.vel.y)  # Compounds over time
        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)

    def update(self) -> None:
        """ Update position """
        self.alpha -= 5

        if self.alpha <= 0:
            self.active = False
        elif self.size < 0:
            self.active = False

        self.move()

    def draw(self, surface) -> None:
        """ Blit image to surface """
        pygame.draw.circle(
                 self.image,
                 self.color,
                (self.size // 2,
                 self.size // 2),
                 self.size // 2)

        self.image.set_alpha(self.alpha)
        surface.blit(self.image, self.rect)
