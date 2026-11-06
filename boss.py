import pygame
import enemy
from settings import Settings as st

class Boss_1(enemy.Enemy):
    def __init__(self, x, y, type):
        # boss info
        self.speed = -2
        self.width = 130
        self.height = 130
        self.hp = 20
        self.max_hp = 20
        self.image_name = 'Boss_1.png'
        self.win_point = 500

        # boss projectile info
        self.projectile_width = 10
        self.projectile_height = 28.6
        self.projectile_damage = 2
        self.projectile_name = 'Boss_1_bullet.png'
        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_2(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 75
        self.height = 177.75
        self.hp = 30
        self.max_hp = 30
        self.image_name = 'Boss_2.png'
        self.win_point = 2000

        # boss projectile info
        self.projectile_width = 8
        self.projectile_height = 24
        self.projectile_damage = 3
        self.projectile_name = 'Boss_2_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_3(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 125
        self.height = 100
        self.hp = 30
        self.image_name = 'Boss_3.png'
        self.win_point = 4000

        # boss projectile info
        self.projectile_width = 15
        self.projectile_height = 25.7
        self.projectile_damage = 3
        self.projectile_name = 'Boss_3_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_4(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 150
        self.height = 130
        self.hp = 30
        self.max_hp = 30
        self.image_name = 'Boss_4.png'
        self.win_point = 7500

        # boss projectile info
        self.projectile_width = 15
        self.projectile_height = 26.4
        self.projectile_damage = 3
        self.projectile_name = 'Boss_4_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_5(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 160
        self.height = 140
        self.hp = 40
        self.max_hp = 40
        self.image_name = 'Boss_5.png'
        self.win_point = 10000

        # boss projectile info
        self.projectile_width = 21.5
        self.projectile_height = 15
        self.projectile_damage = 4
        self.projectile_name = 'Boss_5_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_6(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 146
        self.height = 130
        self.hp = 40
        self.max_hp = 40
        self.image_name = 'Boss_6.png'
        self.win_point = 15000

        # boss projectile info
        self.projectile_width = 15
        self.projectile_height = 26.0625
        self.projectile_damage = 4
        self.projectile_name = 'Boss_6_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_7(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 146
        self.height = 130
        self.hp = 40
        self.max_hp = 40
        self.image_name = 'Boss_7.png'
        self.win_point = 22500

        # boss projectile info
        self.projectile_width = 15
        self.projectile_height = 24.796
        self.projectile_damage = 4
        self.projectile_name = 'Boss_7_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_8(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 147
        self.height = 100
        self.hp = 50
        self.max_hp = 50
        self.image_name = 'Boss_8.png'
        self.win_point = 30000

        # boss projectile info
        self.projectile_width = 8
        self.projectile_height = 28.8
        self.projectile_damage = 5
        self.projectile_name = 'Boss_8_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_9(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 139
        self.height = 130
        self.hp = 50
        self.max_hp = 50
        self.image_name = 'Boss_9.png'
        self.win_point = 40000

        # boss projectile info
        self.projectile_width = 16.66
        self.projectile_height = 15
        self.projectile_damage = 5
        self.projectile_name = 'Boss_9_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)
class Boss_10(enemy.Enemy):
    def __init__(self, x, y, type, speed=2):
        # boss info
        self.speed = -speed
        self.width = 150
        self.height = 150
        self.hp = 60
        self.max_hp = 60
        self.image_name = 'Boss_10.png'
        self.win_point = 50000

        # boss projectile info
        self.projectile_width = 20
        self.projectile_height = 33.6
        self.projectile_damage = 6
        self.projectile_name = 'Boss_10_bullet.png'

        super().__init__(x, y, self.speed, self.width, self.height, self.hp, self.image_name, type, self.projectile_width, self.projectile_height,
                         self.projectile_damage, self.projectile_name, is_boss=True)