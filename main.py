import pygame
import sys
from asteroidfield import AsteroidField
import constants as C
from logger import log_state, log_event
from player import Player
import shot as S
from asteroid import Asteroid

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")
    
    pygame.init()
    clock: Clock = pygame.time.Clock()
    dt: float = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    S.Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for e in asteroids:
            for el in shots:
                if e.collide(el):
                    log_event("asteroid_shot")
                    e.split()
            if e.collide(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
