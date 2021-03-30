import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,game_sets,screen):
        super().__init__()
        self.screen = screen
        self.game_sets = game_sets

        self.image = pygame.image.load("D://python源程序//飞机大战Ver1.0//alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def output(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        self.x += (self.game_sets.alien_speed * self.game_sets.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True