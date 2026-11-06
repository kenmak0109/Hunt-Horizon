"""
This is a software project for HKUSPACE CCIT4080B-CL09, Project on Knowledge Products Development(PKPD), Group 7, year 2021-2022
Most of the images or graphics are designed by our own
Sound content are found from the internet free of charge
"""
"""Reference (IEEE):
        1) Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
        2) Clear Code. "Creating a health bar in pygame [Dark Souls style]." Youtube,
                Oct. 2, 2020 [Video file]. Available: https://www.youtube.com/watch?v=pUEZbUAMZYA&ab_channel=ClearCode. [Accessed: Apr. 13, 2022]
        3) Clear Code. "Creating an animated button in Pygame." Youtube, 
                Jul. 4, 2021 [Video file]. Available: https://www.youtube.com/watch?v=8SzTzvrWaAA&t=1365s&ab_channel=ClearCode
        """

"""Source of Materials used:
        1) font: https://www.fontspace.com/haeres-letter-font-f53961
        2) sound: https://www.fesliyanstudios.com/sound-effects-search.php?q=throw
                  https://www.fesliyanstudios.com/sound-effects-search.php?q=coin
        """
import pygame, time, sys, math, os, collections, decimal
import json

class Settings(object):
    pygame.init()

    # screen attritute
    win_width = 800
    win_height = 600
    max_level = 2
    total_level = 10
    timeout = False
    # Initialize font
    font = os.path.join('assets/font', 'haeres.ttf')
    font_size = 36
    shop_font_size = 20
    interface_font = pygame.font.Font(font, font_size)
    shop_font = pygame.font.Font(font, shop_font_size)

    player_width = 30
    player_height = 40
    coin_point = 50
    coin_random_list = [False,False,False,False,True]

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    # initialize a dictionary for file I/O
    upgrades = collections.OrderedDict()
    upgrades['Attack damage'] = {
        'name': 'Attack damage',
        'current': 1,
        'default': 1,
        'increase': 0.5,
        'level': 1,
        'base cost': 1000
    }
    upgrades['Attack frequency'] = {
        'name': 'Attack frequency',
        'current': 1,
        'default': 1,
        'increase': 0.1,
        'level': 1,
        'base cost': 1000
    }
    upgrades['Bullet velocity'] = {
        'name': 'Bullet velocity',
        'current': 3,
        'default': 3,
        'increase': 1.5,
        'level': 1,
        'base cost': 1000
    }
    upgrades['Max health'] = {
        'name': 'Max health',
        'current': 10,
        'default': 10,
        'increase': 5,
        'level': 1,
        'base cost': 1000
    }
    upgrades['Barrier'] = {
        'name': 'Barrier',
        'invincible': 5,
        'cooldown': 45,
        'level': 0,
        'cost': 5000,
        'cost_interval': 7500,
        'is brought': False
    }
    upgrades['Dash'] = {
        'name': 'Dash',
        'charge': 1,
        'cooldown': 20,
        'level': 0,
        'cost': 5000,
        'cost_interval': 7500,
        'is brought': False
    }
    upgrades['Grenade'] = {
        'name': 'Grenade',
        'diameter': 3 * player_width,
        'charge': 2,
        'cooldown': 15,
        'damage': 3,
        'level': 0,
        'cost': 2000,
        'is brought': False
    }
    upgrades['Laser'] = {
        'name': 'Laser',
        'cooldown': 40,
        'level': 0,
        'cost': 5000,
        'is brought': False
    }
    upgrades['Skin'] = {
        'name': 'Skin',
        'red': False,
        'green': False,
        'orange': False,
        'yellow': False,
        'cost': 4000
    }
    upgrades['User point'] = {
        'name': 'User point',
        'point': 0
    }
    upgrades['Sound'] = {
        'name': 'Sound',
        'main volume': 100,
        'bgm volume': 100,
        'effect volume': 100,
        'actual main volume': 0.5,
        'actual bgm volume': 0.5,
        'actual effect volume': 0.5
    }
    upgrades['Multi shot'] = {
        'name': 'Multi shot',
        'current': 1,
        'default': 1,
        'increase': 1,
        'level':1,
        'base cost': 5000
    }
    upgrades['Bullet number'] = {
        'name': 'Bullet number',
        'current': 1,
        'default': 1,
        'increase': 1,
        'level': 1,
        'base cost': 5000
    }
    try:
        with open('save.txt') as save_file:
            upgrades = json.load(save_file)
    except:
        with open('save.txt', 'w') as create_file:
            json.dump(upgrades, create_file)

    # Initialize sprite groups
    player_group = None
    player_bullet_group = None
    enemy_group = None
    enemy_projectile_group = None
    coin_group = None

    # ----------Initialize interface data-------------
    # point
    point = 0
    point_surface = None
    point_earned = 0
    # time
    time_clock = [0,0,0,0,0,0]
    time_stage_begin = 0
    time_last_update = 0
    time_changed_between_update = 0
    time_passed_surface = None
    # stage info
    stage_info = ''
    stage = 0
    difficulty = 0
    stage_info_surface = None
    # player health
    player_health = None
    player_health_image = None
    player_health_image_size = 25
    player_health_list = []
    player_health_image_index = 0
    # boss health and name
    boss_name = ''
    boss_name_surface = None
    boss_health = 0
    boss_health_factor = 50
    boss_target_health = 0
    boss_max_health = 0
    boss_health_bar_length = 500
    boss_health_bar_ratio = 0
    boss_health_change_speed = 0
    boss_health_transition_width = 0
    boss_health_transition_color = (0, 0, 0)
    boss_health_bar_blit_x = 150
    boss_health_bar_blit_y = 30
    boss_health_bar = None
    boss_health_transition_bar = None
    # skill box
    skill_box_font_size = 15
    skill_box_font = pygame.font.SysFont('Comic Sans MS', skill_box_font_size)
    # barrier
    ui_barrier_image = None
    ui_barrier_box = None
    ui_barrier_cd = None
    ui_barrier_text_surf = None
    # dash
    ui_dash_image = None
    ui_dash_box = None
    ui_dash_cd = None
    ui_dash_text_surf = None
    # grenade
    ui_grenade_image = None
    ui_grenade_box = None
    ui_grenade_cd = None
    ui_grenade_text_surf = None
    # laser
    ui_laser_image = None
    ui_laser_box = None
    ui_laser_cd = None
    ui_laser_text_surf = None

    #------------------------------------------
    # game music volume control
    music_volume_bar_length = 300
    music_volume_factor = music_volume_bar_length
    music_volume_ratio = 1 / music_volume_bar_length
    actual_main_volume = upgrades['Sound']['actual main volume']
    actual_bgm_volume = upgrades['Sound']['actual bgm volume']
    actual_effect_volume = upgrades['Sound']['actual effect volume']
    main_volume_current = upgrades['Sound']['main volume']
    bgm_volume_current = upgrades['Sound']['bgm volume']
    effect_volume_current = upgrades['Sound']['effect volume']
    main_volume = None
    bgm_volume = None
    effect_volume = None

    # player attribute
    player = None
    player_initial_pos = (win_width/2, win_height - 40)
    player_boat_width = 45
    player_boat_height = 55
    player_speed = 3
    player_skin = 'blue.png'
    player_hp = upgrades['Max health']['current']
    player_bullet_frequency = upgrades['Attack frequency']['current']
    player_bullet_density = upgrades['Attack frequency']['current'] * 0.4
    grenade_animation_list = []
    player_grenade_mask = None
    player_grenade_pos = (0,0)
    player_grenade_hit_time = 0
    player_laser_mask = None

    current_game_surface = None
    gameplay_is_on = False

    # enemy data
    boss = None
    boss_is_spawn = False
    # phase data
    phase_change_time = 5
    enemy_shoot_frequency = 1.5
    boss_cycle = phase_change_time * 5
    gameplay_is_paused = False
    # data for bullet
    last_bullet = time.time()
    last_projectile = time.time()
    last_bullet_frequency = time.time()

    # data for spawning enemies in targeted type
    time_TypeA = time.time()
    time_TypeB = time.time()
    time_TypeC = time.time()
    time_TypeD = time.time()
    time_TypeE = time.time()
    time_TypeF = time.time()
    time_TypeG = time.time()
    time_TypeH = time.time()
    time_TypeI = time.time()
    time_TypeJ = time.time()
    time_TypeK = time.time()
    time_TypeL = time.time()
    time_TypeM = time.time()

    # size of enemy spawn is types of movement
    typeA_size = 6
    typeB_size = 7
    typeC_size = 7
    typeD_size = 0
    typeE_size = 16
    typeF_size = 12
    typeG_size = 6
    typeH_size = 8
    typeI_size = 8
    typeJ_size = 7
    typeK_size = 1
    typeL_size = 1
    typeM_size = 1

    # special projectile data
    counter_typeI = 6
    counter_typeJ = 6
    counter_typeL = 3
    counter_typeM = 3

    # --------------initialize sound---------------
    # bgm
    bgm_mainmenu = None
    bgm_gameover = None
    bgm_mission_complete = None
    bgm_s1 = None
    bgm_s2 = None
    bgm_s3 = None
    bgm_s4 = None
    bgm_s5 = None
    bgm_s6 = None
    bgm_s7 = None
    bgm_s8 = None
    bgm_s9 = None
    bgm_s10 = None
    bgm_shop = None
    # effect
    sound_boss_appear = None
    sound_boss_dead = None
    sound_button_clicked = None
    sound_enemy_appear = None
    sound_enemy_defeated = None
    sound_enemy_group_appear = None
    sound_enemy_shoot1 = None
    sound_enemy_shoot2 = None
    sound_player_boat = None
    sound_player_dead = None
    sound_player_shoot = None
    sound_shop_buy_item = None
    sound_target_hit = None
    sound_player_barrier_on = None
    sound_player_barrier_broken = None
    sound_player_dash = None
    sound_player_grenade = None
    sound_player_throw_grenade = None
    sound_player_laser = None
    sound_coin_collcet = None
    sound_coin_drop = None


    # framerate attribute
    clock = pygame.time.Clock()
    fps = 60
    ticks = 0

    # point for testing
    user_point = upgrades['User point']['point']

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def set_sprite_groups(player_group, player_bullet_group, enemy_group, enemy_projectile_group, coin_group):
        Settings.player_group = player_group
        Settings.player_bullet_group = player_bullet_group
        Settings.enemy_group = enemy_group
        Settings.enemy_projectile_group = enemy_projectile_group
        Settings.coin_group = coin_group

    @staticmethod
    def clock_update():
        Settings.clock.tick(Settings.fps)

    @staticmethod
    def check_event():
        for event in pygame.event.get():  # close the game
            if event.type == pygame.QUIT:
                with open('save.txt','w') as save_file:
                    json.dump(Settings.upgrades, save_file)
                Settings.close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
            elif event.type == pygame.KEYDOWN:
                if Settings.gameplay_is_on:
                    if event.key == pygame.K_ESCAPE and not Settings.gameplay_is_paused:
                        Settings.gameplay_is_paused = True
                    elif event.key == pygame.K_ESCAPE and Settings.gameplay_is_paused:
                        Settings.gameplay_is_paused = False

    @staticmethod
    def initialize_player_skill():
        Settings.player_grenade_mask = None
        Settings.player_grenade_hit_time = 0
        Settings.player_grenade_pos = (0, 0)
        Settings.player_grenade_hit_time = 0
        Settings.player_laser_mask = None
        Settings.player_laser_hit_time = 0

    @staticmethod
    def import_grenade_animation_image():
        for i in range(10):
            image_path = os.path.join('assets/graphics/explosion/explosion_'+str(i)+'.png')
            Settings.grenade_animation_list.append(pygame.transform.scale(
                pygame.image.load(image_path),
                (Settings.upgrades['Grenade']['diameter'], Settings.upgrades['Grenade']['diameter'])))
        return Settings.grenade_animation_list

    @staticmethod
    def get_mouse_pos():
        return pygame.mouse.get_pos()

    @staticmethod
    def close_game():
        pygame.quit()
        sys.exit()

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def update_user_point_stage():
        Settings.user_point += Settings.point
        Settings.upgrades['User point']['point'] = Settings.user_point

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def update_user_point(cost: int):
        Settings.user_point = Settings.user_point - cost
        Settings.upgrades['User point']['point'] = Settings.user_point

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def time() -> float:
        return time.time()

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def insert_player_sprite(player):
        Settings.player = player

    @staticmethod
    def insert_boss_sprite(boss):
        Settings.boss = boss

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def multi_shot_angles(number_of_shots: int, base_angle: float,
                          angle_increment: float) -> list:
        """Example result with base_angle = 90, angle_increment = 10:
        [90, 100, 80, 110, 70, 120, 60, 130, ...]"""

        if number_of_shots % 2 == 0:
            shot_angles = [base_angle-10]
            for i in range(number_of_shots):
                if i % 2 == 0:
                    shot_angles.append(shot_angles[i] + 10 + ((i + 1) * angle_increment * math.pow(-1, i)))
                else:
                    shot_angles.append(shot_angles[i] - 10 + ((i + 1) * angle_increment * math.pow(-1, i)))
            return shot_angles
        else:
            shot_angles = [base_angle]
            for i in range(number_of_shots):
                shot_angles.append(shot_angles[i] + ((i + 1) * angle_increment * math.pow(-1, i)))
            return shot_angles
        """Example result with base_angle = 90, angle_increment = 10:
                        [80, 100, 70, 110, 60, 120, 50, 130, ...]"""

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def angle_to_point(point1: tuple, point2: tuple) -> float:
        distance_x = point2[0] - point1[0]
        distance_y = point2[1] - point1[1]
        angle = math.degrees(math.atan2(-distance_y, distance_x))
        return Settings.normalize_angle(angle)

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def normalize_angle(angle: float):
        new_angle = angle
        while new_angle < 0:
            new_angle += 360
        while new_angle > 360:
            new_angle -= 360
        return new_angle

    @staticmethod
    def animation_button_mask():
        mouse_surf = pygame.Surface((1,1))
        mouse_rect = mouse_surf.get_rect(center = (400,200))
        mouse_rect.center = Settings.get_mouse_pos()
        return pygame.mask.from_surface(mouse_surf)

    @staticmethod
    def get_player_bullet_image():
        if Settings.upgrades['Attack damage']['level'] == 1:
            return 'player_bullet_white.png'
        elif Settings.upgrades['Attack damage']['level'] == 2:
            return 'player_bullet_green.png'
        elif Settings.upgrades['Attack damage']['level'] == 3:
            return 'player_bullet_blue.png'
        elif Settings.upgrades['Attack damage']['level'] == 4:
            return 'player_bullet_purple.png'
        elif Settings.upgrades['Attack damage']['level'] == 5:
            return 'player_bullet_yellow.png'
        elif Settings.upgrades['Attack damage']['level'] == 6:
            return 'player_bullet_red.png'
        else:
            return 'player_bullet_white.png'

    """@staticmethod
    def random_player_skin():
        if Settings.upgrades['Skin']['red']:
            Settings.player_skin_list.append('red.png')
        if Settings.upgrades['Skin']['green']:
            Settings.player_skin_list.append('green.png')
        if Settings.upgrades['Skin']['yellow']:
            Settings.player_skin_list.append('yellow.png')
        if Settings.upgrades['Skin']['orange']:
            Settings.player_skin_list.append('orange.png')"""

    @staticmethod
    def menu_difficulty_blit(difficulty):
        if difficulty == 0:
            return 'Easy'
        if difficulty == 1:
            return 'Normal'
        if difficulty == 2:
            return 'Hard'

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def set_point(new_point):
        Settings.point = new_point
        Settings.point_surface = Settings.interface_font.render('Point: %d'
                                                        % Settings.point,
                                                        True, (0, 0, 0))

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def change_point(change_amount):
        Settings.point += change_amount
        Settings.point_surface = Settings.interface_font.render('Point: %d'
                                                                  % Settings.point,
                                                                  True, (0, 0, 0))


    @staticmethod
    def stage_info_setup():
        if Settings.difficulty == 0:
            difficulty_str = 'Easy'
        if Settings.difficulty == 1:
            difficulty_str = 'Normal'
        if Settings.difficulty == 2:
            difficulty_str = 'Hard'
        Settings.stage_info = 'Level-' + str(Settings.stage) + '-' + difficulty_str
        Settings.stage_info_surface = Settings.interface_font.render(Settings.stage_info, True, (0, 0, 0))

    @staticmethod
    def set_time_clock():
        Settings.time_clock = [0,0,0,0,0,0]
        Settings.time_last_update = 0

    @staticmethod
    def update_time_passed():
        if not Settings.time_last_update == 0:
            Settings.time_changed_between_update = Settings.time() - Settings.time_last_update
        else:
            Settings.time_changed_between_update = 0
        time_passed_str = Settings.time_passed_for_display()
        Settings.time_passed_surface = Settings.interface_font.render(time_passed_str, True, (0, 0, 0))
        Settings.time_last_update = Settings.time()

    @staticmethod
    def time_passed_for_display():
        # 00:00:00 (min:sec:minisec*10)
        clock = Settings.time_clock
        scaled_time = Settings.time_changed_between_update * 100
        clock[5] += scaled_time
        while clock[5] >= 10:
            clock[4] += 1
            clock[5] -= 10
        while clock[4] >= 10:
            clock[3] += 1
            clock[4] -= 10
        while clock[3] >= 10:
            clock[2] += 1
            clock[3] -= 10
        while clock[2] >= 10:
            clock[1] += 1
            clock[2] -= 10
        while clock[1] >= 10:
            clock[0] += 1
            clock[1] -= 10
        while clock[0] >= 10:
            Settings.timeout = True
        for i in range(6):
            Settings.time_clock[i] = clock[i]
        return '%d%d:%d%d:%d%d' % (Settings.time_clock[0],Settings.time_clock[1],Settings.time_clock[2]
                                   ,Settings.time_clock[3],Settings.time_clock[4],Settings.time_clock[5])

    @staticmethod
    def update_player_health_image():
        if Settings.player.hp > 0:
            if len(Settings.player_health_list) - Settings.player.hp > 0:
                for i in range(len(Settings.player_health_list) - Settings.player.hp):
                    Settings.player_health_list.pop()

    @staticmethod
    def initialize_skill_box():
        skill_box_image = pygame.image.load(os.path.join('assets/images/ui/skill_box.png'))
        skill_box_image_cd = pygame.image.load(os.path.join('assets/images/ui/selected_skill_box.png'))
        # barrier
        image = pygame.image.load(os.path.join('assets/images/item/skill/barrier.png'))
        Settings.ui_barrier_box = pygame.transform.scale(skill_box_image, (50, 50))
        Settings.ui_barrier_cd = pygame.transform.scale(skill_box_image_cd, (50, 50))
        Settings.ui_barrier_image = pygame.transform.scale(image, (50, 50))
        Settings.ui_barrier_text_surf = Settings.skill_box_font.render('Q', True, (0,0,255))
        # dash
        image = pygame.image.load(os.path.join('assets/images/item/skill/dash.png'))
        Settings.ui_dash_box = pygame.transform.scale(skill_box_image, (50, 50))
        Settings.ui_dash_cd = pygame.transform.scale(skill_box_image_cd, (50, 50))
        Settings.ui_dash_image = pygame.transform.scale(image, (50, 50))
        Settings.ui_dash_text_surf = Settings.skill_box_font.render('W', True, (0, 0, 255))
        # grenade
        image = pygame.image.load(os.path.join('assets/images/item/skill/grenade.png'))
        Settings.ui_grenade_box = pygame.transform.scale(skill_box_image, (50, 50))
        Settings.ui_grenade_cd = pygame.transform.scale(skill_box_image_cd, (50, 50))
        Settings.ui_grenade_image = pygame.transform.scale(image, (50, 50))
        Settings.ui_grenade_text_surf = Settings.skill_box_font.render('E', True, (0, 0, 255))
        # laser
        image = pygame.image.load(os.path.join('assets/images/item/skill/laser.png'))
        Settings.ui_laser_box = pygame.transform.scale(skill_box_image, (50, 50))
        Settings.ui_laser_cd = pygame.transform.scale(skill_box_image_cd, (50, 50))
        Settings.ui_laser_image = pygame.transform.scale(image, (50, 50))
        Settings.ui_laser_text_surf = Settings.skill_box_font.render('R', True, (0, 0, 255))

    @staticmethod
    def initialize_boss_data():
        Settings.boss_health = Settings.boss_max_health
        Settings.boss_target_health = Settings.boss_max_health
        Settings.boss_health_change_speed = 5
        Settings.boss_health_transition_color = (255,0,0)
        Settings.boss_health_transition_width = 0
        Settings.boss_name = 'Boss'
        Settings.boss_name_surface = Settings.interface_font.render(Settings.boss_name,
                                                        True, (255, 0, 0))

    """Reference: Clear Code. "Creating a health bar in pygame [Dark Souls style]." Youtube,
                    Oct. 2, 2020 [Video file]. Available: https://www.youtube.com/watch?v=pUEZbUAMZYA&ab_channel=ClearCode. [Accessed: Apr. 13, 2022]"""
    @staticmethod
    def update_boss_health_data():
        if Settings.boss_target_health >= 0 and Settings.boss_target_health <= Settings.boss_max_health:
            Settings.boss_target_health = Settings.boss.hp * Settings.boss_health_factor
        if Settings.boss_target_health > Settings.boss_max_health:
            Settings.boss_target_health = Settings.boss_max_health
        if Settings.boss_target_health < 0:
            Settings.boss_target_health = 0
        if Settings.boss_health < Settings.boss_target_health:
            Settings.boss_health += Settings.boss_health_change_speed
            Settings.boss_health_transition_width = int((Settings.boss_target_health - Settings.boss_health) / Settings.boss_health_bar_ratio)
            Settings.boss_health_transition_color = (0, 255, 0)
        if Settings.boss_health > Settings.boss_target_health:
            Settings.boss_health -= Settings.boss_health_change_speed
            Settings.boss_health_transition_width = int((Settings.boss_health - Settings.boss_target_health) / Settings.boss_health_bar_ratio)
            Settings.boss_health_transition_color = (255, 255, 0)
        health_bar_width = int(Settings.boss_target_health / Settings.boss_health_bar_ratio)
        Settings.boss_health_bar = pygame.Rect(Settings.boss_health_bar_blit_x, Settings.boss_health_bar_blit_y, health_bar_width, 25)
        Settings.boss_health_transition_bar = pygame.Rect(Settings.boss_health_bar.right, Settings.boss_health_bar_blit_y, Settings.boss_health_transition_width, 25)

    @staticmethod
    def initialize_health_image():
        Settings.player_health_list.clear()
        # player health
        for k in range(0, Settings.upgrades['Max health']['current'], 5):
            for i in range(5):
                player_health_image_path = os.path.join('assets/graphics/player_hp/hp_' + str(i) + '.png')
                Settings.player_health_list.append(pygame.transform.scale(
                    pygame.image.load(player_health_image_path),
                    (Settings.player_health_image_size, Settings.player_health_image_size)))
        # boss health

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def draw_interface(screen):
        # Player health image
        for i in range(len(Settings.player_health_list)):
            if ((i)/5).is_integer():
                Settings.player_health_image_index += 1
            screen.blit(Settings.player_health_list[i],
                        ((Settings.player_health_image_index - 1) *
                         Settings.player_health_image_size, Settings.win_height - Settings.player_health_image_size))
        if Settings.player_health_image_index >= len(Settings.player_health_list) / 5:
            Settings.player_health_image_index = 0

        if Settings.boss_is_spawn:
        # Boss name
            screen.blit(Settings.boss_name_surface, ((Settings.win_width / 2) - Settings.font_size / 2, 0))
            """Reference: Clear Code. "Creating a health bar in pygame [Dark Souls style]." Youtube,
                                Oct. 2, 2020 [Video file]. Available: https://www.youtube.com/watch?v=pUEZbUAMZYA&ab_channel=ClearCode. [Accessed: Apr. 13, 2022]"""
            # Boss health bar
            pygame.draw.rect(screen, (255, 0, 0), Settings.boss_health_bar)
            pygame.draw.rect(screen, Settings.boss_health_transition_color, Settings.boss_health_transition_bar)
            pygame.draw.rect(screen, (255, 255, 255), (Settings.boss_health_bar_blit_x, Settings.boss_health_bar_blit_y, Settings.boss_health_bar_length, 25), 4)
        # Stage and difficulty
        screen.blit(Settings.stage_info_surface, (0, 0))
        # time
        screen.blit(Settings.time_passed_surface, (0, Settings.font_size * 1))
        # Point
        screen.blit(Settings.point_surface, (0, Settings.font_size * 2))
        # skill box
        if Settings.player.barrier_is_cd or not Settings.player.barrier_is_brought:
            screen.blit(Settings.ui_barrier_cd, (600,550))
        else:
            screen.blit(Settings.ui_barrier_box, (600,550))
        if Settings.player.dash_charge_value <= 0 or not Settings.player.dash_is_brought:
            screen.blit(Settings.ui_dash_cd, (650,550))
        else:
            screen.blit(Settings.ui_dash_box, (650,550))
        if Settings.player.grenade_charge_value <= 0 or not Settings.player.grenade_is_brought:
            screen.blit(Settings.ui_grenade_cd, (700,550))
        else:
            screen.blit(Settings.ui_grenade_box, (700,550))
        if Settings.player.laser_is_cd or not Settings.player.laser_is_brought:
            screen.blit(Settings.ui_laser_cd, (750,550))
        else:
            screen.blit(Settings.ui_laser_box, (750,550))
        screen.blit(Settings.ui_barrier_image, (600, 550))
        screen.blit(Settings.ui_dash_image, (650, 550))
        screen.blit(Settings.ui_grenade_image, (700, 550))
        screen.blit(Settings.ui_laser_image, (750, 550))
        screen.blit(Settings.ui_barrier_text_surf, (600, 550))
        screen.blit(Settings.ui_dash_text_surf, (650, 550))
        screen.blit(Settings.ui_grenade_text_surf, (700, 550))
        screen.blit(Settings.ui_laser_text_surf, (750, 550))

    @staticmethod
    def initialize_enemy_data():
        Settings.typeA_size = 6
        Settings.typeB_size = 7
        Settings.typeC_size = 7
        Settings.typeD_size = 1
        Settings.typeE_size = 16
        Settings.typeF_size = 12
        Settings.typeG_size = 6
        Settings.typeH_size = 8
        Settings.typeI_size = 8
        Settings.typeJ_size = 7
        Settings.typeK_size = 1
        Settings.typeL_size = 1
        Settings.typeM_size = 1
        Settings.counter_typeI = 6
        Settings.counter_typeJ = 6

    @staticmethod
    def import_music():
        # bgm and its volume
        Settings.bgm_mainmenu = pygame.mixer.Sound('assets/sounds/bgm/bgm_mainmenu.wav')
        Settings.bgm_gameover = pygame.mixer.Sound('assets/sounds/bgm/bgm_gameover.wav')
        Settings.bgm_mission_complete = pygame.mixer.Sound('assets/sounds/bgm/bgm_mission_complete.wav')
        Settings.bgm_s1 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s1.wav')
        Settings.bgm_s2 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s2.wav')
        Settings.bgm_s3 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s3.wav')
        Settings.bgm_s4 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s4.wav')
        Settings.bgm_s5 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s5.wav')
        Settings.bgm_s6 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s6.wav')
        Settings.bgm_s7 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s7.wav')
        Settings.bgm_s8 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s8.wav')
        Settings.bgm_s9 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s9.wav')
        Settings.bgm_s10 = pygame.mixer.Sound('assets/sounds/bgm/bgm_s10.wav')
        Settings.bgm_shop = pygame.mixer.Sound('assets/sounds/bgm/bgm_shop.wav')

        bgm_mixer = Settings.actual_main_volume * Settings.actual_bgm_volume
        Settings.bgm_mainmenu.set_volume(bgm_mixer)
        Settings.bgm_gameover.set_volume(bgm_mixer)
        Settings.bgm_mission_complete.set_volume(bgm_mixer)
        Settings.bgm_s1.set_volume(bgm_mixer)
        Settings.bgm_s2.set_volume(bgm_mixer)
        Settings.bgm_s3.set_volume(bgm_mixer)
        Settings.bgm_s4.set_volume(bgm_mixer)
        Settings.bgm_s5.set_volume(bgm_mixer)
        Settings.bgm_s6.set_volume(bgm_mixer)
        Settings.bgm_s7.set_volume(bgm_mixer)
        Settings.bgm_s8.set_volume(bgm_mixer)
        Settings.bgm_s9.set_volume(bgm_mixer)
        Settings.bgm_s10.set_volume(bgm_mixer)
        Settings.bgm_shop.set_volume(bgm_mixer)

        # sound effect and its volume
        effect_mixer = Settings.actual_main_volume * Settings.actual_effect_volume
        Settings.sound_boss_appear = pygame.mixer.Sound('assets/sounds/effect/boss_appear.wav')
        Settings.sound_boss_dead = pygame.mixer.Sound('assets/sounds/effect/boss_dead.wav')
        Settings.sound_button_clicked = pygame.mixer.Sound('assets/sounds/effect/button_clicked.wav')
        Settings.sound_enemy_appear = pygame.mixer.Sound('assets/sounds/effect/enemy_appear.wav')
        Settings.sound_enemy_defeated = pygame.mixer.Sound('assets/sounds/effect/enemy_defeated.wav')
        Settings.sound_enemy_group_appear = pygame.mixer.Sound('assets/sounds/effect/enemy_group_appear.wav')
        Settings.sound_enemy_shoot1 = pygame.mixer.Sound('assets/sounds/effect/enemy_shoot1.wav')
        Settings.sound_enemy_shoot2 = pygame.mixer.Sound('assets/sounds/effect/enemy_shoot2.wav')
        Settings.sound_player_boat = pygame.mixer.Sound('assets/sounds/effect/player_boat.wav')
        Settings.sound_player_dead = pygame.mixer.Sound('assets/sounds/effect/player_dead.wav')
        Settings.sound_player_shoot = pygame.mixer.Sound('assets/sounds/effect/player_shoot.wav')
        Settings.sound_shop_buy_item = pygame.mixer.Sound('assets/sounds/effect/shop_buy_item.wav')
        Settings.sound_target_hit = pygame.mixer.Sound('assets/sounds/effect/target_hit.wav')
        Settings.sound_player_barrier_on = pygame.mixer.Sound('assets/sounds/effect/player_barrier_on.wav')
        Settings.sound_player_barrier_broken = pygame.mixer.Sound('assets/sounds/effect/player_barrier_broken.wav')
        Settings.sound_player_dash = pygame.mixer.Sound('assets/sounds/effect/player_dash.wav')
        Settings.sound_player_grenade = pygame.mixer.Sound('assets/sounds/effect/player_grenade.wav')
        Settings.sound_player_throw_grenade = pygame.mixer.Sound('assets/sounds/effect/player_throw_grenade.wav')
        Settings.sound_player_laser = pygame.mixer.Sound('assets/sounds/effect/player_laser.wav')
        Settings.sound_coin_collcet = pygame.mixer.Sound('assets/sounds/effect/coin_collect.wav')
        Settings.sound_coin_drop = pygame.mixer.Sound('assets/sounds/effect/coin_drop.wav')

        Settings.sound_boss_appear.set_volume(effect_mixer)
        Settings.sound_boss_dead.set_volume(effect_mixer)
        Settings.sound_button_clicked.set_volume(effect_mixer)
        Settings.sound_enemy_appear.set_volume(effect_mixer)
        Settings.sound_enemy_defeated.set_volume(effect_mixer)
        Settings.sound_enemy_group_appear.set_volume(effect_mixer)
        Settings.sound_enemy_shoot1.set_volume(effect_mixer)
        Settings.sound_enemy_shoot2.set_volume(effect_mixer)
        Settings.sound_player_boat.set_volume(effect_mixer)
        Settings.sound_player_dead.set_volume(effect_mixer)
        Settings.sound_player_shoot.set_volume(effect_mixer)
        Settings.sound_shop_buy_item.set_volume(effect_mixer)
        Settings.sound_target_hit.set_volume(effect_mixer)
        Settings.sound_player_barrier_on.set_volume(effect_mixer)
        Settings.sound_player_barrier_broken.set_volume(effect_mixer)
        Settings.sound_player_dash.set_volume(effect_mixer)
        Settings.sound_player_grenade.set_volume(effect_mixer)
        Settings.sound_player_throw_grenade.set_volume(effect_mixer)
        Settings.sound_player_laser.set_volume(effect_mixer)
        Settings.sound_coin_collcet.set_volume(effect_mixer)
        Settings.sound_coin_drop.set_volume(effect_mixer)

    @staticmethod
    def sound_volume_update():
        Settings.actual_main_volume = Settings.main_volume_current * Settings.music_volume_ratio
        Settings.actual_bgm_volume = Settings.bgm_volume_current * Settings.music_volume_ratio
        Settings.actual_effect_volume = Settings.effect_volume_current * Settings.music_volume_ratio
        Settings.upgrades['Sound']['main volume'] = Settings.main_volume_current
        Settings.upgrades['Sound']['bgm volume'] = Settings.bgm_volume_current
        Settings.upgrades['Sound']['effect volume'] = Settings.effect_volume_current
        Settings.upgrades['Sound']['actual main volume'] = round(Settings.actual_main_volume,5)
        Settings.upgrades['Sound']['actual bgm volume'] = round(Settings.actual_bgm_volume,5)
        Settings.upgrades['Sound']['actual effect volume'] = round(Settings.actual_effect_volume,5)

        # bgm
        Settings.bgm_mainmenu.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_gameover.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_mission_complete.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s1.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s2.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s3.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s4.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s5.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s6.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s7.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s8.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s9.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_s10.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)
        Settings.bgm_shop.set_volume(Settings.actual_main_volume * Settings.actual_bgm_volume)

        #effect
        Settings.sound_boss_appear.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_boss_dead.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_button_clicked.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_enemy_appear.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_enemy_defeated.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_enemy_group_appear.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_enemy_shoot1.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_enemy_shoot2.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_boat.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_dead.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_shoot.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_shop_buy_item.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_target_hit.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_barrier_on.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_barrier_broken.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_dash.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_grenade.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_throw_grenade.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_player_laser.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_coin_collcet.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)
        Settings.sound_coin_drop.set_volume(Settings.actual_main_volume * Settings.actual_effect_volume)

    @staticmethod
    def check_volume_event():
        if pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False







