import pygame

from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    dt = 0
    
    player_position = (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    player = Player(player_position[0], player_position[1])

    while True:
        log_state()
        player.update(dt=dt)
        player.draw(screen=screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        screen.fill("black")

if __name__ == "__main__":
    main()
