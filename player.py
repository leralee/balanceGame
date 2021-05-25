import pygame
import math

from config import Config


class Player:
    def __init__(self, config: Config):
        self.config = config
        self.rect_1 = pygame.Rect(0, 0, config.player_width, config.player_height)
        self.rect_2 = pygame.Rect(0, 0, config.player_width, config.player_height)
        self.angle_player_1 = 180
        self.angle_player_2 = 0

        self.left = False
        self.right = False
        self.set_coordinates()

    def set_coordinates(self):
        self.rect_1.center = (
            self.config.circle_x - self.config.diameter_between_players / 2,
            self.config.circle_y
        )
        self.rect_2.center = (
            self.config.circle_x + self.config.diameter_between_players / 2,
            self.config.circle_y
        )

    def move(self):
        if self.left:
            self.angle_player_1 -= 2
            self.angle_player_2 -= 2
        if self.right:
            self.angle_player_1 += 2
            self.angle_player_2 += 2

        self.rect_1.center = (
            self.config.circle_x + self.config.diameter_between_players/2 * math.cos(self.angle_player_1 * math.pi / 180),
            self.config.circle_y + self.config.diameter_between_players/2 * math.sin(self.angle_player_1 * math.pi / 180)
        )
        self.rect_2.center = (
            self.config.circle_x + self.config.diameter_between_players / 2 * math.cos(self.angle_player_2 * math.pi / 180),
            self.config.circle_y + self.config.diameter_between_players / 2 * math.sin(self.angle_player_2 * math.pi / 180)
        )

    def show(self, screen):
        # pygame.draw.rect(screen, (23,54,23), self.rect_1)
        # pygame.draw.rect(screen, (23,54,23), self.rect_2)
        pygame.draw.circle(screen, ("red"), self.rect_1.center, self.config.player_radius)
        pygame.draw.circle(screen, ("blue"), self.rect_2.center, self.config.player_radius)

