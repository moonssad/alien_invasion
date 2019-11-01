import sys
from time import sleep

import pygame

from Test.bullet import bullet
from Test.alien import Alien
import Test.ScoreSave as SV


def check_play_button(ai_setting, screen, stats, play_button, ship, aliens, bullects, mouse_x, mouse_y, sb):
    button_clicked = play_button.screen_rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_setting.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_ststs()
        stats.game_active = True
        sb.prep_score()
        sb.prep_hight_socre()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullects.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()


def check_events(ship, screen, ai_setting, bullects, stats, play_button, aliens, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_event(event, ship, ai_setting, screen, bullects)
        elif event.type == pygame.KEYUP:
            check_up_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats, play_button, ship, aliens, bullects, mouse_x, mouse_y, sb)


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


def updata_screen(ai_setting, screen, ship, bullects, alien, stats, play_button, sb):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    sb.show_score()

    # alien.blitme()
    alien.draw(screen)
    for bullect in bullects.sprites():
        bullect.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(bullets, aliens, ship, ai_setting, screen, stats, sb):
    bullets.update()
    for bullect in bullets.copy():
        if bullect.rect.bottom <= 0:
            bullets.remove(bullect)
    check_bullet_alien_collisions(bullets, aliens, ai_setting, screen, ship, stats, sb)


def check_bullet_alien_collisions(bullets, aliens, ai_setting, screen, ship, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points
            sb.prep_score()
        check_hight_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting, screen, ship, aliens)
        stats.level += 1
        sb.prep_score()


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
            create_alien(ai_setting, screen, aliens, alien_number, number_row)


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


def ship_hit(ai_setting, stats, screen, ship, aliens, bullets, sb):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
        sb.prep_ships()
        sleep(1.0)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets, sb):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets, sb)
            break


def update_aliens(ai_setting, aliens, ship, stats, screen, bullets, sb):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets, sb)


def change_fleet_direction(ai_setting, aliens):
    for alien in aliens:
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direct *= -1


def check_fleet_edges(ai_setting, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def check_hight_score(stats, sb):
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        SV.write_score(stats.hight_score)
        sb.prep_hight_socre()

