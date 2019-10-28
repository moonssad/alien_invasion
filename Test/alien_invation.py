import pygame
from pygame.sprite import Group

from Test.ship import ship
from Test.viewSetting import settings
import Test.game_function as gf

def run_game():
    pygame.init()
    ai_setting=settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.name)
    ai_ship=ship(ai_setting,screen)
    bullects=Group()
    ai_alien=Group()
    gf.create_fleet(ai_setting,screen,ai_ship,ai_alien)
    while True:
        gf.check_events(ai_ship,screen,ai_setting,bullects)
        ship.updata(ai_ship)
        gf.update_bullects(bullects)
        gf.update_aliens(ai_alien)
        gf.updata_screen(ai_setting,screen,ai_ship,bullects,ai_alien)

run_game()