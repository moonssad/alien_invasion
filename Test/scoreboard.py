import pygame
from pygame.sprite import Group

from Test.ship import ship


class scoreboard():
    def __init__(self, ai_setting, screen, stats):
        self.ai_setting = ai_setting
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)
        self.prep_score()
        self.prep_hight_socre()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_hight_socre(self):
        hight_score = int(round(self.stats.hight_score, -1))
        hight_score_str = "{:,}".format(hight_score)
        self.hight_score_image = self.font.render(hight_score_str, True, self.text_color, self.ai_setting.bg_color)
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.center = self.screen_rect.center
        self.hight_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_numer in range(self.stats.ship_left):
            Ship = ship(self.ai_setting, self.screen)
            Ship.rect.x = 10 + ship_numer * Ship.rect.width
            Ship.rect.y = 10
            self.ships.add(Ship)
