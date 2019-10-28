import sys
import pygame

from Test.bullet import bullet
from Test.alien import Alien


def check_events(ship, screen, ai_setting, bullects):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_event(event, ship, ai_setting, screen, bullects)
        elif event.type == pygame.KEYUP:
            check_up_event(event, ship)


def check_down_event(event, ship, ai_setting, screen, bullects):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullect(ai_setting, screen, ship, bullects)
    elif event.key == pygame.K_q:
        sys.exit()


def check_up_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def updata_screen(ai_setting, screen, ship, bullects, alien):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # alien.blitme()
    alien.draw(screen)
    for bullect in bullects.sprites():
        bullect.draw_bullet()
    pygame.display.flip()


def update_bullects(bullects):
    bullects.update()
    for bullect in bullects.copy():
        if bullect.rect.bottom <= 0:
            bullects.remove(bullect)


def fire_bullect(ai_setting, screen, ship, bullects):
    if len(bullects) < ai_setting.bullects_allow:
        new_bullet = bullet(ai_setting, screen, ship)
        bullects.add(new_bullet)


# 创建外星人群
def create_fleet(ai_setting, screen, ship, aliens):
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number,number_row)


def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_setting, screen, aliens, aliens_number, row_number):
    Alien1 = Alien(ai_setting, screen)
    alien_width = Alien1.rect.width
    Alien1.x = alien_width + 2 * alien_width * aliens_number
    Alien1.rect.x = Alien1.x
    Alien1.rect.y = Alien1.rect.height + 2 * Alien1.rect.height * row_number

    aliens.add(Alien1)


def get_number_rows(ai_setting, ship_height, alien_height):
    available_space_y = ai_setting.screen_height - ship_height - 3 * alien_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(aliens):
    aliens.update()