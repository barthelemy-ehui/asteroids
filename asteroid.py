from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
         pygame.draw.circle(screen,(255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position +=  dt * self.velocity;

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        rand = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vector1 = self.velocity.rotate(rand)
        vector2 = self.velocity.rotate(-rand)
        asteroid1 = Asteroid(self.position.x + rand, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x - rand, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2
