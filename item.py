import collections, decimal
import pygame
from settings import Settings as st
import screen

class Item(object):
    def __init__(self, name):
        self.name = name

class Skin(Item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.cost = dictionary['cost']
        self.item = ''
        self.is_brought = False
        super().__init__(self.name)
        self.update_text()

    def upgrade(self):
        if st.user_point >= self.cost:
            if not self.is_brought:
                st.update_user_point(self.cost)
                self.is_brought = True
                self.update_text()
                self.update_dictionary()

    def detail_display(self, screen):
        if not self.is_brought:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
        else:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
    def update_text(self):
        if not self.is_brought:
            self.text_0 = screen.Text((self.x, self.y), "You have not brought this before", 30, (255,0,0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Confirm to purchase [%s] player skin?" % self.item, 30, (0,0,0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20), "Point required: %d" % self.cost, 20,
                                      (0, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                      "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
        else:
            self.text_0 = screen.Text((self.x, self.y + 30), "You have reached Brought this before!", 30, (0, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 30), "Click [Yes or No] to return last page", 20, (0, 0, 0))
    def check_if_skin_is_brought(self, skin):
        if self.dictionary[skin]:
            self.is_brought = True
            self.item = skin
        else:
            self.is_brought = False
            self.item = skin
        self.update_text()
    def update_dictionary(self):
        self.dictionary[self.item] = self.is_brought
        st.upgrades[self.name][self.item] = self.dictionary[self.item]
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()

class Pattern(Item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.current = dictionary['current']
        self.default = dictionary['default']
        self.increase = dictionary['increase']
        self.cost_factor = 1000
        self.level = dictionary['level']
        self.max_level = 5
        self.base_cost = dictionary['base cost']
        self.cost = self.level * self.base_cost
        self.update = self.current + self.increase

        # text
        self.update_text()
        super().__init__(self.name)
    def upgrade(self):
        if st.user_point >= self.cost:
            if self.level <= self.max_level:
                st.update_user_point(self.cost)
                self.current += self.increase
                self.level += 1
                self.cost = self.base_cost * self.level
                self.update = self.current + self.increase
                self.update_text()
                self.update_dictionary()
    def reset_item(self):
        self.current = self.default
        self.level = 1
        self.cost = self.level * (self.base_cost + 500)

    def detail_display(self, screen):
        if self.level <= self.max_level:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
        else:
            self.text_6.draw(screen)
            self.text_7.draw(screen)
            self.text_8.draw(screen)
    def update_text(self):
        self.text_0 = screen.Text((self.x, self.y), "Confirm to purchase [%s]?" % self.name, 30, (0,0,0))
        self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Current level: %d" % self.level, 20, (0,0,0))
        self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20), "Upgrade from: %d --> %d" % (self.current,self.update), 20, (255,0,0))
        self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20), "Point required: %d" % self.cost, 20, (0,0,0))
        self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0,0,255))

        self.text_6 = screen.Text((self.x, self.y + 30), "You have reached the maximum level!", 30, (0, 0, 0))
        self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 30), "Your [%s] value is [%.1f]" %(self.name, self.current), 20, (255, 0, 0))
        self.text_8 = screen.Text((self.x, self.text_7.rect.bottom + 30), "Click [Yes or No] to return last page", 20,
                                  (0, 0, 0))
    def update_dictionary(self):
        self.dictionary['current'] = self.current
        self.dictionary['level'] = self.level
        st.upgrades[self.name]['current'] = self.dictionary['current']
        st.upgrades[self.name]['level'] = self.dictionary['level']
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()
class Skill_item(Item):
    def __init__(self, name):
        super().__init__(name)
class Barrier(Skill_item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.invincible = dictionary['invincible']
        self.cooldown = dictionary['cooldown']
        self.level = dictionary['level']
        self.max_level = 3
        self.cost = dictionary['cost']
        self.cost_interval = dictionary['cost_interval']
        self.is_brought = dictionary['is brought']
        super().__init__(self.name)
        self.update_text()

    def upgrade(self):
        if st.user_point >= self.cost:
            if self.level <= 0:
                st.update_user_point(self.cost)
                self.is_brought = True
                self.level += 1
                self.cost +=  self.cost_interval
            elif self.level > 0 and self.level < self.max_level:
                st.update_user_point(self.cost)
                self.cooldown -= 5
                self.level += 1
                self.cost +=  self.cost_interval
            self.update_text()
            self.update_dictionary()

    def detail_display(self, screen):
        if self.level < self.max_level:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
            self.text_5.draw(screen)
        else:
            self.text_6.draw(screen)
            self.text_7.draw(screen)
            self.text_8.draw(screen)
            self.text_9.draw(screen)

    def reset_item(self):
        self.level = 0
        self.cost = 5000
        self.cooldown = 45
        self.brought = False

    def update_text(self):
        if not self.is_brought:
            self.text_0 = screen.Text((self.x, self.y), "You have not brought this before", 30, (255,0,0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Confirm to purchase [%s]?" % self.name, 30, (0,0,0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                      "Invincible time: %d" % self.invincible, 20, (255, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                      "Cooldown: %d" % self.cooldown, 20, (255, 0, 0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Point required: %d" % self.cost, 20,
                                      (0, 0, 0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 20),
                                      "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
        else:
            self.text_0 = screen.Text((self.x, self.y), "Confirm to upgrade [%s]?" % self.name, 30, (0, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Current level: %d" % self.level, 20, (0,0,0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                      "Invincible time: %d" % self.invincible, 20, (255, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20), "Cooldown upgrade from: %.1f --> %.1f" % (self.cooldown, self.cooldown - 5), 20, (255,0,0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Point required: %d" % self.cost, 20, (0,0,0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 20), "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0,0,255))
        self.text_6 = screen.Text((self.x, self.y + 30), "You have reached the maximum level!", 30, (0, 0, 0))
        self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 30), "Your invincible time is: [%.1f]" % self.invincible, 20, (255, 0, 0))
        self.text_8 = screen.Text((self.x, self.text_7.rect.bottom + 30), "Your skill cooldown is [%.1f]" % self.cooldown, 20, (255, 0, 0))
        self.text_9 = screen.Text((self.x, self.text_8.rect.bottom + 30), "Click [Yes or No] to return last page", 20, (0, 0, 0))

    def update_dictionary(self):
        self.dictionary['cooldown'] = self.cooldown
        self.dictionary['level'] = self.level
        self.dictionary['cost'] = self.cost
        self.dictionary['is brought'] = self.is_brought
        st.upgrades[self.name]['cooldown'] = self.dictionary['cooldown']
        st.upgrades[self.name]['level'] = self.dictionary['level']
        st.upgrades[self.name]['cost'] = self.dictionary['cost']
        st.upgrades[self.name]['is brought'] = self.dictionary['is brought']
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()
class Dash(Skill_item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.charge = dictionary['charge']
        self.cooldown = dictionary['cooldown']
        self.level = dictionary['level']
        self.max_level = 3
        self.cost = dictionary['cost']
        self.cost_interval = dictionary['cost_interval']
        self.is_brought = dictionary['is brought']
        super().__init__(self.name)
        self.update_text()

    def upgrade(self):
        if st.user_point >= self.cost:
            if self.level <= 0:
                st.update_user_point(self.cost)
                self.is_brought = True
                self.level += 1
                self.cost += self.level + self.cost_interval
                self.update_text()
                self.update_dictionary()
            elif self.level == 1:
                st.update_user_point(self.cost)
                self.cooldown -= 5
                self.cost += self.level + self.cost_interval
                self.level += 1
                self.update_text()
                self.update_dictionary()
            elif self.level == 2:
                st.update_user_point(self.cost)
                self.cooldown -= 3
                self.charge = 2
                self.level = 3
                self.update_text()
                self.update_dictionary()

    def detail_display(self, screen):
        if self.level < self.max_level:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
            self.text_5.draw(screen)
        else:
            self.text_6.draw(screen)
            self.text_7.draw(screen)
            self.text_8.draw(screen)
            self.text_9.draw(screen)

    def update_text(self):
        if not self.is_brought:
            self.text_0 = screen.Text((self.x, self.y), "You have not brought this before", 30, (255, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Confirm to purchase [%s]?" % self.name,
                                      30, (0, 0, 0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                      "Charge: %d" % self.charge, 20, (255, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                      "Cooldown: %d" % self.cooldown, 20, (255, 0, 0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Point required: %d" % self.cost, 20,
                                      (0, 0, 0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 20),
                                      "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
        else:
            self.text_0 = screen.Text((self.x, self.y), "Confirm to upgrade [%s]?" % self.name, 30, (0, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Current level: %d" % self.level, 20,
                                      (0, 0, 0))
            if self.level == 1:
                self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                          "Charge: %d" % self.charge, 20, (255, 0, 0))
                self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                          "Cooldown upgrade from: %.1f --> %.1f" % (self.cooldown, self.cooldown - 5), 20,
                                          (255, 0, 0))
            else:
                self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                          "Charge upgrade from: %d --> %d" % (self.charge, self.charge + 1), 20, (255, 0, 0))
                self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                          "Cooldown upgrade from: %.1f --> %.1f" % (self.cooldown, self.cooldown - 3),
                                          20,
                                          (255, 0, 0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Point required: %d" % self.cost, 20,
                                      (0, 0, 0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 20),
                                      "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
        self.text_6 = screen.Text((self.x, self.y + 30), "You have reached the maximum level!", 30, (0, 0, 0))
        self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 30),
                                  "Your number of charge is: [%d]" % self.charge, 20, (255, 0, 0))
        self.text_8 = screen.Text((self.x, self.text_7.rect.bottom + 30),
                                  "Your skill cooldown is [%.1f]" % self.cooldown, 20, (255, 0, 0))
        self.text_9 = screen.Text((self.x, self.text_8.rect.bottom + 30), "Click [Yes or No] to return last page", 20,
                                  (0, 0, 0))

    def update_dictionary(self):
        self.dictionary['charge'] = self.charge
        self.dictionary['cooldown'] = self.cooldown
        self.dictionary['level'] = self.level
        self.dictionary['cost'] = self.cost
        self.dictionary['is brought'] = self.is_brought
        st.upgrades[self.name]['charge'] = self.dictionary['charge']
        st.upgrades[self.name]['cooldown'] = self.dictionary['cooldown']
        st.upgrades[self.name]['level'] = self.dictionary['level']
        st.upgrades[self.name]['cost'] = self.dictionary['cost']
        st.upgrades[self.name]['is brought'] = self.dictionary['is brought']
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()

    def reset_item(self):
        self.level = 0
        self.cost = 5000
        self.cooldown = 20
        self.charge = 1
        self.brought = False
class Grenade(Skill_item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.diameter = dictionary['diameter']
        self.charge = dictionary['charge']
        self.cooldown = dictionary['cooldown']
        self.damage = dictionary['damage']
        self.level = dictionary['level']
        self.max_level = 5
        self.cost = dictionary['cost']
        self.is_brought = dictionary['is brought']

        super().__init__(self.name)
        self.update_text()

    def upgrade(self):
        if st.user_point >= self.cost:
            if self.level <= 0:
                st.update_user_point(self.cost)
                self.is_brought = True
                self.level += 1
                self.cost = 4000
            elif self.level == 1:
                st.update_user_point(self.cost)
                self.cooldown = 12
                self.cost = 6000
                self.level = 2
            elif self.level == 2:
                st.update_user_point(self.cost)
                self.charge = 3
                self.level = 3
                self.cost = 10000
            elif self.level == 3:
                st.update_user_point(self.cost)
                self.diameter = st.player_width * 4
                self.level = 4
                self.cost = 15500
            elif self.level == 4:
                st.update_user_point(self.cost)
                self.cooldown = 10
                self.damage = 3.5
                self.level = 5
            self.update_text()
            self.update_dictionary()

    def detail_display(self, screen):
        if self.level < self.max_level:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
            self.text_5.draw(screen)
            self.text_6.draw(screen)
            self.text_7.draw(screen)
        else:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
            self.text_5.draw(screen)

    def update_text(self):
        if not self.is_brought:
            self.text_0 = screen.Text((self.x, self.y), "You have not brought this before", 30, (255, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 15), "Confirm to purchase [%s]?" % self.name,30, (0, 0, 0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 15),"Explosion diameter: %.1f" % self.diameter, 20, (255, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 15),"Charge: %d" % self.charge, 20, (255, 0, 0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 15),"Cooldown: %d" % self.cooldown, 20, (255, 0, 0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 15),"Damage: %d times player attack damage" % self.damage, 20, (255, 0, 0))
            self.text_6 = screen.Text((self.x, self.text_5.rect.bottom + 15), "Point required: %d" % self.cost, 20,(0, 0, 0))
            self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 15),"Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
        else:
            self.text_0 = screen.Text((self.x, self.y), "Confirm to upgrade [%s]?" % self.name, 30, (0, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 15), "Current level: %d" % self.level, 20,(0, 0, 0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 15), "Explosion diameter: %.1f" % self.diameter, 20,(255, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 15), "Charge: %d" % self.charge, 20,(255, 0, 0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 15), "Cooldown: %d" % self.cooldown, 20,(255, 0, 0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 15),"Damage: %d times player attack damage" % self.damage, 20, (255, 0, 0))
            self.text_6 = screen.Text((self.x, self.text_5.rect.bottom + 15), "Point required: %d" % self.cost, 20,(0, 0, 0))
            self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 15),"Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
            if not self.level < self.max_level:
                self.text_0 = screen.Text((self.x, self.y + 30), "You have reached the maximum level!", 30, (0, 0, 0))
                self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20),
                                          "Explosion diameter: [%d]" % self.diameter, 20, (255, 0, 0))
                self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                          "Charge: [%.1f]" % self.charge, 20, (255, 0, 0))
                self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                          "Cooldown: [%.1f]" % self.cooldown, 20, (255, 0, 0))
                self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20),
                                          "Damage factor: [%.1f]" % self.damage, 20, (255, 0, 0))
                self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 20), "Click [Yes or No] to return last page", 20,
                                          (0, 0, 0))

    def update_dictionary(self):
        self.dictionary['diameter'] = self.diameter
        self.dictionary['charge'] = self.charge
        self.dictionary['cooldown'] = self.cooldown
        self.dictionary['damage'] = self.damage
        self.dictionary['level'] = self.level
        self.dictionary['cost'] = self.cost
        self.dictionary['is brought'] = self.is_brought
        st.upgrades[self.name]['diameter'] = self.dictionary['diameter']
        st.upgrades[self.name]['charge'] = self.dictionary['charge']
        st.upgrades[self.name]['cooldown'] = self.dictionary['cooldown']
        st.upgrades[self.name]['damage'] = self.dictionary['damage']
        st.upgrades[self.name]['level'] = self.dictionary['level']
        st.upgrades[self.name]['cost'] = self.dictionary['cost']
        st.upgrades[self.name]['is brought'] = self.dictionary['is brought']
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()

    def reset_item(self):
        self.level = 0
        self.cooldown = 15
        self.diameter = st.player_width * 5
        self.charge = 2
        self.damage = 3 * st.item_att_attack_damage[1]
        self.cost = 2500
        self.brought = False
class Laser(Skill_item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.width = st.player_width
        self.damage = 6 * st.upgrades['Attack damage']['current']
        self.duation = 3
        self.cooldown = dictionary['cooldown']
        self.level = dictionary['level']
        self.max_level = 3
        self.cost = dictionary['cost']
        self.cost_interval = 7500
        self.is_brought = dictionary['is brought']
        super().__init__(self.name)
        self.update_text()

    def upgrade(self):
        if st.user_point >= self.cost:
            if self.level == 0:
                st.update_user_point(self.cost)
                self.is_brought = True
                self.level += 1
                self.cost +=  self.cost_interval
            elif self.level == 1:
                st.update_user_point(self.cost)
                self.level += 1
                self.cooldown = 35
                self.cost += self.cost_interval
            elif self.level == 2:
                st.update_user_point(self.cost)
                self.level += 1
                self.cooldown = 25
            self.update_text()
            self.update_dictionary()

    def detail_display(self, screen):
        if self.level < self.max_level:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            if not self.is_brought:
                self.text_4.draw(screen)
                self.text_5.draw(screen)
                self.text_6.draw(screen)
                self.text_7.draw(screen)
        else:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
            self.text_5.draw(screen)

    def update_text(self):
        if not self.is_brought:
            self.text_0 = screen.Text((self.x, self.y), "You have not brought this before", 30, (255, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 15), "Confirm to purchase [%s]?" % self.name, 30, (0, 0, 0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 15), "Width of laser: %d" % self.width, 20, (255, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 15), "Damage: %d" % self.damage, 20, (255, 0, 0))
            self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 15), "Duation: %d seconds" % self.duation, 20,(255, 0, 0))
            self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 15), "Cooldown: %d" % self.cooldown, 20,(255, 0, 0))
            self.text_6 = screen.Text((self.x, self.text_5.rect.bottom + 15), "Point required: %d" % self.cost, 20,
                                      (0, 0, 0))
            self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 15),"Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
        else:
            self.text_0 = screen.Text((self.x, self.y), "Confirm to upgrade [%s]?" % self.name,
                                      30, (0, 0, 0))
            self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Cooldown: %d" % self.cooldown, 20,
                                      (255, 0, 0))
            self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20), "Point required: %d" % self.cost, 20,
                                      (0, 0, 0))
            self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20),
                                      "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0, 0, 255))
            if not self.level < self.max_level:
                self.text_0 = screen.Text((self.x, self.y + 30), "You have reached the maximum level!", 30, (0, 0, 0))
                self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Width of laser: %d" % self.width, 20,
                                          (255, 0, 0))
                self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20),
                                          "Damage: %d" % self.damage, 20, (255, 0, 0))
                self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20), "Duation: %d seconds" % self.duation, 20, (255, 0, 0))
                self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Cooldown: %d seconds" % self.cooldown, 20,
                                          (255, 0, 0))
                self.text_5 = screen.Text((self.x, self.text_4.rect.bottom + 20), "Click [Yes or No] to return last page", 20,
                                          (0, 0, 0))

    def update_dictionary(self):
        self.dictionary['cooldown'] = self.cooldown
        self.dictionary['level'] = self.level
        self.dictionary['cost'] = self.cost
        self.dictionary['is brought'] = self.is_brought
        st.upgrades[self.name]['cooldown'] = self.dictionary['cooldown']
        st.upgrades[self.name]['level'] = self.dictionary['level']
        st.upgrades[self.name]['cost'] = self.dictionary['cost']
        st.upgrades[self.name]['is brought'] = self.dictionary['is brought']
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()
class Attribute(Item):
    def __init__(self, pos, dictionary):
        self.x = pos[0]
        self.y = pos[1]
        self.dictionary = dictionary
        self.name = dictionary['name']
        self.current = dictionary['current']
        self.default = dictionary['default']
        if self.name != 'Attack frequency':
            self.increase = dictionary['increase']
        else:
            self.increase = -dictionary['increase']
        self.cost_factor = 1000
        self.level = dictionary['level']
        self.max_level = 5
        self.base_cost = dictionary['base cost']
        self.cost = self.level * (self.base_cost + 500)
        self.update = self.current + self.increase

        # text
        self.update_text()
        super().__init__(self.name)

    def upgrade(self):
        if st.user_point >= self.cost:
            if self.level <= self.max_level:
                st.update_user_point(self.cost)
                self.current += self.increase
                self.level += 1
                self.cost = self.base_cost * self.level
                self.update = self.current + self.increase
                self.update_text()
                self.update_dictionary()

    def reset_item(self):
        self.current = self.default
        self.level = 1
        self.cost = self.base_cost

    def detail_display(self, screen):
        if self.level <= self.max_level:
            self.text_0.draw(screen)
            self.text_1.draw(screen)
            self.text_2.draw(screen)
            self.text_3.draw(screen)
            self.text_4.draw(screen)
        else:
            self.text_6.draw(screen)
            self.text_7.draw(screen)
            self.text_8.draw(screen)
    def update_text(self):
        self.text_0 = screen.Text((self.x, self.y), "Confirm to purchase [%s]?" % self.name, 30, (0,0,0))
        self.text_1 = screen.Text((self.x, self.text_0.rect.bottom + 20), "Current level: %d" % self.level, 20, (0,0,0))
        self.text_2 = screen.Text((self.x, self.text_1.rect.bottom + 20), "Upgrade from: %.1f --> %.1f" % (self.current,self.update), 20, (255,0,0))
        self.text_3 = screen.Text((self.x, self.text_2.rect.bottom + 20), "Point required: %d" % self.cost, 20, (0,0,0))
        self.text_4 = screen.Text((self.x, self.text_3.rect.bottom + 20), "Point left after purchase: %d" % (st.user_point - self.cost), 20, (0,0,255))

        self.text_6 = screen.Text((self.x, self.y + 30), "You have reached the maximum level!", 30, (0, 0, 0))
        self.text_7 = screen.Text((self.x, self.text_6.rect.bottom + 30), "Your [%s] value is [%.1f]" %(self.name, self.current), 20, (255, 0, 0))
        self.text_8 = screen.Text((self.x, self.text_7.rect.bottom + 30), "Click [Yes or No] to return last page", 20,
                                  (0, 0, 0))

    def update_dictionary(self):
        self.dictionary['current'] = self.current
        self.dictionary['level'] = self.level
        st.upgrades[self.name]['current'] = self.dictionary['current']
        st.upgrades[self.name]['level'] = self.dictionary['level']
        st.upgrades['User point']['point'] = st.user_point
        st.sound_shop_buy_item.play()
