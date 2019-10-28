import pygame
from pygame.sprite import Group

from Test.button import button
from Test.game_stats import game_stats
from Test.ship import ship
from Test.viewSetting import settings
import Test.game_function as gf


def run_game():
    pygame.init()
    ai_setting = settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.name)
    ai_ship = ship(ai_setting, screen)
    bullects = Group()
    ai_alien = Group()
    gf.create_fleet(ai_setting, screen, ai_ship, ai_alien)
    stats = game_stats(ai_setting)
    play_button=button(ai_setting, screen,"PLAY")
    while True:
        gf.check_events(ai_ship, screen, ai_setting, bullects,stats,play_button,ai_alien)
        gf.updata_screen(ai_setting, screen, ai_ship, bullects, ai_alien, stats, play_button)

        if stats.game_active:
            ship.updata(ai_ship)
            gf.update_bullets(bullects, ai_alien, ai_ship, ai_setting, screen)
            gf.update_aliens(ai_setting, ai_alien, ai_ship, stats, screen, bullects)

run_game()
