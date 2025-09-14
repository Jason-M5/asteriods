import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        velo = self.velocity
        new_radius = self.radius - ASTEROID_MAX_RADIUS / ASTEROID_KINDS
        angle_1 = velo.rotate(random.uniform(20, 50))
        angle_2 = velo.rotate(random.uniform(-20, -50))

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        else:
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = angle_1
            asteroid_2.velocity = angle_2
            self.kill()
        