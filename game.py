import pygame
import sys
import time

from player import Player

from config import Config

from blocks import Block




class Game:
    def __init__(self, config: Config, screen: pygame.Surface):
        self.config = config
        self.screen = screen
        self.player = Player(config)
        self.blocks = list()
        self.timer = pygame.time.Clock()

    def generate_block(self):
        self.blocks.append(Block(self.config))

    def start(self):
        self.generate_block()
        while True:
            self.get_input()
            self.player.move()
            self.move_blocks()
            self.update_screen()

    def move_blocks(self):
        for block in self.blocks:
            block.drop()
            if block.top >= self.config.window_height / 2 and len(self.blocks) < 2:
                self.generate_block()

            if block.top >= self.config.window_height:
                self.blocks.remove(block)
            if block.collide_player(self.player):
                time.sleep(2)
                pygame.quit()
                sys.exit()


    def update_screen(self):
        self.screen.fill(self.config.background_color)
        self.player.show(self.screen)
        for block in self.blocks:
            block.show(self.screen)
        self.timer.tick(self.config.fps)
        pygame.display.flip()

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.right = True
                if event.key == pygame.K_LEFT:
                    self.player.left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.right = False
                if event.key == pygame.K_LEFT:
                    self.player.left = False

        #
        # for block in self.blocks:
        #     pygame.draw.rect(self.screen , (12 , 23 , 54) , [block.x, block.y, 100, 40])
        #     block.x += 0
        #     block.y += 1
        #
        # if block.y > self.config.height:
        #     self.blocks = [Block(20,-40), Block(340,-40)]
