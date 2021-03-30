import sys,pygame

class game_setting():
    def __init__(self):
        self.map_x = 1200
        self.map_y = 800
        self.bg_color = (230,230,230)
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 25

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.sounds = False
        self.bg_sounds = False
        self.aline_sounds = False
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction =1
        self.fleet_drop_speed = 10
        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= self.speedup_scale
        