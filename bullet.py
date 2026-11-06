import pygame, os, math
from settings import Settings as st

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, damage, image, angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.move_speed = speed
        self.damage = damage
        self.angle = st.normalize_angle(angle)
        self.image = pygame.image.load(os.path.join('assets/images/bullet',image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, self.angle + 90)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect(center=(x, y))
        self.diag_move_x = self.move_speed * math.cos(math.radians(self.angle))
        self.diag_move_y = self.move_speed * math.sin(math.radians(self.angle))
        # add it to sprite group
        self.add(st.player_bullet_group)

    def update(self):
        self.x -= self.diag_move_x
        self.y += self.diag_move_y
        self.rect.center = (self.x, self.y)
        self.check_status()

    def check_status(self):
        if self.rect.bottom < 0 or self.rect.left < 0 or\
                self.rect.right > st.win_width or self.rect.top > st.win_height:
            self.kill()