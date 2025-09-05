import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    #Shot.containers = (updatable, drawable)
    
    dt = 0.0

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid = AsteroidField()
    #shoot = Shot(player_1.position.x + PLAYER_RADIUS, player_1.position.y + PLAYER_RADIUS, SHOT_RADIUS)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        dt = clock.tick(60) / 1000
        #player_1.update(dt)
        #player_1.draw(screen)
        
        updatable.update(dt)
        for draws in drawable:
            draws.draw(screen)

        for i in drawable:
            if player_1.collide(i) == True:
                print("Game Over!")
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
