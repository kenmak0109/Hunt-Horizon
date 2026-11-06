import pygame, math, os, random
from settings import Settings as st

# Refecenced: Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter
class Projectile(pygame.sprite.Sprite):
    def __init__(self, bullet_data, angle) -> pygame.sprite.Sprite:
        pygame.sprite.Sprite.__init__(self)

        self.original_bullet_data = bullet_data
        self.original_parent = bullet_data.original_parent
        self.move_speed = bullet_data.speed
        self.damage = bullet_data.damage
        self.angle = angle  # normalized by FiringData
        self.angle_r = math.radians(angle)
        self.turning_rate = bullet_data.turning_rate

        if bullet_data.random_duration == (0, 0):
            self.duration = bullet_data.duration
        else:
            a, b = bullet_data.random_duration
            self.duration = random.uniform(a, b)

        self.spawn_time = st.time()
        self.diag_move_x = self.move_speed * math.cos(math.radians(self.angle))
        self.diag_move_y = self.move_speed * math.sin(math.radians(self.angle))

        if bullet_data.coords:
            self.x, self.y = bullet_data.coords
        else:
            self.x, self.y = bullet_data.parent.rect.center

        self.image = pygame.image.load(os.path.join('assets/images/projectile', bullet_data.image_name)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (bullet_data.image_width, bullet_data.image_height))
        self.image = pygame.transform.rotate(self.image, self.angle - 90)
        self.mask = pygame.mask.from_surface(self.image)

        self.spawn_point = self.x, self.y
        self.spiral = bullet_data.spiral
        self.radial_growth = bullet_data.radial_growth
        self.radius = 0

        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mask = pygame.mask.from_surface(self.image, 250)
        self.mask_rect = self.mask.get_bounding_rects()[0]

        self.add(st.enemy_projectile_group)

    def update(self):
        self.move()
        self.update_rect()
        self.check_out_of_bound()
        self.check_duration()

    def move(self):
        if self.spiral:
            self.x = self.spawn_point[0] + self.radius * math.cos(math.radians(self.angle))
            self.y = self.spawn_point[1] + self.radius * math.sin(math.radians(self.angle))
            self.radius += self.radial_growth
            self.angle += self.turning_rate
        else:
            self.x += self.diag_move_x
            self.y -= self.diag_move_y

    def check_out_of_bound(self):
        if self.rect.bottom < -100 or self.rect.top > 700 or self.rect.left < -100 or self.rect.right > 900:
            self.kill()

    def update_rect(self):
        self.rect.center = (self.x, self.y)

    def movement_type_manager(self):
        pass

    def check_duration(self):
        if st.time() - self.spawn_time >= self.duration:
            self.kill()


class FiringData(object):
    def __init__(self, firing_speed=1, interval=10, angle=None,
                 aim=False, multi=1, random_arc=0,
                 burst=0, burst_delay=0):
        self.firing_speed = firing_speed
        self.interval = interval
        self.aim = aim
        self.multi = multi
        self.random_arc = random_arc
        self.burst = burst
        self.burst_delay = burst_delay
        self.angle = angle

class BulletData(object):
    def __init__(self, original_parent, parent=None, coords=None, damage=1, speed=0,
                 random_speed=(0, 0), duration=5, random_duration=(0, 0),
                 homing=False, turning_rate=0, spiral=False, radial_growth=0, exploding=None,
                 infinite_explosion=False, image_width=0, image_height=0, image_name=None):

        self.original_parent = original_parent
        if parent:
            self.parent = parent
        else:
            self.parent = self.original_parent
        self.coords = coords
        self.damage = damage
        self.random_speed = random_speed
        self.speed = speed
        self.duration = duration
        self.random_duration = random_duration
        self.homing = homing
        self.turning_rate = turning_rate
        self.exploding = exploding
        self.infinite_explosion = infinite_explosion
        self.spiral = spiral
        self.radial_growth = radial_growth
        self.image_width = image_width
        self.image_height = image_height
        self.image_name = image_name