import pygame
from pygame.sprite import Sprite

class ship(Sprite):
    def __init__(self, ai_seeting, screen):
        super(ship,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.ai_seeting = ai_seeting
        self.center = float(self.rect.centerx)
        self.ycenter = float(self.rect.centery)

    def updata(self):
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.center += self.ai_seeting.ship_speed_factor
        if self.moving_left:
            if self.rect.left > 0:
                self.center -= self.ai_seeting.ship_speed_factor
        if self.moving_up:
            if self.rect.top > 0:
                self.ycenter -= self.ai_seeting.ship_speed_factor
        if self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.ycenter += self.ai_seeting.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.centery = self.ycenter

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.ycenter = self.screen_rect.height-self.rect.height


