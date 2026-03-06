import pygame
import sys

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player_position = (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    Player.containers = (updatable, drawable) # type: ignore
    player = Player(player_position[0], player_position[1])

    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable) # type: ignore
    AsteroidField()

    Shot.containers = (shots, updatable, drawable) # type: ignore

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
        updatable.update(dt)        

        for ast in asteroids: 
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if ast.collides_with(s):
                    log_event("asteroid_shot")
                    ast.asteroid_split()
                    s.kill()

        for draw in drawable: draw.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        screen.fill("black")

if __name__ == "__main__":
    main()
