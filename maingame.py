import sys,pygame
from setting import game_setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button 
from scoreboard import Scoreboared

def run_game():
    game_sets = game_setting()

    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((game_sets.map_x,game_sets.map_y))
    pygame.display.set_caption("宇宙飞船游戏v1.2")
    play_button = Button(game_sets,screen,"Play")
    ships = Ship(screen,game_sets)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(game_sets,screen,ships,aliens)
    stats = GameStats(game_sets)
    sb = Scoreboared(game_sets,screen,stats)

    while True:
        

        gf.check_events(game_sets,screen,ships,bullets,play_button,stats,aliens,sb)

        if stats.game_active:
            ships.move_plan()
            gf.update_bullets(game_sets,bullets,aliens,screen,ships,sb,stats)
            gf.update_aliens(game_sets,aliens,ships,stats,screen,bullets,sb)

        gf.game_update(game_sets,screen,ships,aliens,bullets,play_button,stats,sb)

run_game()