import pygame
import random
import math

from player import Player


class Block(pygame.Rect):
    def __init__(self, config):
        super().__init__(0 , 0 , 0 , 0)
        self.config = config
        self.speed = 2
        self.build()

    def build(self):
        block_type = random.randint(1, 3)
        if block_type == 1:
            self.width = (self.config.window_width / 2 - self.config.window_width / 3) * 2
            self.centerx = self.config.window_width/3
        elif block_type == 2:
            self.width = (self.config.diameter_between_players - self.config.diameter_between_players/2)
            self.centerx = self.config.window_width/2
            self.speed = 3
        elif block_type == 3:
            self.width = (self.config.window_width / 2 - self.config.window_width / 3) * 2
            self.centerx = self.config.window_width/3 * 2

        self.height = self.config.diameter_between_players / 4
        self.bottom = 0

    def collide_player(self, player: Player) -> bool:
        for angle in range(360):
            if self.collidepoint(
                player.rect_1.centerx + self.config.player_radius * math.cos(angle * math.pi / 180), #столкновение с первым игроком
                player.rect_1.centery + self.config.player_radius * math.sin(angle * math.pi / 180)
            ) or self.collidepoint(
                player.rect_2.centerx + self.config.player_radius * math.cos(angle * math.pi / 180), #столкновение со вторым игроком
                player.rect_2.centery + self.config.player_radius * math.sin(angle * math.pi / 180)
            ):
                return True
        return False



    def drop(self):
        self.move_ip(0, self.speed)
        # self.y += self.speed

    def show(self, screen):
        pygame.draw.rect(screen, "white", self)
