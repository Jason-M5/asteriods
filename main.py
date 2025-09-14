import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

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
    Shot.containers = (updatable, drawable)
    
    dt = 0.0

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid = AsteroidField()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(5)
        dt = clock.tick(60) / 1000
        
        updatable.update(dt)
        for draws in drawable:
            draws.draw(screen)



        for i in drawable:
            if player_1.collide(i) == True:
                print("Game Over!")
                sys.exit()

            if isinstance(i, Shot):
                screen.fill("white")
                screen.fill(5)
                for a in drawable:
                    if isinstance(a, Asteroid) and i.collide(a):
                        i.kill()
                        a.kill()


        pygame.display.flip()


if __name__ == "__main__":
    main()
