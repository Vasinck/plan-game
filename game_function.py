import sys,pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown(event,game_sets,screen,ships,bullets,stats):
    if event.key == pygame.K_RIGHT:
        ships.moving_right = True
    elif event.key == pygame.K_LEFT:
         ships.moving_left =True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_sets,screen,ships,bullets)
    elif event.key == pygame.K_q:
        stats.save_heigh_scores(stats.high_score)
        sys.exit()

def check_keyup(event,ships):
    if event.key == pygame.K_RIGHT:
        ships.moving_right = False
    elif event.key == pygame.K_LEFT:
        ships.moving_left = False
 
def check_events(game_sets,screen,ships,bullets,play_button,stats,aliens,sb):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stats.save_heigh_scores(stats.high_score)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown(event,game_sets,screen,ships,bullets,stats)
            elif event.type == pygame.KEYUP:
                check_keyup(event,ships)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(stats,play_button,mouse_x,mouse_y,game_sets,screen,ships,aliens,bullets,sb)

def check_play_button(stats,play_button,mouse_x,mouse_y,game_sets,screen,ships,aliens,bullets,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        game_sets.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        game_sets.sounds = True
        game_sets.bg_sounds = True
        game_sets.aline_sounds = True

        alien_rechange_music(game_sets)
        sb.prep_hight_score()
        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        creat_fleet(game_sets,screen,ships,aliens)
        ships.center_ship()

def game_update(game_sets,screen,ships,aliens,bullets,play_button,stats,sb):
    screen.fill(game_sets.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ships.output() 
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    play_bg_music(game_sets)
    
    pygame.display.flip()

def update_bullets(game_sets,bullets,aliens,screen,ships,sb,stats):
    bullets.update()
    check_bullet_alien_collisions(game_sets,screen,ships,aliens,bullets,sb,stats)

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
def fire_bullet(game_sets,screen,ships,bullets):
    if len(bullets) < game_sets.bullet_allowed:
            new_bullet = Bullet(game_sets,screen,ships)
            bullets.add(new_bullet)
            play_bullet_music(game_sets)

def creat_fleet(game_sets,screen,ships,aliens):
    alien = Alien(game_sets,screen)
    number_aliens_x = get_number_aliens_x(game_sets,alien.rect.width)
    number_row = get_number_rows(game_sets,ships.rect.height,alien.rect.height)

    for row_number in  range(number_row):
        for aline_number in range(number_aliens_x):
            create_alien(game_sets,screen,aliens,aline_number,row_number)

def get_number_aliens_x(game_sets,alien_width):
    available_space_x = game_sets.map_x - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(game_sets,screen,aliens,alien_number,row_number):
    alien = Alien(game_sets,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number +50
    alien_rechange_music(game_sets)
    aliens.add(alien)

def get_number_rows(game_sets,ship_height,alien_height):
    available_space_y = (game_sets.map_y - (3 * alien_height) - ship_height)
    number_row = int(available_space_y / (2 * alien_height))
    return number_row

def update_aliens(game_sets,aliens,ships,stats,screen,bullets,sb):
    check_fleet_edges(game_sets,aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ships,aliens):
        ship_hit(game_sets,stats,screen,ships,aliens,bullets,sb)
    check_aliens_bottom(game_sets,stats,screen,ships,aliens,bullets,sb)

def check_fleet_edges(game_sets,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_sets,aliens)
            break

def change_fleet_direction(game_sets,aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_sets.fleet_drop_speed
    game_sets.fleet_direction *= -1

def check_bullet_alien_collisions(game_sets,screen,ships,aliens,bullets,sb,stats):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += game_sets.alien_points * len(aliens)
            sb.prep_score()

        check_hight_score(stats,sb)

    if len(aliens) == 0:
        bullets.empty()
        game_sets.increase_speed()

        stats.level += 1
        sb.prep_level()

        creat_fleet(game_sets,screen,ships,aliens)

def ship_hit(game_sets,stats,screen,ships,aliens,bullets,sb):
    if stats.ships_left > 0:
        alien_rechange_music(game_sets)
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()

        creat_fleet(game_sets,screen,ships,aliens)
        ships.center_ship()

        sleep(0.3)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(game_sets,stats,screen,ships,aliens,bullets,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_sets,stats,screen,ships,aliens,bullets,sb)
            break

def check_hight_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_hight_score()


def play_bullet_music(game_sets):
    if game_sets.sounds:
        fire_bullet_music = pygame.mixer.Sound('D://python源程序//飞机大战Ver1.0//123.ogg')
        fire_bullet_music.play()

def play_bg_music(game_sets):
    if game_sets.bg_sounds and not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('D://python源程序//飞机大战Ver1.0//bg_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

def alien_rechange_music(game_sets):
    alien_sound = pygame.mixer.Sound('D://python源程序//飞机大战Ver1.0//456.ogg')
    if game_sets.aline_sounds:
        alien_sound.set_volume(0.3)
        alien_sound.play()
