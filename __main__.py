import pygame
from map.map import Map
from characters.puppy import Puppy
from pygame.locals import *

height = 600
width = 400


def run_game():
    try:
        pygame.init()

        screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption('The Saddest Pup')

        screen.fill((42, 42, 42))

        game_map = Map(size=14, screen=screen)

        puppy = Puppy()

        game_map.draw_map()

        player = pygame.sprite.RenderPlain(puppy)

        player.draw(screen)

        pygame.display.update()

        game_running = True

        while game_running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_running = False
                    break

    finally:
        pygame.quit()


if __name__ == "__main__":
    run_game()