
class Config:
    def __init__(self):
        # главные настройки
        self.window_width = 480
        self.window_height = 640
        self.background_color = (0, 0, 0)
        self.fps = 100

        # настройки игрока
        self.player_radius = 15
        self.player_color_1 = (0, 0, 255)
        self.player_color_2 = (255, 0, 0)
        self.diameter_between_players = 200
        self.circle_x = self.window_width / 2
        self.circle_y = self.window_height - self.diameter_between_players / 2 - 20
        self.player_width = self.player_height = 10

        # настройки блока
