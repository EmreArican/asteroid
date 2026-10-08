import pygame
from circleshape import CircleShape
import constants as C
from logger import log_state, log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, C.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= C.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            angle = random.uniform(20, 50)
            first_asteroid_angle = self.velocity.rotate(angle)
            second_asteroid_angle = self.velocity.rotate(-angle)
            new_radius = self.radius - C.ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_asteroid.velocity = first_asteroid_angle * 1.2
            second_asteroid.velocity = second_asteroid_angle * 1.2
