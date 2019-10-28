class game_stats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_ststs()
        self.game_active = False
        self.score = 0

    def reset_ststs(self):
        self.ship_left = self.ai_setting.ship_limit
