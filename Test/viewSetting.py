class settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.name = "alien_invasion"
        self.ship_speed_factor = 5.0
        self.bullet_speech_factor = 2.5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullects_allow = 50
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direct = 1  # 1右移，-1左移
        self.ship_limit = 3
        self.speechup_scale = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speech_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direct = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speechup_scale
        self.bullet_speech_factor *= self.speechup_scale
        self.alien_speed_factor *= self.speechup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
