import pygame
import random

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def asteroid_split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        SPEED_INCREASE = 1.2
        
        split_angle = random.uniform(20, 50)
        ast1_direction = self.velocity.rotate(split_angle)
        ast2_direction = self.velocity.rotate(-1 * split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        astroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        astroid_one.velocity = ast1_direction * SPEED_INCREASE
        
        astroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        astroid_two.velocity = ast2_direction * SPEED_INCREASE

