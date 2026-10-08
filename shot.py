from circleshape import CircleShape
import constants as C
import pygame

class Shot(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, C.SHOT_RADIUS)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, C.LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

