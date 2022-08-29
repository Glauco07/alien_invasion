import sys

import pygame


def run_game():
    '''initializes the game and and create an object for the screen'''
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))  # window dimensions
    pygame.display.set_caption('Alien Invasion')

    while True:
        # listen to mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()
