import sys
import pygame
from Test.bullet import bullet


def check_events(ship,screen,ai_setting,bullects):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_event(event,ship,ai_setting,screen,bullects)
        elif event.type == pygame.KEYUP:
            check_up_event(event,ship)



def check_down_event(event,ship,ai_setting,screen,bullects):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up=True
    elif event.key == pygame.K_DOWN:
        ship.moving_down=True
    elif event.key == pygame.K_SPACE:
        fire_bullect(ai_setting, screen, ship,bullects)
    elif event.key==pygame.K_q:
        sys.exit()

def check_up_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def updata_screen(ai_setting, screen, ship,bullects,alien):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    alien.blitme()
    for bullect in bullects.sprites():
        bullect.draw_bullet()
    pygame.display.flip()
def update_bullects(bullects):
    bullects.update()
    for bullect in bullects.copy():
        if bullect.rect.bottom <= 0:
            bullects.remove(bullect)
def fire_bullect(ai_setting,screen, ship,bullects):
    if len(bullects)<ai_setting.bullects_allow:
        new_bullet = bullet(ai_setting, screen, ship)
        bullects.add(new_bullet)