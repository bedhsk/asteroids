from shot import Shot
from circleshape import CircleShape
from pygame import Vector2, draw, key, K_a, K_d, K_w, K_s, K_SPACE
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

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
        self.shoot_timer -= dt
        keys = key.get_pressed()

        if keys[K_w]:
            self.move(dt)
        if keys[K_s]:
            self.move(-dt)
        if keys[K_a]:
            self.rotate(-dt)
        if keys[K_d]:
            self.rotate(dt)
        if keys[K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
