import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game_sets,screen,ships):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,game_sets.bullet_width,game_sets.bullet_height)
        self.rect.centerx = ships.rect.centerx
        self.rect.top = ships.rect.top

        self.y = float(self.rect.y)

        self.color = game_sets.bullet_color
        self.speed = game_sets.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    