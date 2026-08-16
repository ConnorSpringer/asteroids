import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface.Surface):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt:float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vel_1 = self.velocity.rotate(angle)
            vel_2 = self.velocity.rotate(-angle)
            r = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(*self.position,radius=r)
            asteroid_2 = Asteroid(*self.position,radius=r)
            asteroid_1.velocity = vel_1
            asteroid_2.velocity = vel_2