import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()