import pygame, time, sys

from page import Page
from level import Level
from settings import Settings as st


class Game:
    def __init__(self):

        # game initial attribute
        self.max_level = st.max_level

        # manu creation
        self.manu = Page(0, self.max_level, window, self.create_level)
        self.status = 'initialize_page'

    def create_level(self, current_level):
        self.level = Level(current_level)
        self.status = 'level'

    def create_manu(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.status = 'initialize_page'
        # ... to be finished
        # update unlocked level

    def run(self):
        if self.status == 'initialize_page':
            self.manu.run()

# pygame setup
pygame.init()
window = pygame.display.set_mode((st.win_width, st.win_height))
clock = pygame.time.Clock()
game = Game()
icon = pygame.image.load('assets/images/ui/icon.png').convert_alpha()
pygame.display.set_caption("Hunt Horizon")
pygame.display.set_icon(icon)
fps = 60
st.import_music()


# game loop
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill('black')
    game.run()
    pygame.display.update()