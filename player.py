from pygame import Vector2, draw, key, K_a, K_d
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = key.get_pressed()

        if keys[K_a]:
            self.rotate(-dt)
        if keys[K_d]:
            self.rotate(dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt