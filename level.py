import pygame, time, screen

from player import Player
from boss import *
from enemy import *
from settings import Settings as st
from projectiles import FiringData, BulletData
class Level(object):
    def __init__(self,surface):
        # initiate the screen
        self.display_surface = surface
        self.difficulty = 0
        self.level_start_time = st.time()
        # initialize bgm
        self.bgm = None
        # initiate boss
        self.boss = None
        # checking the game status
        self.game_status = True
        self.is_win = False
        self.give_up = False
        self.boss_is_spawn = False
        # phase data
        self.phase = 1
        self.last_phase_time = st.time()
        self.phase_change_time = st.phase_change_time
        self.phase_changed = False
        self.boss_last_phase_time = st.time
        self.difficulty = st.difficulty
        self.level_spawn_delay = 0
        self.boss_win_point = 0
        # game pause
        self.gameplay_pause_image = pygame.image.load(os.path.join('assets/images/background/Bg_credit.png'))
        self.gameplay_pause_image = pygame.transform.scale(self.gameplay_pause_image, (600, 600))
        self.text_0 = screen.Text((400, 200), 'Game paused!', 50, (0, 0, 0))
        self.text_1 = screen.Text((400, self.text_0.rect.bottom + 20), 'Main volume', 20, (0, 0, 0))
        self.main_volume = screen.Volume_control((400, self.text_1.rect.bottom + 20), st.music_volume_bar_length, 20)
        self.text_2 = screen.Text((400, self.main_volume.rect.bottom + 20), 'Background music volume', 20, (0, 0, 0))
        self.bgm_volume = screen.Volume_control((400, self.text_2.rect.bottom + 20), st.music_volume_bar_length, 20)
        self.text_3 = screen.Text((400, self.bgm_volume.rect.bottom + 20), 'Sound effect volume', 20, (0, 0, 0))
        self.effect_volume = screen.Volume_control((400, self.text_3.rect.bottom + 20), st.music_volume_bar_length, 20)
        self.button_back = screen.Button_text('Back to game', (250, self.effect_volume.rect.bottom + 100), 150, 30)
        self.button_give_up = screen.Button_text('Give up', (550, self.effect_volume.rect.bottom + 100), 150, 30)
        st.initialize_health_image()
        st.set_point(0)
        st.time_stage_begin = st.time()
        st.set_time_clock()
        st.stage_info_setup()
        st.current_game_surface = self.display_surface
        st.initialize_enemy_data()
        st.initialize_player_skill()
        st.initialize_skill_box()

        # initiate the sprite groups
        self.player_group = pygame.sprite.Group()
        self.player_bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_projectile_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        st.set_sprite_groups(self.player_group, self.player_bullet_group, self.enemy_group, self.enemy_projectile_group, self.coin_group)
        self.enemy_typeB_group = pygame.sprite.Group()
        self.enemy_typeD_group = pygame.sprite.Group()
        self.enemy_typeE_group = pygame.sprite.Group()
        self.enemy_typeF_group = pygame.sprite.Group()
        self.enemy_typeG_group = pygame.sprite.Group()
        self.enemy_typeH_group = pygame.sprite.Group()
        self.enemy_typeH_shooting_group = pygame.sprite.Group()
        self.enemy_typeI_group = pygame.sprite.Group()
        self.enemy_typeJ_shooting1_group = pygame.sprite.Group()
        self.enemy_typeJ_shooting2_group = pygame.sprite.Group()
        self.enemy_typeK_group = pygame.sprite.Group()
        self.enemy_typeL_group = pygame.sprite.Group()
        self.enemy_typeM_group = pygame.sprite.Group()

        # TypeB
        self.typeB_timer = st.time()
        self.typeB1_bd = None
        self.typeB1_fd = None
        self.typeB2_bd = None
        self.typeB2_fd = None
        # TypeD
        self.typeD_timer = st.time()
        self.typeD_bd = None
        self.typeD_fd = None
        # TypeE
        self.typeE_timer = st.time()
        self.typeE1_bd = None
        self.typeE1_fd = None
        self.typeE2_bd = None
        self.typeE2_fd = None
        # TypeF
        self.typeF_timer = st.time()
        self.typeF1_bd = None
        self.typeF1_fd = None
        self.typeF2_bd = None
        self.typeF2_fd = None
        # TypeH
        self.typeH_timer = st.time()
        self.typeH1_bd = None
        self.typeH1_fd = None
        self.typeH2_bd = None
        self.typeH2_fd = None
        # TypeI
        self.typeI_timer = st.time()
        self.typeI1_bd = None
        self.typeI1_fd = None
        self.typeI2_bd = None
        self.typeI2_fd = None
        # TypeJ
        self.typeJ_timer = st.time()
        self.typeJ1_bd = None
        self.typeJ1_fd = None
        self.typeJ2_bd = None
        self.typeJ2_fd = None
        # TypeL
        self.typeL_timer = st.time()
        self.typeL_bd = None
        self.typeL_fd = None
        # TypeM
        self.typeM_timer = st.time()
        self.typeM_bd = None
        self.typeM_fd = None

        # Boss_TypeG
        self.boss_typeG_angle = 230
        self.boss_typeG_counter = 1

        # Boss_TypeH
        self.boss_typeH_angle = 240
        self.boss_typeH_counter = 1

        # Boss_TypeI
        self.boss_typeI_angle = 270
        self.boss_typeI_counter = 1

        # enemy spawn
        self.spawn_typeD_1 = 1
        self.spawn_typeD_2 = 2
        self.spawn_typeD_3 = 3

        # player's bullet counter
        self.bullet_count = 0

        # enemy's bullet counter
        self.counter_typeI = st.counter_typeI
        self.counter_typeJ = st.counter_typeJ
        self.counter_typeL = st.counter_typeL
        self.counter_typeM = st.counter_typeM

    # update the sprites
    def spirte_update(self):
        # update the sprites
        self.player_bullet_group.update()
        self.enemy_projectile_group.update()
        self.player_group.update()
        self.enemy_group.update()
        self.coin_group.update()

    # draw the sprites on the screen
    def sprite_draw(self, screen):
        self.enemy_projectile_group.draw(screen)
        self.player_bullet_group.draw(screen)
        self.enemy_group.draw(screen)
        self.player_group.draw(screen)
    # check collision of enemy
    def check_collision_enemy(self):
        for enemy in self.enemy_group:
            enemy_gets_hit_by_player = pygame.sprite.spritecollide(enemy, self.player_bullet_group, True
                                                         , pygame.sprite.collide_mask)
            grenade_offset_x = st.player_grenade_pos[0] - st.player_width - enemy.rect.left
            grenade_offset_y = st.player_grenade_pos[1] - 300 - enemy.rect.top
            laser_offset_x = st.player.rect.left - enemy.rect.left
            laser_offset_y = -(st.win_height - st.player.y) - enemy.rect.top
            try:
                if st.player.grenade_exploding:
                    if enemy.mask.overlap(st.player_grenade_mask, (grenade_offset_x, grenade_offset_y)):
                        if st.time() - st.player_grenade_hit_time > 2:
                            enemy.get_hit(st.player.grenade_damage_value)
                            st.player_grenade_hit_time = st.time()
            except:
                pass
            try:
                if st.player.laser_shoot:
                    if enemy.mask.overlap(st.player_laser_mask, (laser_offset_x, laser_offset_y)):
                        if not enemy.hit_by_laser:
                            enemy.get_hit(st.player.laser_damage)
                            enemy.hit_by_laser = True
            except:
                pass
            if enemy_gets_hit_by_player:
                enemy.get_hit(st.player.bullet_damage)
    # check collision of player
    def check_collision_player(self):
        for player in self.player_group:
            player_gets_hit_projectile = pygame.sprite.spritecollide(player, self.enemy_projectile_group,
                                                                     False, pygame.sprite.collide_mask)
            player_gets_hit_enemy = pygame.sprite.spritecollide(player, self.enemy_group, False
                                                                , pygame.sprite.collide_mask)
            player_collide_coin = pygame.sprite.spritecollide(player, self.coin_group, True)
            if player_gets_hit_projectile:
                projectile_sprite = pygame.sprite.spritecollideany(player, self.enemy_projectile_group)
                if projectile_sprite != None:
                    player.get_hit(projectile_sprite.damage)
                    projectile_sprite.kill()
            elif player_gets_hit_enemy:
                enemy_sprite = pygame.sprite.spritecollideany(player, self.enemy_group)
                if enemy_sprite != None:
                    player.get_hit(enemy_sprite.damage)
            elif player_collide_coin:
                st.change_point(st.coin_point)
                st.sound_coin_collcet.play()
    def gameover(self):
        self.player_group.empty()
        self.player_bullet_group.empty()
        self.enemy_group.empty()
        self.enemy_projectile_group.empty()
        self.game_status = False
    def check_win(self):
        st.update_time_passed()
        if self.boss_is_spawn:
            st.update_boss_health_data()
            if not self.boss.alive:
                self.is_win = True
                self.gameover()
                self.bgm.stop()
                st.sound_player_boat.stop()
        if not st.player.alive:
            self.is_win = False
            self.gameover()
            self.bgm.stop()
            st.sound_player_boat.stop()
    def pause_screen(self):
        click = st.check_event()
        self.display_surface.screen.blit(self.gameplay_pause_image, (100, 0))
        self.text_0.draw(self.display_surface.screen)
        self.text_1.draw(self.display_surface.screen)
        self.text_2.draw(self.display_surface.screen)
        self.text_3.draw(self.display_surface.screen)
        self.main_volume.draw(self.display_surface.screen)
        self.bgm_volume.draw(self.display_surface.screen)
        self.effect_volume.draw(self.display_surface.screen)
        self.main_volume.set_current_volume(st.main_volume_current)
        self.bgm_volume.set_current_volume(st.bgm_volume_current)
        self.effect_volume.set_current_volume(st.effect_volume_current)
        self.button_back.draw(self.display_surface.screen)
        self.button_give_up.draw(self.display_surface.screen)
        if self.main_volume.rect.collidepoint(st.get_mouse_pos()):
            if click:
                self.main_volume.is_pressed()
        if self.main_volume.pressed:
            self.main_volume.pressed = st.check_volume_event()
            st.main_volume = self.main_volume.update()
            st.main_volume_current = self.main_volume.change_volume(st.get_mouse_pos())
            st.sound_volume_update()
        if self.bgm_volume.rect.collidepoint(st.get_mouse_pos()):
            if click:
                self.bgm_volume.is_pressed()
        if self.bgm_volume.pressed:
            self.bgm_volume.pressed = st.check_volume_event()
            st.bgm_volume = self.bgm_volume.update()
            st.bgm_volume_current = self.bgm_volume.change_volume(st.get_mouse_pos())
            st.sound_volume_update()
        if self.effect_volume.rect.collidepoint(st.get_mouse_pos()):
            if click:
                self.effect_volume.is_pressed()
        if self.effect_volume.pressed:
            self.effect_volume.pressed = st.check_volume_event()
            st.effect_volume = self.effect_volume.update()
            st.effect_volume_current = self.effect_volume.change_volume(st.get_mouse_pos())
            st.sound_volume_update()
        if self.button_back.top_rect.collidepoint(st.get_mouse_pos()):
            if click:
                st.gameplay_is_paused = False
        if self.button_give_up.top_rect.collidepoint(st.get_mouse_pos()):
            if click:
                self.is_win = False
                self.gameover()
                self.bgm.stop()
                st.sound_player_boat.stop()
                st.gameplay_is_paused = False
        pygame.display.update()
        st.clock_update()
    # ---------------------generate player bullets-------------------------
    def player_shoot(self):
        for player in self.player_group:
            player.shoot()
    # ---------------------generate enemies of that movement type---------------------------
    def enemy_movement_TypeA(self, Minion1, Minion2):
        if time.time() - st.time_TypeA > 2 and st.typeA_size > 0:
            for index in range(2):
                if index % 2 == 0:
                    Minion1(60, 45/2, 'TypeA1')
                if index % 2 == 1:
                    Minion2(740, 45 / 2, 'TypeA2')
                st.typeA_size -= 1
            st.time_TypeA = time.time()
    def enemy_movement_TypeB(self):
        if time.time() - st.time_TypeB > 2 and st.typeB_size > 0:
            for index in range(7):
                if index % 2 == 0:
                    enemy_b1 = Goblin(-60, 45 / 2 + index * 92.5, 'TypeB1')
                    self.typeB1_bd = BulletData(enemy_b1, speed=3, damage=2, image_width=enemy_b1.projectile_width, image_height=enemy_b1.projectile_height,
                                        image_name=enemy_b1.projectile_name)
                    self.typeB1_fd = FiringData(angle=0)
                    enemy_b1.insert_data([self.typeB1_bd, self.typeB1_fd])
                    self.enemy_typeB_group.add(enemy_b1)
                if index % 2 == 1:
                    enemy_b2 = Slime(st.win_width + 60, 45 / 2 + index * 92.5, 'TypeB2')
                    self.typeB2_bd = BulletData(enemy_b2, speed=3, damage=2, image_width=enemy_b2.projectile_width, image_height=enemy_b2.projectile_height,
                                        image_name=enemy_b2.projectile_name)
                    self.typeB2_fd = FiringData(angle=180)
                    enemy_b2.insert_data([self.typeB2_bd, self.typeB2_fd])
                    self.enemy_typeB_group.add(enemy_b2)
                st.typeB_size -= 1
            st.time_TypeB = time.time()
    def enemy_movement_TypeC(self):
        if time.time() - st.time_TypeC > 0.5 and st.typeC_size > 0:
            Bird(st.win_width - (st.typeC_size - 1) * 120 -40, -45, 'TypeC')
            st.typeC_size -= 1
            st.time_TypeC = st.time()
    def enemy_movement_TypeD(self, Minion, spawn):
        if time.time() - st.time_TypeD > 2:
            list = []
            if spawn == self.spawn_typeD_1:
                list.append(Minion(random.uniform(60 / 2, st.win_width - 60 / 2),
                             random.uniform(45 / 2, st.win_height / 2), 'TypeD'))
                self.spawn_typeD_1 = 0
            elif spawn == self.spawn_typeD_2:
                for i in range(self.spawn_typeD_2):
                    list.append(Minion(random.uniform(60 / 2, st.win_width - 60 / 2),
                                 random.uniform(45 / 2, st.win_height / 2), 'TypeD'))
                self.spawn_typeD_2 = 0
            elif spawn == self.spawn_typeD_3:
                for i in range(self.spawn_typeD_3):
                    list.append(Minion(random.uniform(60 / 2, st.win_width - 60 / 2),
                                 random.uniform(45 / 2, st.win_height / 2), 'TypeD'))
                self.spawn_typeD_3 = 0
            for enemy_d in list:
                self.typeD_bd = BulletData(enemy_d, speed=4, damage=2, image_width=enemy_d.projectile_width,
                                           image_height=enemy_d.projectile_height,
                                           image_name=enemy_d.projectile_name)
                self.typeD_fd = FiringData(angle=270)
                enemy_d.insert_data([self.typeD_bd, self.typeD_fd])
                self.enemy_typeD_group.add(enemy_d)
    def enemy_movement_TypeE(self, Minion1, Minion2):
        if time.time() - st.time_TypeE > 0.8 and st.typeE_size != 0:
            enemy_e1 = Minion1(st.win_width + 60 / 2, 30, 'TypeE1')
            enemy_e2 = Minion2(-60 / 2, 5 * 30, 'TypeE2')
            self.typeE1_bd = BulletData(enemy_e1, speed=4, damage=3, image_width=enemy_e1.projectile_width, image_height=enemy_e1.projectile_height,
                                        image_name=enemy_e1.projectile_name)
            self.typeE1_fd = FiringData(angle=270)
            self.typeE2_bd = BulletData(enemy_e2, speed=4, damage=3, image_width=enemy_e2.projectile_width, image_height=enemy_e2.projectile_height,
                                        image_name=enemy_e2.projectile_name)
            self.typeE2_fd = FiringData(angle=270)
            enemy_e1.insert_data([self.typeE1_bd, self.typeE1_fd])
            enemy_e2.insert_data([self.typeE2_bd, self.typeE2_fd])
            self.enemy_typeE_group.add(enemy_e1)
            self.enemy_typeE_group.add(enemy_e2)
            st.typeE_size -= 2
            st.time_TypeE = time.time()
    def enemy_movement_TypeF(self, Minion1, Minion2):
        if time.time() - st.time_TypeF > 0.9 and st.typeF_size != 0:
            enemy_f1 = Minion1(60 / 2, st.win_height + 45, 'TypeF1')
            enemy_f2 = Minion2(st.win_width - 60 / 2, -45, 'TypeF2')
            self.typeF1_bd = BulletData(enemy_f1, speed=3, damage=3, image_width=enemy_f1.projectile_width, image_height=enemy_f1.projectile_height,
                                        image_name=enemy_f1.projectile_name)
            self.typeF1_fd = FiringData(angle=0)
            self.typeF2_bd = BulletData(enemy_f2, speed=4, damage=3, image_width=enemy_f2.projectile_width, image_height=enemy_f2.projectile_height,
                                        image_name=enemy_f2.projectile_name)
            self.typeF2_fd = FiringData(angle=180)
            enemy_f1.insert_data([self.typeF1_bd, self.typeF1_fd])
            enemy_f2.insert_data([self.typeF2_bd, self.typeF2_fd])
            self.enemy_typeF_group.add(enemy_f1)
            self.enemy_typeF_group.add(enemy_f2)
            st.typeF_size -= 2
            st.time_TypeF = time.time()
    def enemy_movement_TypeG(self):
        """if len(self.enemy_typeG_group.sprites()) == 0 and st.typeG_size != 0:
            enemy_g = Mouse(-60 / 2, st.typeG_size * 100 - 50, 'TypeG')
            self.enemy_typeG_group.add(enemy_g)
            st.typeG_size -= 1"""
        if st.time() - st.time_TypeG > 1 and st.typeG_size > 0:
            enemy_g = Mouse(-60 / 2, st.typeG_size * 100 - 50, 'TypeG')
            self.enemy_typeG_group.add(enemy_g)
            st.typeG_size -= 1
            st.time_TypeG = st.time()
    def enemy_movement_TypeH(self):
        if time.time() - st.time_TypeH > 1 and st.typeH_size != 0:
            for index in range(4):
                enemy_h1 = Squirrel(100 + index * 200, -30, 'TypeH1')
                enemy_h2 = Turtle(100 + index * 200, -50, 'TypeH2')
                self.typeH1_bd = BulletData(enemy_h1, speed=3, damage=3, image_width=enemy_h1.projectile_width, image_height=enemy_h1.projectile_height,
                                            image_name=enemy_h1.projectile_name)
                self.typeH1_fd = FiringData(angle=270)
                enemy_h1.insert_data([self.typeH1_bd, self.typeH1_fd])
                self.enemy_typeH_shooting_group.add(enemy_h1)
                self.enemy_typeH_group.add(enemy_h1)
                self.enemy_typeH_group.add(enemy_h2)
                st.typeH_size -= 2
                st.time_TypeH = time.time()
        """try:
            if self.enemy_typeH_group.sprites()[0] != None:
                if self.enemy_typeH_group.sprites()[0].x > 100 + 0 * 180:
                    self.enemy_typeH_group.sprites()[0].velocityx = 0
            if self.enemy_typeH_group.sprites()[1] != None:
                if self.enemy_typeH_group.sprites()[1].x > 100 + 0 * 180:
                    self.enemy_typeH_group.sprites()[1].velocityx = 0
            if self.enemy_typeH_group.sprites()[2] != None:
                if self.enemy_typeH_group.sprites()[2].x > 100 + 1 * 180:
                    self.enemy_typeH_group.sprites()[2].velocityx = 0
            if self.enemy_typeH_group.sprites()[3] != None:
                if self.enemy_typeH_group.sprites()[3].x > 100 + 1 * 180:
                    self.enemy_typeH_group.sprites()[3].velocityx = 0
            if self.enemy_typeH_group.sprites()[4] != None:
                if self.enemy_typeH_group.sprites()[4].x > 100 + 2 * 180:
                    self.enemy_typeH_group.sprites()[4].velocityx = 0
            if self.enemy_typeH_group.sprites()[5] != None:
                if self.enemy_typeH_group.sprites()[5].x > 100 + 2 * 180:
                    self.enemy_typeH_group.sprites()[5].velocityx = 0
            if self.enemy_typeH_group.sprites()[6] != None:
                if self.enemy_typeH_group.sprites()[6].x > 100 + 3 * 180:
                    self.enemy_typeH_group.sprites()[6].velocityx = 0
            if self.enemy_typeH_group.sprites()[7] != None:
                if self.enemy_typeH_group.sprites()[7].x > 100 + 3 * 180:
                    self.enemy_typeH_group.sprites()[7].velocityx = 0
        except:
            pass"""
    def enemy_movement_TypeI(self):
        if time.time() - st.time_TypeI > 2 and st.typeI_size != 0:
            if st.typeI_size == 8 and st.counter_typeI == 6:
                list = []
                list.append(EyeMonster(-50, -50, 'TypeI1'))
                list.append(EyeMonster(850, -50, 'TypeI1'))
                list.append(EyeMonster(-50, 650, 'TypeI1'))
                list.append(EyeMonster(850, 650, 'TypeI1'))
                for enemy_i1 in list:
                    self.typeI1_bd = BulletData(enemy_i1, speed=3, damage=3, image_width=enemy_i1.projectile_width, image_height=enemy_i1.projectile_height,
                                        image_name=enemy_i1.projectile_name)
                    self.typeI1_fd = FiringData(angle=st.angle_to_point((enemy_i1.x, enemy_i1.y), (st.win_width/2, st.win_height/2)))
                    enemy_i1.insert_data([self.typeI1_bd, self.typeI1_fd])
                    self.enemy_typeI_group.add(enemy_i1)
                st.typeI_size -= 4
            elif st.typeI_size == 4 and st.counter_typeI == 3:
                list = []
                list.append(Squirrel(400, -50, 'TypeI2'))
                list.append(Squirrel(-50, 300, 'TypeI2'))
                list.append(Squirrel(850, 300, 'TypeI2'))
                list.append(Squirrel(400, 650, 'TypeI2'))
                for enemy_i2 in list:
                    self.typeI2_bd = BulletData(enemy_i2, speed=5, damage=3, image_width=enemy_i2.projectile_width, image_height=enemy_i2.projectile_height,
                                        image_name=enemy_i2.projectile_name)
                    self.typeI2_fd = FiringData(angle=st.angle_to_point((enemy_i2.x, enemy_i2.y), (st.win_width/2, st.win_height/2)))
                    enemy_i2.insert_data([self.typeI2_bd, self.typeI2_fd])
                    self.enemy_typeI_group.add(enemy_i2)
                st.typeI_size -= 4
    def enemy_movement_TypeJ(self):
        if time.time() - st.time_TypeJ > 2 and st.typeJ_size != 0:
            for index in range(7):
                if index % 2 == 0:
                    enemy_j1 = Goat(100 + index * 100, 150, 'TypeJ')
                    self.typeJ1_bd = BulletData(enemy_j1, speed=3, damage=3, image_width=enemy_j1.projectile_width, image_height=enemy_j1.projectile_height,
                                        image_name=enemy_j1.projectile_name)
                    self.typeJ1_fd = FiringData(angle=270)
                    enemy_j1.insert_data([self.typeJ1_bd, self.typeJ1_fd])
                    self.enemy_typeJ_shooting1_group.add(enemy_j1)
                if index % 2 == 1:
                    enemy_j2 = Goblin(100 + index * 100, 75, 'TypeJ')
                    self.typeJ2_bd = BulletData(enemy_j2, speed=3, damage=3, image_width=enemy_j2.projectile_width, image_height=enemy_j2.projectile_height,
                                        image_name=enemy_j2.projectile_name)
                    self.typeJ2_fd = FiringData(angle=270)
                    enemy_j2.insert_data([self.typeJ2_bd, self.typeJ2_fd])
                    self.enemy_typeJ_shooting2_group.add(enemy_j2)
                st.typeJ_size -= 1
    def enemy_movement_TypeK(self, Minion):
        if time.time() - st.time_TypeK > 2 and st.typeK_size != 0:
            enemy_k = Minion(st.win_width / 2, 50, 'TypeK')
            self.enemy_typeK_group.add(enemy_k)
            st.time_TypeK = time.time()
            st.typeK_size -= 1
    def enemy_movement_TypeL(self, Minion):
        if time.time() - self.typeL_timer > 1 and st.typeL_size != 0:
            enemy_l = Minion(200, -40, 'TypeL')
            self.typeL_bd = BulletData(enemy_l, speed=6, damage=2, image_width=enemy_l.projectile_width, image_height=enemy_l.projectile_height,
                                        image_name=enemy_l.projectile_name)
            self.typeL_fd = FiringData(aim=True)
            enemy_l.insert_data([self.typeL_bd, self.typeL_fd])
            self.enemy_typeL_group.add(enemy_l)
            st.time_TypeL = time.time()
            st.typeL_size -= 1
    def enemy_movement_TypeM(self, Minion):
        if st.time() - self.typeM_timer > 1 and st.typeM_size != 0:
            enemy_m = Minion(st.win_width - 200, -40, 'TypeM')
            self.typeM_bd = BulletData(enemy_m, speed=6, damage=2, image_width=enemy_m.projectile_width, image_height=enemy_m.projectile_height,
                                        image_name=enemy_m.projectile_name)
            self.typeM_fd = FiringData(aim=True)
            enemy_m.insert_data([self.typeM_bd, self.typeM_fd])
            self.enemy_typeM_group.add(enemy_m)
            st.time_TypeM = time.time()
            st.typeM_size -= 1
    # -----------------genereate enemy minion projectiles----------------
    def enemy_shooting_projectile_TypeB(self):
        if st.time() - self.typeB_timer > st.enemy_shoot_frequency:
            for enemy in self.enemy_typeB_group:
                if enemy.alive == True:
                    self.typeB_timer = enemy.shoot(self.typeB_timer, enemy.bulletData, enemy.firingData)
    def enemy_shooting_projectile_TypeD(self):
        if st.time() - self.typeD_timer > st.enemy_shoot_frequency:
            for enemy in self.enemy_typeD_group:
                if enemy.alive == True:
                    self.typeD_timer = enemy.shoot(self.typeB_timer, enemy.bulletData, enemy.firingData)
    def enemy_shooting_projectile_TypeE(self):
        if st.time() - self.typeE_timer > st.enemy_shoot_frequency:
            for enemy in self.enemy_typeE_group:
                if enemy.alive == True:
                    self.typeE_timer = enemy.shoot(self.typeE_timer, enemy.bulletData, enemy.firingData)
    def enemy_shooting_projectile_TypeF(self):
        if st.time() - self.typeF_timer > st.enemy_shoot_frequency:
            for enemy in self.enemy_typeF_group:
                if enemy.alive == True:
                    self.typeF_timer = enemy.shoot(self.typeF_timer, enemy.bulletData, enemy.firingData)
    def enemy_shooting_projectile_TypeH(self):
        if st.time() - self.typeH_timer > st.enemy_shoot_frequency:
            for enemy in self.enemy_typeH_shooting_group:
                if enemy.alive == True:
                    self.typeH_timer = enemy.shoot(self.typeH_timer, enemy.bulletData, enemy.firingData)
    def enemy_shooting_projectile_TypeI(self):
        if st.time() - self.typeI_timer > st.enemy_shoot_frequency - 0.7:
            for enemy in self.enemy_typeI_group:
                if enemy.alive == True:
                    self.typeI_timer = enemy.shoot(self.typeI_timer, enemy.bulletData, enemy.firingData)
            st.counter_typeI -= 1
    def enemy_shooting_projectile_TypeJ(self):
        if st.time() - self.typeJ_timer > st.enemy_shoot_frequency - 1.1 and st.counter_typeJ != 0:
            if st.counter_typeJ % 2 == 0:
                for enemy in self.enemy_typeJ_shooting1_group:
                    if enemy.alive == True:
                        self.typeJ_timer = enemy.shoot(self.typeJ_timer, enemy.bulletData, enemy.firingData)
            else:
                for enemy in self.enemy_typeJ_shooting2_group:
                    if enemy.alive == True:
                        self.typeJ_timer = enemy.shoot(self.typeJ_timer, enemy.bulletData, enemy.firingData)
            st.counter_typeJ -= 1
    def enemy_shooting_projectile_TypeL(self):
        for enemy in self.enemy_typeL_group:
            if st.time() - enemy.timer > st.enemy_shoot_frequency - 0.4 and enemy.counter != 0:
                if enemy.alive:
                    enemy.timer = enemy.shoot(enemy.timer, enemy.bulletData, enemy.firingData)
                    enemy.counter -= 1
            if enemy.counter == 0:
                if enemy.alive:
                    enemy.typeL_return = True
    def enemy_shooting_projectile_TypeM(self):
        for enemy in self.enemy_typeM_group:
            if st.time() - enemy.timer > st.enemy_shoot_frequency - 0.4 and enemy.counter != 0:
                if enemy.alive:
                    enemy.timer = enemy.shoot(enemy.timer, enemy.bulletData, enemy.firingData)
                    enemy.counter -= 1
            if enemy.counter == 0:
                if enemy.alive:
                    enemy.typeM_return = True
    def boss_shooting_projectile(self):
        if self.boss_is_spawn:
            if self.boss.alive:
                if self.boss.type == 'Boss_TypeB':
                    if time.time() - self.Boss_TypeB_timer > 1:
                        self.Boss_TypeB_timer = self.boss.shoot(self.Boss_TypeB_timer, self.Boss_TypeB_bd,
                                                                self.Boss_TypeB_fd)
                        self.boss.shoot_sound.play()
                if self.boss.type == 'Boss_TypeC':
                    if time.time() - self.Boss_TypeC_timer > 1:
                        self.Boss_TypeC_timer = self.boss.shoot(self.Boss_TypeC_timer, self.Boss_TypeC_bd,
                                                                self.Boss_TypeC_fd)
                        self.boss.shoot_sound.play()
                elif self.boss.type == 'Boss_TypeD':
                    if time.time() - self.Boss_TypeD_timer > 1:
                        self.Boss_TypeD_timer = self.boss.shoot(self.Boss_TypeD_timer, self.Boss_TypeD_bd,
                                                                self.Boss_TypeD_fd)
                        self.boss.shoot_sound.play()
                elif self.boss.type == 'Boss_TypeG':
                    if time.time() - self.Boss_TypeG_timer > 0.1:
                        self.Boss_TypeG_timer = self.boss.shoot(self.Boss_TypeG_timer, self.Boss_TypeG_bd,
                                                                self.Boss_TypeG_fd)
                        if self.boss_typeG_counter <= 8:
                            self.boss_typeG_angle += 10
                        else:
                            self.boss_typeG_angle -= 10
                        if self.boss_typeG_counter != 16:
                            self.boss_typeG_counter += 1
                        else:
                            self.boss_typeG_counter = 1
                        self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
                        self.boss.shoot_sound.play()
                elif self.boss.type == 'Boss_TypeH':
                    if time.time() - self.Boss_TypeH_timer > 0.3:
                        self.Boss_TypeH_timer = self.boss.shoot(self.Boss_TypeH_timer, self.Boss_TypeH_bd,
                                                                self.Boss_TypeH_fd)
                        if self.boss_typeH_counter < 3:
                            self.boss_typeH_angle += 30
                            self.boss_typeH_counter += 1
                        else:
                            self.boss_typeH_counter = 1
                            self.boss_typeH_angle = 240
                        self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
                        self.boss.shoot_sound.play()
                elif self.boss.type == 'Boss_TypeI':
                    if time.time() - self.Boss_TypeI_timer > 0.3:
                        self.Boss_TypeI_timer = self.boss.shoot(self.Boss_TypeI_timer, self.Boss_TypeI_bd,
                                                                self.Boss_TypeI_fd)
                        if self.boss_typeI_counter == 1:
                            self.boss_typeI_angle -= 30
                            self.boss_typeI_counter += 1
                        elif self.boss_typeI_counter == 2:
                            self.boss_typeI_angle += 60
                            self.boss_typeI_counter += 1
                        else:
                            self.boss_typeI_counter = 1
                            self.boss_typeI_angle = 270
                        self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
                        self.boss.shoot_sound.play()
                elif self.boss.type == 'Boss_TypeJ':
                    if self.boss.x > 700 or self.boss.x < 100:
                        if time.time() - self.Boss_TypeJ_timer > 1:
                            self.Boss_TypeJ_timer = self.boss.shoot(self.Boss_TypeJ_timer, self.Boss_TypeJ_bd,
                                                                    self.Boss_TypeJ_fd)
    #----------------------------------------------------------------------------------
    def run(self):
        """Boss shooting data
        # Boss_TypeB
        self.Boss_TypeB_timer = st.time()
        self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                        image_width=self.boss.projectile_width, image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
        # boss_typeC
        self.Boss_TypeC_timer = st.time()
        self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                        image_width=self.boss.projectile_width, image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
        # Boss_TypeD
        self.Boss_TypeD_timer = st.time()
        self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                        image_width=self.boss.projectile_width, image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
        self.Boss_TypeG_timer = st.time()
        self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                        image_width=self.boss.projectile_width,
                                        image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
        self.Boss_TypeH_timer = st.time()
        self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                        image_width=self.boss.projectile_width,
                                        image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
        self.Boss_TypeI_timer = st.time()
        self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                        image_width=self.boss.projectile_width,
                                        image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
        self.Boss_TypeJ_timer = st.time()
        self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                        image_width=self.boss.projectile_width,
                                        image_height=self.boss.projectile_height, image_name=self.boss.projectile_name)
        self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)

"""
    def change_phase(self):
        self.phase_changed = False
        if st.time() - self.last_phase_time > self.phase_change_time:
            self.phase_changed = True
            if self.phase < self.num_phases:
                self.phase += 1
            self.last_phase_time = st.time()
    def reset_spawn_typeD(self):
        self.spawn_typeD_1 = 1
        self.spawn_typeD_2 = 2
        self.spawn_typeD_3 = 3
    def all_type_shooting(self):
        self.enemy_shooting_projectile_TypeB()
        self.enemy_shooting_projectile_TypeD()
        self.enemy_shooting_projectile_TypeE()
        self.enemy_shooting_projectile_TypeF()
        self.enemy_shooting_projectile_TypeH()
        self.enemy_shooting_projectile_TypeI()
        self.enemy_shooting_projectile_TypeJ()
        self.enemy_shooting_projectile_TypeL()
        self.enemy_shooting_projectile_TypeM()
    def reset_boss_type_shooting_data(self):
        self.boss_typeG_angle = 230
        self.boss_typeG_counter = 1
        self.boss_typeH_angle = 240
        self.boss_typeH_counter = 1
        self.boss_typeI_angle = 270
        self.boss_typeI_counter = 1
    def reset_all_data(self):
        self.reset_spawn_typeD()
        self.reset_boss_type_shooting_data()
        self.boss_is_spawn = False
        st.boss_is_spawn = False
        st.initialize_enemy_data()
class Level_1(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s1
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                                      , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                                      , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                                      , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            self.boss = Boss_1(st.win_width / 2, 100, 'Boss_TypeC')
            self.boss.set_boss_point(self.boss.win_point)
            self.boss_spawn_time = time.time()
            st.sound_boss_appear.play()
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, damage=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(multi=9, angle=270)
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
    def phase2(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
    def phase3(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(EyeMonster, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(EyeMonster, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(EyeMonster, 1)
    def phase4(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeL(Goblin)
    def phase5(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Slime, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Slime, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Slime, 1)
    def phase6(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeM(Goblin)
    def phase7(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goat, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goat, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goat, 1)
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeL(Goblin)
    def phase9(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 1:
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 2:
            self.enemy_movement_TypeM(Slime)
    def phase10(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
    def phase11(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase12(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                pass
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 6:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 6:
                    self.boss.type = 'Boss_TypeB'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                     and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeA'
                else:
                    self.boss.type = 'Boss_TypeC'
class Level_2(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s2
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            self.boss = Boss_2(st.win_width / 2, 100, 'Boss_TypeC')
            self.boss_spawn_time = time.time()
            self.boss.set_boss_point(self.boss.win_point)
            st.sound_boss_appear.play()
            # boss_typeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        #setup
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeL(Goblin)
    def phase2(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeM(Goblin)
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 1:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 2:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goat, 3)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goat, 3)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goat, 3)
    def phase5(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Bird, Mouse)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeD(Goblin, 1)
    def phase7(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goat, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goat, 1)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goat, 1)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
    def phase9(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
    def phase10(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Squirrel, 1)
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase11(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeA'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeA'
                else:
                    self.boss.type = 'Boss_TypeB'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeB'
class Level_3(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s3
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            self.boss = Boss_3(st.win_width / 2, 100, 'Boss_TypeC')
            self.boss_spawn_time = time.time()
            self.boss.set_boss_point(self.boss.win_point)
            st.sound_boss_appear.play()
            # boss_typeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(Goblin)
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeM(Goblin)
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 1:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 2:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goat, 1)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goat, 1)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goat, 1)
            self.enemy_movement_TypeM(Slime)
    def phase5(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 1)
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)

        elif self.difficulty == 2:
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase9(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeH()
    def phase10(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
    def phase11(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeD'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 6:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 6:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 6:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 6:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 4 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 5 / 6:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeD'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 7:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 7 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 7:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 7 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 7:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 7 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 7:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 4 / 7 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 5 / 7:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 5 / 7 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 6 / 7:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeI'
class Level_4(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s4
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            self.boss = Boss_4(st.win_width / 2, 100, 'Boss_TypeB')
            self.boss_spawn_time = time.time()
            self.boss.set_boss_point(self.boss.win_point)
            st.sound_boss_appear.play()
            # boss_typeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeH()
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeD(Goblin, 3)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeK(Bird)
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeD(Goblin, 3)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 1:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeD(EyeMonster, 3)
    def phase9(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase10(self):
        if self.phase_changed:
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeK(Mouse)
    def phase11(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeA'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeA'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeI'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeA'
                else:
                    self.boss.type = 'Boss_TypeC'
class Level_5(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s5
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            if self.difficulty == 0:
                self.boss = Boss_5(st.win_width / 2, 100, 'Boss_TypeB')
            elif self.difficulty == 1:
                self.boss = Boss_5(st.win_width / 2, 100, 'Boss_TypeB')
            elif self.difficulty == 2:
                self.boss = Boss_5(st.win_width / 2, 100, 'Boss_TypeI')
            self.boss_spawn_time = time.time()
            st.sound_boss_appear.play()
            self.boss.set_boss_point(self.boss.win_point)
            # boss_typeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                st.player.check_if_boat(150, 650)
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeD(Goblin, 2)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeD(Goblin, 2)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeD(Goblin, 2)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeK(Starfish)
        elif self.difficulty == 1:
            self.enemy_movement_TypeK(Starfish)
        elif self.difficulty == 2:
            self.enemy_movement_TypeK(Starfish)
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeK(Starfish)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeK(Starfish)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeK(Starfish)
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeK(Turtle)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 1:
            self.enemy_movement_TypeK(Turtle)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 2:
            self.enemy_movement_TypeK(Turtle)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Shark, Bird)
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Shark, Bird)
            self.enemy_movement_TypeK(Bird)
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Shark, Bird)
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeH()
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase9(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            self.enemy_movement_TypeA(Shark, Bird)
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
    def phase10(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeH()
    def phase11(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Fish, Shark)
            self.enemy_movement_TypeK(Starfish)
    def phase12(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeI'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeH'
class Level_6(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s6
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            if self.difficulty == 0:
                self.boss = Boss_6(st.win_width / 2, 100, 'Boss_TypeC')
            elif self.difficulty == 1:
                self.boss = Boss_6(st.win_width / 2, 100, 'Boss_TypeA')
            elif self.difficulty == 2:
                self.boss = Boss_6(st.win_width / 2, 100, 'Boss_TypeA')
            self.boss_spawn_time = time.time()
            self.boss.set_boss_point(self.boss.win_point)
            st.sound_boss_appear.play()
            # boss_typeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeK(Mouse)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 1:
            self.enemy_movement_TypeK(Mouse)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeK(Mouse)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeD(Goblin, 1)
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeK(Mouse)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeB()
        elif self.difficulty == 2:
            self.enemy_movement_TypeI()
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeK(Mouse)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeB()
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(EyeMonster, 3)
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Bird, Mouse)
            self.enemy_movement_TypeK(Mouse)
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(EyeMonster, 3)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeI()
    def phase9(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
    def phase10(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeH()
    def phase11(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Mouse, Bird)
            self.enemy_movement_TypeH()
    def phase12(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeE'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeE'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeE'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeH'
class Level_7(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s7
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            if self.difficulty == 0:
                self.boss = Boss_7(st.win_width / 2, 100, 'Boss_TypeB')
            elif self.difficulty == 1:
                self.boss = Boss_7(st.win_width / 2, 100, 'Boss_TypeD')
            elif self.difficulty == 2:
                self.boss = Boss_7(st.win_width / 2, 100, 'Boss_TypeD')
            self.boss_spawn_time = time.time()
            self.boss.set_boss_point(self.boss.win_point)
            st.sound_boss_appear.play()
            # boss_typeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                st.player.check_if_boat(500, 800)
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeI()
        elif self.difficulty == 1:
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeI()
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(EyeMonster, 3)
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeI()
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeI()
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Turtle)
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Turtle)
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(Slime, 3)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(Slime, 3)
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Bird, Starfish)
            self.enemy_movement_TypeD(Goat, 3)
        elif self.difficulty == 1:
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeI()
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 2:
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase9(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            self.enemy_movement_TypeA(Bird, Starfish)
            self.enemy_movement_TypeD(Goat, 3)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeA(Bird, Starfish)
            self.enemy_movement_TypeD(Goat, 3)
    def phase10(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(EyeMonster, 3)
            self.enemy_movement_TypeH()
    def phase11(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeH()
    def phase12(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeD'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeB'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeD'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeG'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeD'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeH'
                else:
                    self.boss.type = 'Boss_TypeI'
class Level_8(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s8
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            if self.difficulty == 0:
                self.boss = Boss_8(st.win_width / 2, 100, 'Boss_TypeC')
            elif self.difficulty == 1:
                self.boss = Boss_8(st.win_width / 2, 100, 'Boss_TypeG')
            elif self.difficulty == 2:
                self.boss = Boss_8(st.win_width / 2, 100, 'Boss_TypeG')
            self.boss_spawn_time = time.time()
            self.boss.set_boss_point(self.boss.win_point)
            st.sound_boss_appear.play()
            # Boss_TypeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                st.player.check_if_boat(500, 800)
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(Squirrel, 3)
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(Squirrel, 3)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeD(Squirrel, 3)
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeG()
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Shark, Starfish)
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeG()
        elif self.difficulty == 1:
            self.enemy_movement_TypeG()
        elif self.difficulty == 2:
            self.enemy_movement_TypeG()
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Shark, Starfish)
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeG()
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Shark, Starfish)
            self.enemy_movement_TypeD(EyeMonster, 1)
            self.enemy_movement_TypeG()
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeC()
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeK(Turtle)
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeK(Turtle)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Slime, 3)
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
    def phase9(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeK(Turtle)
            self.enemy_movement_TypeL(Goblin)
            self.enemy_movement_TypeM(Goblin)
    def phase10(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeH()
    def phase11(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeC()
    def phase12(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeC'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeH'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeA'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeG'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeH'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeG'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeH'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeE'
                else:
                    self.boss.type = 'Boss_TypeG'
class Level_9(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s9
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            if self.difficulty == 0:
                self.boss = Boss_9(st.win_width / 2, 100, 'Boss_TypeJ')
            elif self.difficulty == 1:
                self.boss = Boss_9(st.win_width / 2, 100, 'Boss_TypeA')
            elif self.difficulty == 2:
                self.boss = Boss_9(st.win_width / 2, 100, 'Boss_TypeA')
            self.boss_spawn_time = time.time()
            st.sound_boss_appear.play()
            self.boss.set_boss_point(self.boss.win_point)
            # Boss_TypeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                st.player.check_if_boat(200, 600)
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Fish, Shark)
            self.enemy_movement_TypeG()
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Fish, Shark)
            self.enemy_movement_TypeG()
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Fish, Shark)
            self.enemy_movement_TypeG()
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeC()
        elif self.difficulty == 1:
            self.enemy_movement_TypeC()
        elif self.difficulty == 2:
            self.enemy_movement_TypeC()
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeI()
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Starfish, Shark)
            self.enemy_movement_TypeC()
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Starfish, Shark)
            self.enemy_movement_TypeC()
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeI()
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeC()
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeC()
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeG()
        elif self.difficulty == 1:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeG()
            self.enemy_movement_TypeI()
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 1:
            self.enemy_movement_TypeI()
        elif self.difficulty == 2:
            self.enemy_movement_TypeI()
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeC()
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
        elif self.difficulty == 1:
            self.enemy_movement_TypeG()
        elif self.difficulty == 2:
            self.enemy_movement_TypeG()
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Shark)
        elif self.difficulty == 2:
            self.enemy_movement_TypeE(Goblin, EyeMonster)
    def phase9(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            self.enemy_movement_TypeC()
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 2:
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Shark)
    def phase10(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeC()
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Goat)
    def phase11(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeF(Goblin, Slime)
    def phase12(self):
        if self.difficulty == 2:
            pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeJ'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeG'
                else:
                    self.boss.type = 'Boss_TypeD'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeD'
                else:
                    self.boss.type = 'Boss_TypeG'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 5:
                    self.boss.type = 'Boss_TypeA'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 5:
                    self.boss.type = 'Boss_TypeB'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 5:
                    self.boss.type = 'Boss_TypeD'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 5 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 5:
                    self.boss.type = 'Boss_TypeG'
                else:
                    self.boss.type = 'Boss_TypeE'
class Level_10(Level):
    def __init__(self, surface):
        super().__init__(surface)
        # setup bgm
        self.bgm = st.bgm_s10
        # ----------phase data------------
        if self.difficulty == 0:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 1:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10]
            self.num_phases = len(self.phase_method_list)
        elif self.difficulty == 2:
            self.phase_method_list = [self.phase1, self.phase2, self.phase3, self.phase4, self.phase5
                , self.phase6, self.phase7, self.phase8, self.phase9, self.phase10, self.phase11, self.phase12
                                      , self.phase13]
            self.num_phases = len(self.phase_method_list)
        self.boss_spawn_delay = (self.num_phases // 2) * st.phase_change_time
    def boss_spawn(self):
        if st.time() - self.level_start_time > self.boss_spawn_delay and not self.boss_is_spawn:
            self.boss_is_spawn = True
            st.boss_is_spawn = self.boss_is_spawn
            if self.difficulty == 0:
                self.boss = Boss_10(st.win_width / 2, 100, 'Boss_TypeG')
            elif self.difficulty == 1:
                self.boss = Boss_10(st.win_width / 2, 100, 'Boss_TypeG')
            elif self.difficulty == 2:
                self.boss = Boss_10(st.win_width / 2, 100, 'Boss_TypeG')
            self.boss_spawn_time = time.time()
            st.sound_boss_appear.play()
            self.boss.set_boss_point(self.boss.win_point)
            # Boss_TypeB
            self.Boss_TypeB_timer = st.time()
            self.Boss_TypeB_bd = BulletData(self.boss, speed=2, duration=6,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeB_fd = FiringData(aim=True, multi=36)
            # boss_typeC
            self.Boss_TypeC_timer = st.time()
            self.Boss_TypeC_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeC_fd = FiringData(aim=True, multi=9)
            # Boss_TypeD
            self.Boss_TypeD_timer = st.time()
            self.Boss_TypeD_bd = BulletData(self.boss, speed=2, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeD_fd = FiringData(aim=True, multi=13)
            self.Boss_TypeG_timer = st.time()
            self.Boss_TypeG_bd = BulletData(self.boss, speed=2, damage=5, duration=5.2,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeG_fd = FiringData(angle=self.boss_typeG_angle)
            self.Boss_TypeH_timer = st.time()
            self.Boss_TypeH_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeH_fd = FiringData(multi=3, angle=self.boss_typeH_angle)
            self.Boss_TypeI_timer = st.time()
            self.Boss_TypeI_bd = BulletData(self.boss, speed=2, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeI_fd = FiringData(multi=3, angle=self.boss_typeI_angle)
            self.Boss_TypeJ_timer = st.time()
            self.Boss_TypeJ_bd = BulletData(self.boss, speed=3, damage=5,
                                            image_width=self.boss.projectile_width,
                                            image_height=self.boss.projectile_height,
                                            image_name=self.boss.projectile_name)
            self.Boss_TypeJ_fd = FiringData(aim=True, multi=7)
    def run(self):
        # setup data
        p1 = Player(st.player_skin, st.get_player_bullet_image())
        self.reset_all_data()
        self.bgm.play(loops=-1)
        # game loop
        while self.game_status:
            if not st.gameplay_is_paused:
                click = st.check_event()
                # player shooting bullets
                self.player_shoot()
                st.player.check_if_boat(200, 600)
                # ----------------calling enemies------------------------------
                # update the phase
                self.boss_spawn()
                self.change_phase()
                self.phase_method_list[self.phase - 1]()
                self.boss_phase()
                # ---------------Enemy shooting projectiles--------------------
                self.boss_shooting_projectile()
                self.all_type_shooting()
                # ------------------updating and checking----------------------
                # draw the screen
                self.display_surface.draw()
                # update the sprites
                self.spirte_update()
                # draw the sprites
                self.sprite_draw(self.display_surface.screen)
                # check collision: delete the enemy if bullet collide with enemy
                self.check_collision_enemy()
                # check collision: delete the player if projectile or enemy collide with player
                self.check_collision_player()
                # check if the game is win or loss
                self.check_win()
                # pygame update
                st.draw_interface(self.display_surface.screen)
                pygame.display.update()
                st.clock_update()
            else:
                self.pause_screen()
        return self.is_win
    def phase1(self):
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Slime, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Slime, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Slime, 1)
    def phase2(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeD(EyeMonster, 1)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeD(EyeMonster, 1)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Shark, Fish)
            self.enemy_movement_TypeD(EyeMonster, 1)
    def phase3(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
    def phase4(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Goblin, 3)
            self.enemy_movement_TypeH()
    def phase5(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeA(Starfish, Shark)
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 1:
            self.enemy_movement_TypeA(Starfish, Shark)
            self.enemy_movement_TypeK(Bird)
        elif self.difficulty == 2:
            self.enemy_movement_TypeA(Starfish, Shark)
            self.enemy_movement_TypeK(Bird)
    def phase6(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 1:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
        elif self.difficulty == 2:
            self.enemy_movement_TypeB()
            self.enemy_movement_TypeL(Goat)
            self.enemy_movement_TypeM(Goat)
    def phase7(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Shark)
        elif self.difficulty == 1:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Shark)
        elif self.difficulty == 2:
            self.enemy_movement_TypeH()
            self.enemy_movement_TypeI()
            self.enemy_movement_TypeK(Shark)
    def phase8(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeC()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 1:
            self.enemy_movement_TypeC()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
        elif self.difficulty == 2:
            self.enemy_movement_TypeC()
            self.enemy_movement_TypeL(EyeMonster)
            self.enemy_movement_TypeM(EyeMonster)
    def phase9(self):
        if self.phase_changed:
            st.initialize_enemy_data()
            self.reset_spawn_typeD()
        if self.difficulty == 0:
            self.enemy_movement_TypeD(Squirrel, 1)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
            self.enemy_movement_TypeJ()
        elif self.difficulty == 1:
            self.enemy_movement_TypeD(Squirrel, 3)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
            self.enemy_movement_TypeJ()
        elif self.difficulty == 2:
            self.enemy_movement_TypeD(Squirrel, 3)
            self.enemy_movement_TypeL(Slime)
            self.enemy_movement_TypeM(Slime)
            self.enemy_movement_TypeJ()
    def phase10(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 0:
            pass
        elif self.difficulty == 1:
            pass
        elif self.difficulty == 2:
            self.enemy_movement_TypeE(Goblin, EyeMonster)
            self.enemy_movement_TypeF(Goblin, Slime)
    def phase11(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Fish, Starfish)
            self.enemy_movement_TypeE(EyeMonster, Goat)
            self.enemy_movement_TypeF(Slime, Squirrel)
    def phase12(self):
        if self.phase_changed:
            self.reset_spawn_typeD()
            st.initialize_enemy_data()
        if self.difficulty == 2:
            self.enemy_movement_TypeA(Shark, Bird)
            self.enemy_movement_TypeE(Goblin, EyeMonster)
            self.enemy_movement_TypeF(Goat, Slime)
            self.enemy_movement_TypeL(Squirrel)
            self.enemy_movement_TypeM(Squirrel)
    def phase13(self):
        pass
    def boss_phase(self):
        if self.boss_is_spawn:
            if self.difficulty == 0:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 4:
                    self.boss.type = 'Boss_TypeG'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 4:
                    self.boss.type = 'Boss_TypeD'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 4 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 / 4:
                    self.boss.type = 'Boss_TypeC'
                else:
                    self.boss.type = 'Boss_TypeC'
            elif self.difficulty == 1:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 3:
                    self.boss.type = 'Boss_TypeG'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 3 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 / 3:
                    self.boss.type = 'Boss_TypeG'
                else:
                    self.boss.type = 'Boss_TypeH'
            elif self.difficulty == 2:
                if (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 1 / 6:
                    self.boss.type = 'Boss_TypeG'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 1 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 2 /6:
                    self.boss.type = 'Boss_TypeI'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 2 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 3 /6:
                    self.boss.type = 'Boss_TypeG'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 3 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 4 / 6:
                    self.boss.type = 'Boss_TypeH'
                elif (time.time() - self.boss_spawn_time) % st.boss_cycle > st.boss_cycle * 4 / 6 \
                        and (time.time() - self.boss_spawn_time) % st.boss_cycle < st.boss_cycle * 5 / 6:
                    self.boss.type = 'Boss_TypeE'
                else:
                    self.boss.type = 'Boss_TypeD'
