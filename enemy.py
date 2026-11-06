import pygame, os, math, random
from settings import Settings as st
from projectiles import Projectile

class Enemy(pygame.sprite.Sprite): #x, y, width, height, radial_growth, angle, damage, image
    def __init__(self,
                 x, y, move_speed, width, height, hp, image_name, type, projectile_width,
                 projectile_height, projectile_damage, projectile_name, is_boss = False):
        pygame.sprite.Sprite.__init__(self)
        ####### setups for enemy
        if is_boss:
            self.image_path = os.path.join('assets', 'images', 'enemy', 'boss', image_name)
            self.image = pygame.image.load(self.image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image_path = os.path.join('assets', 'images', 'enemy', 'minion', image_name)
            self.image = pygame.image.load(self.image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)
        # setup attribute of enemy
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.spawn = (x,y)
        self.velocityx = move_speed
        self.velocityy = move_speed
        self.original_velocityx = move_speed
        self.original_velocityy = move_speed
        self.type = type
        self.point = 0
        self.is_boss = is_boss
        self.spawn_time = st.time()
        self.shoot_sound = random.choice([st.sound_enemy_shoot1, st.sound_enemy_shoot2])
        self.hit_by_laser = False
        self.hit_by_laser_time = 0
        self.damage = 0
        self.timer = st.time()
        self.counter = 0
        if self.is_boss:
            self.hp = hp
            self.damage = projectile_damage
            st.boss_max_health = self.hp * st.boss_health_factor
            st.boss_health_bar_ratio = st.boss_max_health / st.boss_health_bar_length
            st.initialize_boss_data()
        else:
            self.hp = 0

        # locate the image rectangular block
        self.rect = self.image.get_rect()

        # type A1/A2 curve path attribute >>> for test
        self.rotation_centerA = (400,0)
        self.rotation_centerB = (400,680)
        self.radius = 340
        self.angleA1 = 180
        self.angleA2 = 90
        self.angleB1 = 360
        self.angleB2 = 90
        self.angleK = 53.1301
        self.angleBossF = 62

        # initialize hp, damage and point for certain enemy type and spawn special movement of enemy type
        if self.type == 'TypeA1' or self.type == 'TypeA2':
            self.point = 20
            self.damage = 2
            self.hp = 2
        elif self.type == 'TypeB1' or self.type == 'TypeB2':
            self.point = 30
            self.damage = 2
            self.hp = 2
        elif self.type == 'TypeC':
            self.point = 30
            self.damage = 3
            self.hp = 2
        elif self.type == "TypeD":
            self.velocityx = round(random.randrange(move_speed, -move_speed, abs(move_speed * 2)),6)
            self.velocityy = round(random.randrange(move_speed, -move_speed, abs(move_speed * 2)),6)
            self.point = 10
            self.damage = 2
            self.hp = 5
        elif self.type == 'TypeE1' or self.type == 'TypeE2':
            self.point = 40
            self.damage = 3
            self.hp = 3
        elif self.type == 'TypeF1' or self.type == 'TypeF2':
            self.point = 40
            self.hp = 3
            self.damage = 3
        elif self.type == 'TypeG':
            self.point = 40
            self.hp = 3
            self.damage = 3
        elif self.type == 'TypeH1':
            self.point = 30
            self.hp = 1
            self.damage = 3
        elif self.type == 'TypeH2':
            self.point = 10
            self.hp = 10
            self.damage = 1
        elif self.type == 'TypeI1':
            self.velocityx = move_speed * math.sin(math.radians(st.angle_to_point((self.spawn[0], self.spawn[1]), (st.win_width/2, st.win_height/2))))
            self.velocityy = move_speed * math.cos(math.radians(st.angle_to_point((self.spawn[0], self.spawn[1]), (st.win_width/2, st.win_height/2))))
            self.original_velocityx = self.velocityx
            self.original_velocityy = self.velocityy
            self.point = 20
            self.hp = 2
            self.damage = 3
        elif self.type == 'TypeI2':
            self.velocityx = move_speed * math.cos(math.radians(st.angle_to_point((self.spawn[0], self.spawn[1]), (st.win_width/2, st.win_height/2))))
            self.velocityy = move_speed * math.sin(math.radians(st.angle_to_point((self.spawn[0], self.spawn[1]), (st.win_width/2, st.win_height/2))))
            self.original_velocityx = self.velocityx
            self.original_velocityy = self.velocityy
            self.point = 20
            self.hp = 2
            self.damage = 3
        elif self.type == 'TypeJ':
            self.point = 20
            self.hp = 2
            self.damage = 3
        elif self.type == "TypeK":
            self.velocityx = move_speed * math.sin(math.radians(self.angleK))
            self.velocityy = move_speed * math.cos(math.radians(self.angleK))
            self.point = 30
            self.hp = 2
            self.damage = 2
            #self.image = pygame.transform.rotate(self.image,
            #            st.normalize_angle(math.degrees(math.hypot(self.velocityx, self.velocityy))+90))
        elif self.type == "TypeL":
            self.point = 10
            self.hp = 3
            self.damage = 2
            self.counter = 3
        elif self.type == "TypeM":
            self.point = 10
            self.hp = 3
            self.damage = 2
            self.counter = 3
        elif self.type == 'Boss_TypeA':
            self.point = 500

        if self.type == "Boss_TypeF":
            self.velocityx = self.original_velocityx * math.sin(math.radians(self.angleBossF))
            self.velocityx = self.original_velocityy * math.sin(math.radians(self.angleBossF))
            self.original_Boss_TypeF_velocityx = self.velocityx
            self.original_Boss_TypeF_velocityy = self.velocityy
        self.typeI_return = False
        self.typeL_return = False
        self.typeM_return = False

        # enemy status
        self.alive = True
        self.appearance = True
        self.mission_finished = False

        ###### setups for enemy's projectiles
        self.projectile_name = projectile_name
        self.projectile_width = projectile_width
        self.projectile_height = projectile_height
        self.projectile_damage = projectile_damage

        # Add to sprite group
        self.add(st.enemy_group)
        if self.is_boss:
            st.insert_boss_sprite(self)
            st.boss_max_health = self.hp * st.boss_health_factor
            st.boss_health_bar_ratio = st.boss_max_health / st.boss_health_bar_length
        # data
        self.bulletData = None
        self.FiringData = None

    def update(self):
        self.move()
        self.check_health()
        self.out_of_bounds()

    def check_health(self):
        if self.hp <= 0:
            if self.is_boss:
                st.sound_boss_dead.play()
            else:
                st.sound_enemy_defeated.play()
                if random.choice(st.coin_random_list):
                    Coin(self.x, self.y)
                    st.sound_coin_drop.play()
            st.change_point(self.point)
            self.alive = False
            self.kill()
        if self.mission_finished:
            if not self.is_boss:
                st.change_point(self.point)
            self.alive = False
            self.kill()
        if self.hit_by_laser:
            self.hit_by_laser_time = st.time()
            if st.time() - self.hit_by_laser_time > 4:
                self.hit_by_laser = False

    def out_of_bounds(self):
        if not self.is_boss:
            if self.x > st.win_width + 75 or \
                            self.x < -75 or \
                            self.y > st.win_height + 75 or self.y < -75:
                self.kill()
        else:
            if self.x > st.win_width + 100 or \
                            self.x < -100 or \
                            self.y > st.win_height + 100 or self.y < -100:
                self.kill()

    def insert_data(self,data):
        self.bulletData = data[0]
        self.firingData = data[1]

    def get_hit(self, bullet_damage):
        self.hp -= bullet_damage
        st.sound_target_hit.play()


    def move(self):
        if self.type == 'TypeA1':
            if self.angleA1 <= 270:
                self.x = self.rotation_centerA[0] + self.radius * math.cos(math.radians(self.angleA1))
                self.y = self.rotation_centerA[1] - self.radius * math.sin(math.radians(self.angleA1))
                self.angleA1 += 1
                if self.angleA1 > 270:
                    self.angleA2 = 90
            if self.angleA1 > 270:
                self.x = self.rotation_centerB[0] + self.radius * math.cos(math.radians(self.angleA2 % 360))
                self.y = self.rotation_centerB[1] - self.radius * math.sin(math.radians(self.angleA2 % 360))
                self.angleA2 -= 1
                if self.angleA2 < 0:
                    self.angleA1 = 180
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeA2':
            if self.angleB1 >= 270:
                self.x = self.rotation_centerA[0] + self.radius * math.cos(math.radians(self.angleB1))
                self.y = self.rotation_centerA[1] - self.radius * math.sin(math.radians(self.angleB1))
                self.angleB1 -= 1
                if self.angleB1 < 270:
                    self.angleB2 = 90
            if self.angleB1 < 270:
                self.x = self.rotation_centerB[0] + self.radius * math.cos(math.radians(self.angleB2))
                self.y = self.rotation_centerB[1] - self.radius * math.sin(math.radians(self.angleB2))
                self.angleB2 += 1
                if self.angleB2 > 180:
                    self.angleB1 = 360
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeB1':
            self.x -= self.velocityx
            if self.x > 50:
                self.velocityx = 0
            if st.time() - self.spawn_time > st.phase_change_time:
                self.velocityx = -self.original_velocityx
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeB2':
            self.x += self.velocityx
            if self.x < st.win_width - 50:
                self.velocityx = 0
            if st.time() - self.spawn_time > st.phase_change_time:
                self.velocityx = -self.original_velocityx
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeC':
            self.y -= self.velocityy
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeD':
            self.x += self.velocityx
            self.y -= self.velocityy
            if st.time() - self.spawn_time < st.phase_change_time:
                if self.x - self.rect.width / 2 < 0 or self.x + self.rect.width / 2 > st.win_width:
                    self.velocityx *= -1
                if self.y - self.rect.height / 2 < 0 or self.y + self.rect.height / 2 > st.win_height / 2:
                    self.velocityy *= -1
            else:
                pass
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeE1':
            self.x += self.velocityx
            if self.x <= -50:
                if not st.time() - self.spawn_time > st.phase_change_time:
                    self.x = st.win_width + 50 + self.width/2
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeE2':
            self.x -= self.velocityx
            if self.x >= st.win_width + 50:
                if not st.time() - self.spawn_time > st.phase_change_time:
                    self.x = -50
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeF1':
            self.y += self.velocityy
            if self.y <= -50 - self.height/2:
                if not st.time() - self.spawn_time > st.phase_change_time:
                    self.y = st.win_height + 50 + self.height/2
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeF2':
            self.y -= self.velocityy
            if self.y >= st.win_height + 50 + self.height/2:
                if not st.time() - self.spawn_time > st.phase_change_time:
                    self.y = -50 - self.height/2
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeG':
            self.x -= self.velocityx
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeH1':
            if self.y > 50:
                self.velocityy = 0
            if st.time() - self.spawn_time > st.phase_change_time:
                self.velocityy = -self.original_velocityy
            self.y -= self.velocityy
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeH2':
            if self.y > 125:
                self.velocityy = 0
            if st.time() - self.spawn_time > st.phase_change_time:
                self.velocityy = -self.original_velocityy
            self.y -= self.velocityy
            self.rect.center = (self.x, self.y)

        elif self.type == 'TypeI1':
            if self.velocityx >= 0 and self.velocityy >= 0:
                self.x -= self.velocityx
                self.y += self.velocityy
            elif self.velocityx >= 0 and self.velocityy <= 0:
                self.x += self.velocityx
                self.y -= self.velocityy
            elif self.velocityx <= 0 and self.velocityy >= 0:
                self.x += self.velocityx
                self.y -= self.velocityy
            elif self.velocityx <= 0 and self.velocityy <= 0:
                self.x -= self.velocityx
                self.y += self.velocityy
            self.rect.center = (self.x, self.y)
            if math.hypot((self.x - self.spawn[0]), (self.y - self.spawn[1])) > 150:
                self.velocityx = 0
                self.velocityy = 0
                if st.counter_typeI == 3 and not self.typeI_return:
                    self.velocityx = -self.original_velocityx
                    self.velocityy = -self.original_velocityy
                    self.typeI_return = True

        elif self.type == 'TypeI2':
            if self.velocityx >= 0 and self.velocityy >= 0:
                self.x -= self.velocityx
                self.y += self.velocityy
            elif self.velocityx >= 0 and self.velocityy <= 0:
                self.x -= self.velocityx
                self.y += self.velocityy
            elif self.velocityx <= 0 and self.velocityy >= 0:
                self.x -= self.velocityx
                self.y += self.velocityy
            elif self.velocityx <= 0 and self.velocityy <= 0:
                self.x -= self.velocityx
                self.y += self.velocityy
            self.rect.center = (self.x, self.y)
            if math.hypot((self.x - self.spawn[0]), (self.y - self.spawn[1])) > 80:
                self.velocityx = 0
                self.velocityy = 0
                if st.counter_typeI == 0 and not self.typeI_return:
                    self.velocityx = -self.original_velocityx
                    self.velocityy = -self.original_velocityy
                    self.typeI_return = True
        elif self.type == 'TypeJ':
            if not st.counter_typeJ > 0:
                self.y += self.velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'TypeK':
            self.x += self.velocityx
            self.y -= self.velocityy
            if self.x - self.rect.width / 2 < 0 or self.x - st.win_width + self.width/2 > 0:
                self.velocityx *= -1
                #self.image = pygame.transform.rotate(self.image,
                #            st.normalize_angle(math.degrees(math.hypot(self.velocityx, self.velocityy))))
            if self.y - self.rect.height / 2 < 0 or self.y - st.win_height + self.height/2 > 0:
                self.velocityy *= -1
                #self.image = pygame.transform.rotate(self.image,
                #            st.normalize_angle(math.degrees(math.hypot(self.velocityx, self.velocityy))))
            self.rect.center = (self.x, self.y)
        elif self.type == 'TypeL':
            self.y -= self.velocityy
            if self.y > st.win_height / 3:
                self.velocityy = 0
            if self.typeL_return:
                self.velocityy = -1 * self.original_velocityy
            if self.y < -100:
                self.mission_finished = True
            self.rect.center = (self.x, self.y)
        elif self.type == 'TypeM':
            self.y -= self.velocityy
            if self.y > st.win_height / 3:
                self.velocityy = 0
            if self.typeM_return:
                self.velocityy = -1 * self.original_velocityy
            if self.y < -200:
                self.mission_finished = True
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeA':
            if self.y + self.rect.height / 2 >= st.win_height or self.y - self.rect.height / 2 < 0:
                self.velocityy = -self.original_velocityy
            self.y -= self.velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeB':
            if self.y > self.spawn[1]:
                self.y += self.original_velocityy
                self.velocityy = self.original_velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeC':
            if self.y > self.spawn[1]:
                self.y += self.original_velocityy
                self.velocityy = self.original_velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeD':
            self.velocityx = self.original_velocityx * math.cos(math.radians
                            (st.normalize_angle(0 + st.angle_to_point([self.x, self.y], [st.player.x, st.player.y]))))
            self.velocityy = self.original_velocityy * math.sin(math.radians
                            (st.normalize_angle(0 + st.angle_to_point([self.x, self.y], [st.player.x, st.player.y]))))
            self.x -= self.velocityx
            self.y += self.velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeE':
            self.y -= self.original_velocityy
            if self.y - st.win_height - self.height/2 > 0:
                self.x = random.randrange(200, 601, 200)
                self.y = -self.height/2
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeF':
            self.x -= self.velocityx
            self.y += self.velocityy
            if self.x - self.width / 2 < 0:
                self.velocityx = -1 * self.original_velocityx
                self.velocityy = 0
            if self.x - st.win_width + self.width/2 > 0:
                self.velocityx = self.original_Boss_TypeF_velocityx
                self.velocityy = -1 * self.original_Boss_TypeF_velocityy
            if self.y - self.height / 2 < 0 :
                self.velocityy = self.original_Boss_TypeF_velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeG':
            if self.y > self.spawn[1]:
                self.y += self.original_velocityy
                self.velocityy = self.original_velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeH':
            if self.y > self.spawn[1]:
                self.y += self.original_velocityy
                self.velocityy = self.original_velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeI':
            if self.y > self.spawn[1]:
                self.y += self.original_velocityy
                self.velocityy = self.original_velocityy
            self.rect.center = (self.x, self.y)
        elif self.type == 'Boss_TypeJ':
            self.x -= self.velocityx
            if self.x > 700:
                self.velocityx = -1 * self.original_velocityx
            elif self.x < 100:
                self.velocityx = self.original_velocityx
            self.rect.center = (self.x, self.y)
    def set_typeF_data(self):
        if self.type == "Boss_TypeF":
            self.velocityx = self.original_velocityx * math.sin(math.radians(self.angleBossF))
            self.velocityx = self.original_velocityy * math.sin(math.radians(self.angleBossF))
            self.original_Boss_TypeF_velocityx = self.velocityx
            self.original_Boss_TypeF_velocityy = self.velocityy

    def set_boss_point(self,point):
        self.point = point

    # Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
    @staticmethod
    def shoot(timer, bullet_data, firing_data, burst_counter=0):
        parent = bullet_data.parent
        firing_speed = firing_data.firing_speed
        interval = firing_data.interval
        aim = firing_data.aim
        multi = firing_data.multi
        random_arc = firing_data.random_arc
        burst = firing_data.burst
        burst_delay = firing_data.burst_delay
        counter = burst_counter
        angle = firing_data.angle

        if burst:
            if aim:
                shot_angle = st.angle_to_point(parent.rect.center, st.player.rect.center)
            elif angle is None:
                shot_angle = random.uniform(0, 360)
            else:
                shot_angle = angle

            if counter < burst and st.time() - timer >= burst_delay:

                shot_angles = st.multi_shot_angles(multi, shot_angle, interval)
                for arc_shot in range(multi):
                    Projectile(bullet_data,
                                angle=shot_angles[arc_shot] +
                                      random.uniform(-random_arc, random_arc)
                                )

                return st.time(), counter + 1

            else:
                # Reset counter
                if st.time() - timer >= firing_speed:
                    counter = 0

                return timer, counter

        else:
            if aim:
                shot_angle = st.angle_to_point(parent.rect.center, st.player.rect.center)
            elif angle is None:
                shot_angle = random.uniform(0, 360)
            else:
                shot_angle = angle

            shot_angles = st.multi_shot_angles(multi, shot_angle, interval)

            for arc_shot in range(multi):
                Projectile(bullet_data,
                            angle=shot_angles[arc_shot] +
                                  random.uniform(-random_arc, random_arc)
                            )
            return st.time()

        return timer

"""------------------------------------------------------------------------------------------------------"""
class Goblin(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -3
        self.width = 60
        self.height = 45
        self.hp = 5
        self.image_name = 'Goblin.png'
        # projectile info
        self.projectile_width = 10
        self.projectile_height = 31.9375
        self.projectile_damage = 1
        self.projectile_name = 'Goblin_bullet.png'


        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class EyeMonster(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -2
        self.width = 73.845
        self.height = 60
        self.hp = 5
        self.image_name = 'EyeMonster.png'
        # projectile info
        self.projectile_width = 18
        self.projectile_height = 31.76
        self.projectile_damage = 1
        self.projectile_name = 'EyeMonster_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Slime(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -2
        self.width = 33.8325
        self.height = 30
        self.hp = 5
        self.image_name = 'Slime.png'
        # projectile info
        self.projectile_width = 12
        self.projectile_height = 12
        self.projectile_damage = 1
        self.projectile_name = 'Slime_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Goat(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -2
        self.width = 63.75
        self.height = 60
        self.hp = 5
        self.image_name = 'Goat.png'
        # projectile info
        self.projectile_width = 18
        self.projectile_height = 28.5
        self.projectile_damage = 1
        self.projectile_name = 'Goat_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Squirrel(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -4
        self.width = 54.7
        self.height = 50
        self.hp = 1
        self.damage = 3
        self.image_name = 'Squirrel.png'
        # projectile info
        self.projectile_width = 18
        self.projectile_height = 19.632
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Bird(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -4
        self.width = 51.652
        self.height = 50
        self.hp = 5
        self.image_name = 'Bird.png'
        # projectile info
        self.projectile_width = 0
        self.projectile_height = 0
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Fish(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -4
        self.width = 40
        self.height = 60.327
        self.hp = 5
        self.image_name = 'Fish.png'
        # projectile info
        self.projectile_width = 0
        self.projectile_height = 0
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Mouse(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -4
        self.width = 30
        self.height = 64.1379
        self.hp = 5
        self.image_name = 'Mouse.png'
        # projectile info
        self.projectile_width = 0
        self.projectile_height = 0
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Shark(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -4
        self.width = 50
        self.height = 64.36
        self.hp = 5
        self.image_name = 'Shark.png'
        # projectile info
        self.projectile_width = 0
        self.projectile_height = 0
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Starfish(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -4
        self.width = 46.755
        self.height = 40
        self.hp = 5
        self.image_name = 'Starfish.png'
        # projectile info
        self.projectile_width = 0
        self.projectile_height = 0
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)
class Turtle(Enemy):
    def __init__(self, x, y, type):
        # enemy info
        self.speed = -2
        self.width = 50
        self.height = 69
        self.hp = 10
        self.image_name = 'Turtle.png'
        self.point = 10
        self.damage = 1
        # projectile info
        self.projectile_width = 0
        self.projectile_height = 0
        self.projectile_damage = 1
        self.projectile_name = 'Squirrel_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type,
                         self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.length = 3
        self.width = 30
        self.height = 36
        self.image_list = []
        self.image_index = 0
        for index in range(self.length):
            image_path = os.path.join('assets/graphics/coin/coin_'+str(index)+'.png')
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (self.width, self.height))
            self.image_list.append(image)
        self.rect = self.image_list[self.image_index].get_rect()
        self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image_list[self.image_index])
        self.display = st.current_game_surface
        self.last_blit_time = st.time()
        self.animation_interval = 0.1

        self.add(st.coin_group)

    def animate(self):
        if self.image_index < self.length - 1:
            #if st.time() - self.last_blit_time > self.animation_interval:
            self.display.screen.blit(self.image_list[self.image_index], (self.x - self.width/2, self.y-self.height/2))
            self.mask = pygame.mask.from_surface(self.image_list[self.image_index])
            self.last_blit_time = st.time()
            self.image_index += 1
        else:
            self.image_index = 0

    def update(self):
        self.animate()
        self.check_alive()

    def check_alive(self):
        if self.x < -30 or self.x > 830 or self.y < -30 or self.y > 630:
            self.kill