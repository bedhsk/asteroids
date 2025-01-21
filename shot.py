from pygame import draw
from circleshape import CircleShape
from constants import SHOOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOOT_RADIUS)
        
    def draw(self, screen):
        draw.circle(screen, "white", self.position, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
