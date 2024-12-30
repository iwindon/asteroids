import pygame
from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create groups
    updatable = [player]
    drawable = [player]

    # Game Loop 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #player.update(dt)
        for obj in updatable:
            obj.update(dt)

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw player
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        # Update display
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # limit to 60 fps and convert from ms to seconds

    pygame.quit()

if __name__ == "__main__":
    main()
