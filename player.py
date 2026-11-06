import pygame, os

from settings import Settings as st
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, image, bullet_image):
        pygame.sprite.Sprite.__init__(self)

        # player assets
        self.image = pygame.image.load(os.path.join('assets/images/item/skin',image))
        self.image = pygame.transform.scale(self.image, (st.player_width, st.player_height))
        self.image_original = self.image
        self.mask = pygame.mask.from_surface(self.image)

        self.image_invisible = pygame.image.load(os.path.join('assets/images/item/skin/player_invisible.png'))
        self.image_invisible = pygame.transform.scale(self.image_invisible, (st.player_width, st.player_height))

        self.image_boat = pygame.image.load(os.path.join('assets/images/item/skin/boat_original.png'))
        self.image_boat = pygame.transform.scale(self.image_boat, (st.player_width+10, st.player_height+10))

        # player initial position
        self.x = st.player_initial_pos[0]
        self.y = st.player_initial_pos[1]

        self.rect = self.image.get_rect(center=(self.x,self.y))

        # player attribute
        self.player_width = st.player_width
        self.player_height = st.player_height
        self.player_speed = st.player_speed
        self.hp = st.upgrades['Max health']['current']

        # player status
        self.alive = True
        self.invincible = False
        self.invincible_time = None
        self.invincible_duration = 1
        self.invincible_toggle = None
        self.is_boat = False
        self.boat_sound_played = False

        # player bullet
        self.bullet_speed = st.upgrades['Bullet velocity']['current']
        self.bullet_damage = st.upgrades['Attack damage']['current']
        self.bullet_image = bullet_image
        self.shooting_frequency = st.upgrades['Attack frequency']['current']
        self.shooting_frequency_timer = 0
        self.shooting_density = st.upgrades['Attack frequency']['current'] * 0.4
        self.shooting_density_timer = 0
        self.bullet_counter = 0
        self.bullet_number = st.upgrades['Bullet number']['current']
        self.bullet_multi = st.upgrades['Multi shot']['current']
        self.bullet_shot_angle_list = st.multi_shot_angles(self.bullet_multi, 270, 10)
        self.shooting = False

        # ------------player skill data-----------------
        # barrier
        self.barrier_image = pygame.image.load(os.path.join('assets/images/effect/barrier.png'))
        self.barrier_image = pygame.transform.scale(self.barrier_image, (st.player_width+20, st.player_height+20))
        self.barrier_invincible_value = st.upgrades['Barrier']['invincible']
        self.barrier_cooldown_value = st.upgrades['Barrier']['cooldown']
        self.barrier_invincible_time = 0
        self.barrier_cooldown_time = 0
        self.barrier_is_cd = False
        self.barrier_on = False
        self.barrier_is_brought = st.upgrades['Barrier']['is brought']
        # dash
        self.dash_charge_value = st.upgrades['Dash']['charge']
        self.dash_cooldown_value = st.upgrades['Dash']['cooldown']
        self.dash_dash_time = 0
        self.dash_cooldown_time = 0
        self.dashing = False
        self.dash_start = False
        self.dash_monitor = True
        self.dashing_duration = 0.1
        self.dash_is_brought = st.upgrades['Dash']['is brought']
        # grenade
        self.grenade_explosion_list = st.import_grenade_animation_image()
        self.grenade_explosion_list_index = 0
        self.grenade_image = pygame.image.load(os.path.join('assets/images/effect/grenade.png'))
        self.grenade_image = pygame.transform.scale(self.grenade_image, (25, 25))
        self.grenade_image_angle = 0
        self.grenade_speed = 0
        self.grenade_spawn_pos = (0,0)
        self.grenade_y = 0
        self.grenade_flying = False
        self.grenade_diameter_value = st.upgrades['Grenade']['diameter']
        self.grenade_charge_value = st.upgrades['Grenade']['charge']
        self.grenade_charge_value_max = st.upgrades['Grenade']['charge']
        self.grenade_cooldown_value = st.upgrades['Grenade']['cooldown']
        self.grenade_damage_value = st.upgrades['Grenade']['damage'] * self.bullet_damage
        self.grenade_cooldown_time = 0
        self.grenading_time = 0
        self.grenading = False
        self.grenade_start = False
        self.grenade_monitor = True
        self.grenade_animate = False
        self.grenade_exploding = False
        self.grenade_animate_time = 0
        self.grenading_interval = 0.5
        self.grenade_is_brought = st.upgrades['Grenade']['is brought']
        # laser
        self.laser_image = pygame.image.load(os.path.join('assets/images/effect/laser.png'))
        self.laser_image = pygame.transform.scale(self.laser_image, (self.player_width, 600))
        self.laser_cooldown_value = st.upgrades['Laser']['cooldown']
        self.laser_width = self.player_width
        self.laser_duration = 3
        self.laser_damage = 6 * self.bullet_damage
        self.laser_cooldown_time = 0
        self.laser_shoot_time = 0
        self.laser_shoot = False
        self.laser_is_cd = False
        self.laser_is_brought = st.upgrades['Laser']['is brought']
        #update data to settings for other usage
        st.insert_player_sprite(self)

        # Add to sprite group
        self.add(st.player_group)

    def move(self):
        keys = pygame.key.get_pressed()
        self.rect.center = (self.x, self.y)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < st.win_width:
            self.x += self.player_speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.y -= self.player_speed
        if keys[pygame.K_DOWN] and self.rect.bottom < st.win_height:
            self.y += self.player_speed

    def update(self):
        self.input()
        self.check_is_boat()
        self.check_invincible_active()
        self.move()
        self.check_health()
        st.update_player_health_image()

    def shoot(self):
        if not self.shooting:
            if st.time() - self.shooting_frequency_timer > self.shooting_frequency:
                self.shooting = True
                self.shooting_density_timer = st.time()
                self.bullet_counter += 1
                for arc_shot in range(self.bullet_multi):
                    Bullet(self.rect.centerx, self.rect.top, 15, 40, self.bullet_speed, self.bullet_damage,
                           self.bullet_image, self.bullet_shot_angle_list[arc_shot])
                st.sound_player_shoot.play()
        else:
            if self.bullet_counter < self.bullet_number:
                if st.time() - self.shooting_density_timer > self.shooting_density:
                    self.bullet_counter += 1
                    self.shooting_density_timer = st.time()
                    for arc_shot in range(self.bullet_multi):
                        Bullet(self.rect.centerx, self.rect.top, 15, 40, self.bullet_speed, self.bullet_damage,
                               self.bullet_image, self.bullet_shot_angle_list[arc_shot])
                    st.sound_player_shoot.play()
            else:
                self.bullet_counter = 0
                self.shooting = False
                self.shooting_frequency_timer = st.time()

    def get_hit(self, projectile_damage):
        if not self.barrier_on:
            if not self.invincible:
                self.invincible = True
                self.invincible_time = st.time()
                self.invincible_toggle = st.time()
                self.hp -= projectile_damage
        else:
            pass
    def check_health(self):
        if self.hp <= 0:
            self.alive = False
            st.sound_player_dead.play()
            self.kill()
    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    def check_invincible_active(self):
        if self.invincible:
            if st.time() - self.invincible_time < self.invincible_duration:
                if st.time() - self.invincible_toggle > 0.05:
                    self.invincible_toggle = st.time()
                    self.image = self.image_invisible
                    self.rect = self.image.get_rect(center=(self.x,self.y))
                else:
                    if self.is_boat:
                        st.current_game_surface.screen.blit(self.image_boat, (self.x - 20, self.y - 25))
                    self.image = self.image_original
                    self.rect = self.image.get_rect(center=(self.x,self.y))
            else:
                self.invincible = False
        else:
            if self.is_boat:
                st.current_game_surface.screen.blit(self.image_boat, (self.x - 20, self.y - 25))
            self.image = self.image_original
            self.rect = self.image.get_rect()
    def check_is_boat(self):
        if not self.is_boat:
            pass
        else:
            self.image = self.image_boat
            self.rect = self.image.get_rect()
    def check_if_boat(self, border_left, border_right):
        if self.x >= border_left and self.x <= border_right:
            self.is_boat = True
            if not self.boat_sound_played:
                self.boat_sound_played = True
                st.sound_player_boat.play(loops=-1)
        else:
            self.is_boat = False
            self.boat_sound_played = False
            st.sound_player_boat.stop()
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.barrier_is_brought:
            self.barrier()
        elif keys[pygame.K_w] and self.dash_is_brought:
            self.dash()
        elif keys[pygame.K_e] and self.grenade_is_brought:
            self.grenade()
        elif keys[pygame.K_r] and self.laser_is_brought:
            self.laser()
        self.skill_update()
    def barrier(self):
        if not self.barrier_is_cd:
            self.barrier_on = True
            self.barrier_is_cd = True
            self.barrier_cooldown_time = st.time()
            self.barrier_invincible_time = st.time()
    def dash(self):
        if self.dash_charge_value > 0:
            if not self.dashing:
                self.dashing = True
                self.dash_charge_value -= 1
                self.dash_dash_time = st.time()
                self.dash_start = True
    def grenade(self):
        if self.grenade_charge_value > 0:
            if not self.grenading:
                self.grenading = True
                self.grenade_charge_value -= 1
                self.grenading_time = st.time()
                self.grenade_start = True
    def laser(self):
        if not self.laser_is_cd:
            self.laser_is_cd = True
            self.laser_shoot = True
            self.laser_shoot_time = st.time()
    def skill_update(self):
        self.cast_barrier()
        self.cast_dash()
        self.cast_grenade()
        self.cast_laser()
        self.grenade_explosion()
    def cast_barrier(self):
        if self.barrier_on:
            if st.time() - self.barrier_invincible_time > self.barrier_invincible_value:
                self.barrier_on = False
                st.sound_player_barrier_broken.play()
            else:
                st.sound_player_barrier_on.play()
                st.current_game_surface.screen.blit(self.barrier_image, (self.rect.left - 10, self.rect.top - 10))
        else:
            if st.time() - self.barrier_cooldown_time > self.barrier_cooldown_value:
                self.barrier_is_cd = False
    def cast_dash(self):
        if self.dashing:
            self.player_speed = 20
            if st.time() - self.dash_dash_time > self.dashing_duration:
                self.dashing = False
                self.player_speed = 3
            st.sound_player_dash.play()
        else:
            if self.dash_monitor:
                if self.dash_start:
                    self.dash_cooldown_time = st.time()
                    self.dash_monitor = False
            if st.time() - self.dash_cooldown_time > self.dash_cooldown_value:
                if self.dash_charge_value < 2:
                    self.dash_charge_value += 1
                self.dash_cooldown_time = st.time()
    def cast_grenade(self):
        if self.grenading:
            if st.time() - self.grenading_time > self.grenading_interval:
                self.grenading = False
                self.grenade_animate = True
                self.grenade_flying = True
                self.grenade_speed = 8
                self.grenade_image_angle = 0
                self.grenade_spawn_pos = (self.rect.topleft)
                self.grenade_y = self.grenade_spawn_pos[1]
                self.grenade_animate_time = st.time()
                st.player_grenade_pos = (self.rect.topleft)
                st.sound_player_throw_grenade.play()

        else:
            if self.grenade_monitor:
                if self.grenade_start:
                    self.grenade_cooldown_time = st.time()
                    self.grenade_monitor = False
            if st.time() - self.grenade_cooldown_time > self.grenade_cooldown_value:
                if self.grenade_charge_value < self.grenade_charge_value_max:
                    self.grenade_charge_value += 1
                self.grenade_cooldown_time = st.time()
    def grenade_explosion(self):
        if self.grenade_animate:
            if self.grenade_flying:
                if not self.grenade_spawn_pos[1] - self.grenade_y > 300:
                    self.grenade_y -= self.grenade_speed
                    self.grenade_image_angle += 12
                    st.current_game_surface.screen.blit(pygame.transform.rotate
                                                        (self.grenade_image, self.grenade_image_angle), (self.grenade_spawn_pos[0] - 10, self.grenade_y - 10))
                else:
                    self.grenade_speed = 0
                    self.grenade_flying = False
                    self.grenade_exploding = True
                    st.sound_player_grenade.play()
            else:
                if st.time() - self.grenade_animate_time > 0.1:
                    st.current_game_surface.screen.blit(self.grenade_explosion_list
                                                        [self.grenade_explosion_list_index],
                                                        (st.player_grenade_pos[0] - self.player_width, st.player_grenade_pos[1] - 300))
                    st.player_grenade_mask = pygame.mask.from_surface(self.grenade_explosion_list
                                                                    [self.grenade_explosion_list_index])
                    self.grenade_animate_time = st.time()
                    self.grenade_explosion_list_index += 1
            if self.grenade_explosion_list_index >= 10:
                self.grenade_explosion_list_index = 0
                self.grenade_animate = False
                self.grenade_exploding = False
    def cast_laser(self):
        if self.laser_shoot:
            if st.time() - self.laser_shoot_time > self.laser_duration:
                self.laser_shoot = False
                self.laser_cooldown_time = st.time()
            st.current_game_surface.screen.blit(self.laser_image, (self.rect.left, -(st.win_height - self.y)))
            st.player_laser_mask = pygame.mask.from_surface(self.laser_image)
            st.sound_player_laser.play()
        else:
            if st.time() - self.laser_cooldown_time > self.laser_cooldown_value:
                self.laser_is_cd = False
                self.laser_cooldown_time = st.time()

