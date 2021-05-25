import pygame

from config import Config
from blocks import Block
from game import Game





def run():
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Balance")

    config = Config()
    screen = pygame.display.set_mode((config.window_width, config.window_height))

    game = Game(config, screen)
    game.start()


run()





