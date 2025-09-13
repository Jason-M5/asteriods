import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS
from shot import Shot



class Player(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0


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
        self.PLAYER_SHOOT_COOLDOWN -= dt

        if keys[pygame.K_a]:
            #print("a")
            self.rotate(-PLAYER_TURN_SPEED, dt)
            print(PLAYER_TURN_SPEED)
        if keys[pygame.K_d]:
            #print("d")
            self.rotate(PLAYER_TURN_SPEED, dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.PLAYER_SHOOT_COOLDOWN <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_position = self.position + forward * (self.radius + SHOT_RADIUS + 1)
            self.shoot(SHOT_RADIUS, shot_position, forward * PLAYER_SHOOT_SPEED)

    def shoot(self, radius, position, velocity):
        self.PLAYER_SHOOT_COOLDOWN = .3
        shot = Shot(position.x, position.y, radius)
        shot.velocity = velocity
  
