import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_SPEED, SHOT_RADIUS


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #print(self.triangle())
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

    def rotate(self, PLAYER_TURN_SPEED, dt):
        print(self.rotation)
            
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            print("a")
            self.rotate(-PLAYER_TURN_SPEED, dt)
            print(PLAYER_TURN_SPEED)
        if keys[pygame.K_d]:
            print("d")
            self.rotate(PLAYER_TURN_SPEED, dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        
        shot = Shot(self.position.x + self.radius, self.position.y + self.radius, SHOT_RADIUS)
        shot.rotate(Player.rotate())
        shot.velocity = SHOT_SPEED





class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
        
        
