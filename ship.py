import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,game_sets):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("D://python源程序//飞机大战Ver1.0//ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.game_sets = game_sets
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def move_plan(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.center += self.game_sets.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
           self.center -= self.game_sets.ship_speed
        
        self.rect.centerx = self.center
    
    def output(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
    