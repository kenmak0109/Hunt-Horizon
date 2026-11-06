import pygame
import os

from settings import Settings as st
from item import *

pygame.init()


class Screen:
    def __init__(self, bgimg):
        self.bgimg = pygame.image.load(os.path.join('assets/images/background',bgimg))
        self.width = st.win_width
        self.height = st.win_height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        self.bgimg = pygame.transform.scale(self.bgimg, (self.width, self.height))
        self.screen.blit(self.bgimg, (0, 0))

class Gameplay(Screen):
    def __init__(self, bgimg):
        super().__init__(bgimg)
        self.gameplay_height = 1600
        self.gameplay_blit_pos_y = 0
        self.gameplay_blit_pos_y_default = -1000
        self.gameplay_blit_pos_y_rate = 10

    def draw(self):
        rel_y = self.gameplay_blit_pos_y_default + self.gameplay_blit_pos_y % self.gameplay_height
        self.bgimg = pygame.transform.scale(self.bgimg, (self.width, self.gameplay_height))
        self.screen.blit(self.bgimg, (0, rel_y - self.gameplay_height))
        if rel_y < self.height:
            self.screen.blit(self.bgimg, (0, rel_y))
        self.gameplay_blit_pos_y += self.gameplay_blit_pos_y_rate

class Animated_screen():
    def __init__(self):
        self.list = []
        self.length = 9
        self.is_win = False
        for i in range(self.length):
            self.list.append(pygame.image.load(os.path.join
                                               ('assets/graphics/gameover/'+ 'sunset_' + str(i) + '.png')))
        if self.is_win:
            self.current_object = self.length - 1
        else:
            self.current_object = 0
        self.image = self.list[self.current_object]
        self.width = st.win_width
        self.height = st.win_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.last_blit = st.time()


    def change_state(self):
        self.animate()

    def animate(self):
        if not self.is_win:
            if st.time() - self.last_blit > 0.25:
                self.current_object += 1
                if self.current_object >= self.length:
                    self.current_object = 0
                self.last_blit = st.time()
        else:
            if st.time() - self.last_blit > 0.25:
                self.current_object -= 1
                if self.current_object < 0:
                    self.current_object = self.length - 1
                self.last_blit = st.time()


    def draw(self):
        self.image = self.list[self.current_object]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.screen.blit(self.image, (0,0))

class Button():
    def __init__(self, pos, size, image):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.image = pygame.image.load(os.path.join('assets/images/button', image))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
        self.current = False
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

    def adjust_image(self, image):
        self.image = image

class Image:
    def __init__(self, pos, width, height, folder, image):
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.image.load(os.path.join('assets/images/item/'+folder, image))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

"""Reference: Clear Code. "Creating an animated button in Pygame." Youtube, 
                Jul. 4, 2021 [Video file]. Available: https://www.youtube.com/watch?v=8SzTzvrWaAA&t=1365s&ab_channel=ClearCode"""
class Button_text():
    def __init__(self, text, pos, width, height):
        self.pressed = False
        self.font = pygame.font.Font(None, 30)
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_rect.center = pos
        self.top_color = '#475F77'
        self.text_surf = self.font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, display):
        pygame.draw.rect(display, self.top_color, self.top_rect, border_radius = 12)
        display.blit(self.text_surf, self.text_rect)
        self.animate()

    def animate(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#9999FF'
        else:
            self.top_color = '#475F77'

class Animated_button():
    def __init__(self, name, length, pos, size):
        self.list = []
        self.length = length
        self.size = size
        for i in range(length):
            self.list.append(pygame.image.load(os.path.join('assets/graphics/button/'+ name, name + '_' + str(i) + '.png')))
        self.current_object = 0

        self.image = self.list[self.current_object]
        self.image = pygame.transform.scale(self.image, self.size)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def draw(self, display):
        if self.rect.collidepoint(st.get_mouse_pos()):
            self.current_object = 1
        else:
            self.current_object = 0
        self.image = self.list[self.current_object]
        self.image = pygame.transform.scale(self.image, self.size)
        display.blit(self.image, self.rect.topleft)

    """def offset(self, pos_mouse, pos_button):
        return ( pos_button[0] - pos_mouse[0], pos_button[1] - pos_mouse[1])"""

class Text:
    def __init__(self, pos, text, size, color):
        self.font = pygame.font.SysFont('Comic Sans MS', size)
        self.size = size
        self.textsurf = self.font.render(str(text), True, color)
        self.rect = self.textsurf.get_rect()
        self.x = pos[0]
        self.y = pos[1]
        self.rect.center = (self.x, self.y)

    def draw(self, display):
        display.blit(self.textsurf, self.rect.topleft)

class Volume_control():
    def __init__(self, pos, width, height):
        self.pressed = False
        self.pressed_counter = 0
        self.rect = pygame.Rect(pos, (width, height))
        self.rect.center = pos
        self.color = (255,255,255)
        self.current_volume = 0
        self.slider_rect = pygame.Rect((self.rect.left, self.rect.centery), (20, height + 10))
        self.slider_rect.center = (self.current_volume + self.rect.left, self.rect.centery)
        self.slider_color = (128,128,128)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)
        pygame.draw.rect(display, self.slider_color, self.slider_rect)

    def change_volume(self, pos):
        if pos[0] > self.rect.right:
            self.current_volume = st.music_volume_bar_length
        elif pos[0] < self.rect.left:
            self.current_volume = 0
        else:
            self.current_volume = pos[0] - self.rect.left
        return self.current_volume

    def update(self):
        if self.current_volume < 0:
            self.current_volume = 0
        if self.current_volume > st.music_volume_bar_length:
            self.current_volume = st.music_volume_bar_length
        self.slider_rect.center = (self.current_volume + self.rect.left, self.rect.centery)
        return self

    def is_pressed(self):
        self.pressed = True

    def set_current_volume(self, volume):
        self.current_volume = volume
        self.slider_rect.center = (self.current_volume + self.rect.left, self.rect.centery)

class Inventary():
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

class Inventary_item(Inventary):
    def __init__(self, pos, image=''):
        self.x = pos[0]
        self.y = pos[1]

class Your_player(object):
    def __init__(self, pos, image_size, image_folder, image_name, button_size, dictionary):
        self.image_x = pos[0]
        self.image_y = pos[1]
        self.image = Image((self.image_x, self.image_y), image_size[0], image_size[1], image_folder, image_name)
        self.button = Button_text('Check', (self.image_x, self.image.rect.bottom + 30), button_size[0], button_size[1])
        self.dictionary = dictionary

    def draw(self,display):
        self.image.draw(display)
        self.button.draw(display)

    def display_detail(self, display):
        pass

    def check_is_brought(self, name):
        pass

class Your_player_skin(Your_player):
    def __init__(self, pos, image_size, image_folder, image_name, button_size, dictionary, skin):
        self.image_x = pos[0]
        self.image_y = pos[1]
        self.image = Image((self.image_x, self.image_y), image_size[0], image_size[1], image_folder, image_name)
        self.button = Button_text('Check', (self.image_x, self.image.rect.bottom + 30), button_size[0], button_size[1])
        self.text_0 = Text((632, 190), 'Skin details',
                           30, (0, 0, 0))
        self.image_detail = Image((632, self.text_0.rect.bottom + 60), image_size[0] + 40, image_size[1] + 40,
                                  image_folder, image_name)
        self.button_use = Button_text('Use', (632, self.image_detail.rect.bottom + 200), button_size[0]+50, button_size[1]+17)
        self.dictionary = dictionary
        self.skin = skin
        self.is_brought = st.upgrades['Skin'][self.skin]
        super().__init__(pos, image_size, image_folder, image_name, button_size, dictionary)

    def display_detail(self, display):
        text_0 = Text((632, self.image_detail.rect.bottom + 40), 'Player skin: [%s] ' % self.skin,
                      20, (0, 0, 0))
        if self.is_brought:
            text_1 = Text((632, text_0.rect.bottom + 20), 'Status: Owned', 20,
                          (0, 0, 0))
            if st.player_skin == self.skin+'.png':
                text_2 = Text((632, text_1.rect.bottom + 20), 'Using: Yes', 20,
                          (0, 0, 0))
                text_2.draw(display)
            else:
                text_2 = Text((632, text_1.rect.bottom + 20), 'Using: No', 20,
                              (0, 0, 0))
                text_2.draw(display)
        else:
            text_1 = Text((632, text_0.rect.bottom + 20), 'Status: Available at shop', 20,
                          (255, 0, 0))

        self.image_detail.draw(display)
        if self.is_brought:
            self.button_use.draw(display)
            if self.button_use.top_rect.collidepoint(st.get_mouse_pos()):
                if st.check_event():
                    st.player_skin = self.skin+'.png'
                    st.sound_button_clicked.play()
        self.text_0.draw(display)
        text_0.draw(display)
        text_1.draw(display)

class Your_player_pattern(Your_player):
    def __init__(self, pos, image_size, image_folder, image_name, button_size, dictionary):
        self.image_x = pos[0]
        self.image_y = pos[1]
        self.image = Image((self.image_x, self.image_y), image_size[0], image_size[1], image_folder, image_name)
        self.button = Button_text('Check', (self.image_x, self.image.rect.bottom + 30), button_size[0], button_size[1])
        self.text_0 = Text((632, 190), 'Pattern details',
                           30, (0, 0, 0))
        self.image_detail = Image((632, self.text_0.rect.bottom + 60), image_size[0] + 40, image_size[1] + 40,
                                  image_folder, image_name)
        self.dictionary = dictionary
        super().__init__(pos, image_size, image_folder, image_name, button_size, dictionary)

    def display_detail(self, display):
        text_0 = Text((632, self.image_detail.rect.bottom + 40), 'Pattern: [%s]' % self.dictionary['name'],
                      20, (0, 0, 0))
        text_1 = Text((632, text_0.rect.bottom + 20), 'Number of shots: [%d]' % self.dictionary['current'],
                      20, (0, 0, 0))
        text_2 = Text((632, text_1.rect.bottom + 20), 'Level: [%d]' % self.dictionary['level'],
                      20, (0, 0, 0))
        self.image_detail.draw(display)
        self.text_0.draw(display)
        text_0.draw(display)
        text_1.draw(display)
        text_2.draw(display)

class Your_player_skill(Your_player):
    def __init__(self, pos, image_size, image_folder, image_name, button_size, dictionary):
        self.image_x = pos[0]
        self.image_y = pos[1]
        self.image = Image((self.image_x, self.image_y), image_size[0], image_size[1], image_folder, image_name)
        self.button = Button_text('Check', (self.image_x, self.image.rect.bottom + 30), button_size[0], button_size[1])
        self.text_0 = Text((632, 190), 'Skill details',
                           30, (0, 0, 0))
        self.image_detail = Image((632, self.text_0.rect.bottom + 60), image_size[0] + 40, image_size[1] + 40,
                                  image_folder, image_name)
        self.dictionary = dictionary
        self.name = self.dictionary['name']
        self.is_brought = self.dictionary['is brought']
        super().__init__(pos, image_size, image_folder, image_name, button_size, dictionary)

    def display_detail(self, display):
        text_0 = Text((632, self.image_detail.rect.bottom + 40), 'Player skill: [%s] ' % self.name,
                      20, (0, 0, 0))
        if self.is_brought:
            text_1 = Text((632, text_0.rect.bottom + 10), 'Status: Owned', 20,
                          (0, 0, 0))
        else:
            text_1 = Text((632, text_0.rect.bottom + 10), 'Status: Available at shop', 20,
                          (255, 0, 0))
        if self.name == 'Barrier':
            text_2 = Text((632, text_1.rect.bottom + 20), 'Description: Ability to become invincible', 14,
                      (0, 0, 0))
            if self.is_brought:
                text_3 = Text((632, text_2.rect.bottom + 10), 'Duration: [%ds]'%self.dictionary['invincible'], 14,
                              (0, 0, 0))
                text_4 = Text((632, text_3.rect.bottom + 10), 'Cooldown: [%ds]'%self.dictionary['cooldown'], 14,
                              (0, 0, 0))
                text_5 = Text((632, text_4.rect.bottom + 10), 'Level: [%d]'%self.dictionary['level'], 14,
                              (0, 0, 0))
                text_2.draw(display)
                text_3.draw(display)
                text_4.draw(display)
                text_5.draw(display)
        elif self.name == 'Dash':
            text_2 = Text((632, text_1.rect.bottom + 20), 'Description: Ability to dash like a boss', 14,
                      (0, 0, 0))
            if self.is_brought:
                text_3 = Text((632, text_2.rect.bottom + 10), 'Number of charge: [%d]'%self.dictionary['charge'], 14,
                              (0, 0, 0))
                text_4 = Text((632, text_3.rect.bottom + 10), 'Cooldown: [%ds]'%self.dictionary['cooldown'], 14,
                              (0, 0, 0))
                text_5 = Text((632, text_4.rect.bottom + 10), 'Level: [%d]'%self.dictionary['level'], 14,
                              (0, 0, 0))
                text_2.draw(display)
                text_3.draw(display)
                text_4.draw(display)
                text_5.draw(display)
        elif self.name == 'Grenade':
            text_2 = Text((632, text_1.rect.bottom + 20), 'Description: Ability to throw a grande', 14,
                      (0, 0, 0))
            if self.is_brought:
                text_3 = Text((632, text_2.rect.bottom + 10), 'Effective diameter: [%d]'%self.dictionary['diameter'], 14,
                              (0, 0, 0))
                text_4 = Text((632, text_3.rect.bottom + 10), 'Number of charge: [%d]' % self.dictionary['charge'], 14,
                              (0, 0, 0))
                text_5 = Text((632, text_4.rect.bottom + 10), 'Cooldown: [%ds]'%self.dictionary['cooldown'], 14,
                              (0, 0, 0))
                text_6 = Text((632, text_5.rect.bottom + 10), 'Damage: [%d] times player damage' % self.dictionary['damage'], 14,
                              (0, 0, 0))
                text_7 = Text((632, text_6.rect.bottom + 10), 'Level: [%d]'%self.dictionary['level'], 14,
                              (0, 0, 0))
                text_2.draw(display)
                text_3.draw(display)
                text_4.draw(display)
                text_5.draw(display)
                text_6.draw(display)
                text_7.draw(display)
        elif self.name == 'Laser':
            text_2 = Text((632, text_1.rect.bottom + 20), 'Description: Ability to emit a powerful laser', 14,
                      (0, 0, 0))
            if self.is_brought:
                text_3 = Text((632, text_2.rect.bottom + 10), 'Effective diameter: [%d]'%st.player_width, 14,
                              (0, 0, 0))
                text_4 = Text((632, text_3.rect.bottom + 10), 'Laser duration: [3s]', 14,
                              (0, 0, 0))
                text_5 = Text((632, text_4.rect.bottom + 10), 'Cooldown: [%ds]'%self.dictionary['cooldown'], 14,
                              (0, 0, 0))
                text_6 = Text((632, text_5.rect.bottom + 10), 'Damage: [6] times player damage', 14,
                              (0, 0, 0))
                text_7 = Text((632, text_6.rect.bottom + 10), 'Level: [%d]'%self.dictionary['level'], 14,
                              (0, 0, 0))
                text_2.draw(display)
                text_3.draw(display)
                text_4.draw(display)
                text_5.draw(display)
                text_6.draw(display)
                text_7.draw(display)

        self.image_detail.draw(display)
        self.text_0.draw(display)
        text_0.draw(display)
        text_1.draw(display)

class Your_player_attribute(Your_player):
    def __init__(self, pos, image_size, image_folder, image_name, button_size, dictionary):
        self.image_x = pos[0]
        self.image_y = pos[1]
        self.image = Image((self.image_x, self.image_y), image_size[0], image_size[1], image_folder, image_name)
        self.button = Button_text('Check', (self.image_x, self.image.rect.bottom + 30), button_size[0], button_size[1])
        self.text_0 = Text((632, 190), 'Attribute details',
                           30, (0, 0, 0))
        self.image_detail = Image((632, self.text_0.rect.bottom + 60), image_size[0] + 40, image_size[1] + 40, image_folder, image_name)
        self.dictionary = dictionary
        self.name = self.dictionary['name']
        super().__init__(pos, image_size, image_folder, image_name, button_size, dictionary)

    def display_detail(self, display):
        text_1 = Text((632, self.image_detail.rect.bottom + 40), 'Attribute: [%s]' % self.dictionary['name'],
                      20, (0, 0, 0))
        text_2 = Text((632, text_1.rect.bottom + 20), 'Level: [%d]' % self.dictionary['level'],
                      20, (0, 0, 0))
        if self.name == 'Attack damage':
            text_3 = Text((632, text_2.rect.bottom + 20), 'Damage: [%.1f]' % self.dictionary['current'],
                          20, (0, 0, 0))
            text_3.draw(display)
        elif self.name == 'Attack frequency':
            text_3 = Text((632, text_2.rect.bottom + 20), 'Frequency: [%.1fs] per shot' % self.dictionary['current'],
                          20, (0, 0, 0))
            text_3.draw(display)
        elif self.name == 'Bullet velocity':
            text_3 = Text((632, text_2.rect.bottom + 20), 'Velocity: [%.1f]' % self.dictionary['current'],
                          20, (0, 0, 0))
            text_3.draw(display)
        elif self.name == 'Max health':
            text_3 = Text((632, text_2.rect.bottom + 20), 'Max health: [%d]' % self.dictionary['current'],
                          20, (0, 0, 0))
            text_3.draw(display)
        self.image_detail.draw(display)
        self.text_0.draw(display)
        text_1.draw(display)
        text_2.draw(display)
