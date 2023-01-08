"""
main.py
Author: Joshua Rose
Email: joshuarose099@gmail.com
"""

import math
import random

from consts import *
from enemy import Enemy
from player import Player
from recticle import Recticle
from particle import Particle

import pygame

pygame.init()


class WindowProperties(object):
    def __init__(self) -> None:
        self.width  = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.clock = pygame.time.Clock()

        self.fps = 60
        self.flags = 0
        self.depth = 32
        self.running = 1
        self.mx = 0
        self.my = 0

        self.keys = {
                'w': 0,
                'a': 0,
                'r': 0,
                's': 0}

        self.offset = self.offset_vel = pygame.math.Vector2()

        self.bullets = []
        self.enemies = []
        self.particles = []
        self.enemy_spawns = []

        pygame.mouse.set_visible(False)

        self.recticle = Recticle(
                self.mx,
                self.my,
                100, 100)

        self.player = Player(self.width // 2 - 50 // 2,
                               self.height // 2 - 50 // 2,
                               50, 50)

    def generate_spawn(self) -> tuple:
        """ Generate entity spawn (negates player entity area) """
        x = random.choice([
                random.randint(-self.width, 0),
                random.randint(self.width, self.width*2)])

        y = random.choice([
                random.randint(-self.height, 0),
                random.randint(self.height, self.height*2)])
        return (x, y)

    def spawn_enemies(self, amount=1):
        """ Spawn entity sprite objets """
        for _ in range(amount):
            x, y = self.generate_spawn()
            size = random.randint(20, 30)
            enemy = Enemy(x, y, size, size)
            self.enemies.append(enemy)
            del enemy, x, y, size

    def camera_movement(self):
        """ Move all entities, creating a camera 'illusion'"""
        if self.keys['s']:
            if self.offset_vel.x < MAXVEL:
                self.offset_vel.x += ACC
            else:
                self.offset_vel.x = MAXVEL
            self.offset.x += math.floor(self.offset_vel.x)
        elif self.keys['a']:
            if self.offset_vel.x < MAXVEL:
                self.offset_vel.x += ACC
            else:
                self.offset_vel.x = MAXVEL
            self.offset.x += -math.floor(self.offset_vel.x)
        if self.keys['r']:
            if self.offset_vel.y < MAXVEL:
                self.offset_vel.y += ACC
            else:
                self.offset_vel.y = MAXVEL
            self.offset.y += math.floor(self.offset_vel.y)
        elif self.keys['w']:
            if self.offset_vel.y < MAXVEL:
                self.offset_vel.y += ACC
            else:
                self.offset_vel.y = MAXVEL
            self.offset.y += -math.floor(self.offset_vel.y)

    def handle_events(self):
        """ process events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.close()
                if event.key == pygame.K_w: self.keys['w'] = 1
                if event.key == pygame.K_a: self.keys['a'] = 1
                if event.key == pygame.K_r: self.keys['r'] = 1
                if event.key == pygame.K_s: self.keys['s'] = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: self.keys['w'] = 0
                if event.key == pygame.K_a: self.keys['a'] = 0
                if event.key == pygame.K_r: self.keys['r'] = 0
                if event.key == pygame.K_s: self.keys['s'] = 0
            if event.type == pygame.MOUSEMOTION:
                self.mx, self.my = pygame.mouse.get_pos()
                self.recticle.rect.center = (  # pyright: ignore
                        self.mx, self.my)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # self.recticle.do_shoot = True
                pass # FIXME ensure recticle size fits for fx

    def close(self):
        pygame.display.quit()
        exit()

window = WindowProperties()

DISPLAY = pygame.display.set_mode(
        (window.width,
         window.height),
         window.flags,
         window.depth)

window.spawn_enemies(2)

dt = 0
mx = my = 0
max_enemies = 2

def generate_particles(x, y, amount, color):
    for _ in range(amount):
        window.particles.append(Particle((x, y), color))

while window.running:
    DISPLAY.fill((0,0,0))

    window.handle_events()
    window.camera_movement()

    window.player.draw(DISPLAY, window.mx, window.my)

    for enemy in window.enemies:
        """
        NOTE: this code block causes known bugs.
        if len(window.enemies) > max_enemies:
            window.enemies.remove(enemy)
            continue # go to start of loop
        """
        if enemy.active:
            enemy.update(window.player.rect)
            enemy.draw(DISPLAY)
            pygame.draw.line(
                    DISPLAY,
                    (255,255,255),
                    enemy.rect.center,
                    window.player.rect.center, 2)
        else:
            generate_particles(
                    enemy.rect.centerx,
                    enemy.rect.centery,
                    random.randint(3, 7),
                    enemy.color)
            window.enemies.remove(enemy)
            max_enemies += 0.25
            if len(window.enemies) < round(max_enemies):
                window.spawn_enemies(
                        round(max_enemies) - len(window.enemies))
                continue
            else:
                window.spawn_enemies(1)

    for particle in window.particles:
        if particle.active:
            particle.update()
            particle.draw(DISPLAY)
        else:
            window.particles.remove(particle)

    window.recticle.draw(DISPLAY)

    pygame.display.update()
    dt = window.clock.tick(window.fps) * 0.001
