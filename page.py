import pygame
from screen import *
from settings import Settings as st
from item import *
from level import *

class Page(object):

    # ----------initiate different screens-----------
    # menu
    screen_initialize_page = Screen("BG_mainmenu.png")
    screen_main = Screen("BG_button.png")
    screen_option = Screen("BG_button.png")
    screen_credit = Screen("BG_credit.png")
    screen_insaves = Screen("BG_button.png")
    screen_your_player = Screen("BG_credit.png")
    screen_setting = Screen("BG_button.png")
    screen_player_stats = Screen("BG_button.png")
    screen_start_difficulty = Screen("BG_button.png")
    screen_stage = Screen("BG_button.png")
    screen_start_confirm = Screen("BG_start_confirm.png")

    # gameplay
    screen_gameplay1 = Gameplay("BG_Map_1.png")
    screen_gameplay2 = Gameplay("BG_Map_2.png")
    screen_gameplay3 = Gameplay("BG_Map_3.png")
    screen_gameplay4 = Gameplay("BG_Map_4.png")
    screen_gameplay5 = Gameplay("BG_Map_5.png")
    screen_gameplay6 = Gameplay("BG_Map_6.png")
    screen_gameplay7 = Gameplay("BG_Map_7.png")
    screen_gameplay8 = Gameplay("BG_Map_8.png")
    screen_gameplay9 = Gameplay("BG_Map_9.png")
    screen_gameplay10 = Gameplay("BG_Map_10.png")
    screen_gameover = Animated_screen()

    # shop
    screen_shop = Screen("BG_button.png")
    screen_shop_skin = Screen("BG_button.png")
    screen_shop_shoot = Screen("BG_button.png")  # to be corrected
    screen_shop_skill = Screen("BG_button.png")  # to be corrected
    screen_shop_attribute = Screen("BG_button.png")
    screen_shop_skin_confirm = Screen("BG_button.png")
    screen_shop_shoot_confirm = Screen("BG_button.png")
    screen_shop_skill_confirm = Screen("BG_button.png")
    screen_shop_attribute_confirm = Screen("BG_button.png")

    # ------------------initiate different buttons------------------------
    #button_setting = Button(st.win_width / 2, 400, "button_setting.png")

    button_gameover = Button((st.win_width / 2, st.win_height * 1 / 5), (275,60), "button_gameover.png")
    button_complete = Button((st.win_width / 2, st.win_height * 1 / 5), (289,60), "button_complete.png")
    button_again = Button((st.win_width *1 / 4, st.win_height * 3 / 5), (120, 75), "button_again.png")
    button_menu = Button((st.win_width *3 / 4, st.win_height * 3 / 5), (120, 75), "button_menu.png")
    button_next = Button((st.win_width / 2, st.win_height * 4 / 5), (120, 75), "button_next.png")

    # initiate shop item (superclass) (current, default, increase, level, base_cost)
    # subclasses :>>
    # skin
    # shooting pattern
    # skill
    # attribute (current, default, increase, level, base_cost)


    def __init__(self, start_level, max_level, surface, create_level):
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level
        # select which page to display
        self.state = 'initialize_page'
        # initiate default difficulty
        self.selected_diff = 0
        # initiate default level
        self.level = 0
        self.level_win = False
        self.selected_level = None

        # initiate item
        self.item_chose = ""

    def initialize_page(self):
        run = True
        screen = Page.screen_initialize_page.screen
        text_0 = Text((400, 300), 'Press any key to start', 60, (0,0,0))
        while run:
            Page.screen_initialize_page.draw()
            text_0.draw(screen)
            for event in pygame.event.get():  # close the game
                if event.type == pygame.QUIT:
                    st.close_game()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    self.state = 'main'
                    st.bgm_mainmenu.play(loops=-1)
            pygame.display.update()
    def main(self):
        run = True
        screen = Page.screen_main.screen
        text_0 = Text((400, 190), 'Main Menu', 40, (0,0,0))
        button_save = Animated_button('save', 2, (st.win_width * 1/ 3, 300), (126, 75))
        button_credit = Animated_button('credit', 2, (st.win_width * 2 / 3, 300), (126, 75))
        button_setting = Animated_button('setting', 2, (st.win_width * 1 / 3, 450), (126, 75))
        button_quit = Animated_button('quit', 2, (st.win_width * 2 / 3, 450), (126, 75))
        while run:
            click = st.check_event()
            Page.screen_main.draw()
            text_0.draw(screen)
            button_save.draw(screen)
            button_credit.draw(screen)
            button_setting.draw(screen)
            button_quit.draw(screen)
            if button_save.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'insaves'
            if button_credit.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'credit'
            if button_setting.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'setting'
            if button_quit.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    st.sound_button_clicked.play()
                    st.close_game()
            pygame.display.update()
    def setting(self):
        run = True
        text_0 = Text((400, 190), 'Settings', 50, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 50), 'Main volume', 20, (0, 0, 0))
        main_volume = Volume_control((400, text_1.rect.bottom + 20), st.music_volume_bar_length, 20)
        text_2 = Text((400, main_volume.rect.bottom + 50), 'Background music volume', 20, (0, 0, 0))
        bgm_volume = Volume_control((400, text_2.rect.bottom + 20), st.music_volume_bar_length, 20)
        text_3 = Text((400, bgm_volume.rect.bottom + 50), 'Sound effect volume', 20, (0, 0, 0))
        effect_volume = Volume_control((400, text_3.rect.bottom + 20), st.music_volume_bar_length, 20)
        button_back = Animated_button('back', 2, (50, 575), (66, 40))
        main_volume.set_current_volume(st.main_volume_current)
        bgm_volume.set_current_volume(st.bgm_volume_current)
        effect_volume.set_current_volume(st.effect_volume_current)
        screen = Page.screen_insaves.screen
        st.sound_button_clicked.play()
        while run:
            click = st.check_event()
            Page.screen_insaves.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            text_3.draw(screen)
            main_volume.draw(screen)
            bgm_volume.draw(screen)
            effect_volume.draw(screen)
            button_back.draw(screen)
            if main_volume.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    main_volume.is_pressed()
            if main_volume.pressed:
                main_volume.pressed = st.check_volume_event()
                st.main_volume = main_volume.update()
                st.main_volume_current = main_volume.change_volume(st.get_mouse_pos())
                st.sound_volume_update()
            if bgm_volume.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    bgm_volume.is_pressed()
            if bgm_volume.pressed:
                bgm_volume.pressed = st.check_volume_event()
                st.bgm_volume = bgm_volume.update()
                st.bgm_volume_current = bgm_volume.change_volume(st.get_mouse_pos())
                st.sound_volume_update()
            if effect_volume.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    effect_volume.is_pressed()
            if effect_volume.pressed:
                effect_volume.pressed = st.check_volume_event()
                st.effect_volume = effect_volume.update()
                st.effect_volume_current = effect_volume.change_volume(st.get_mouse_pos())
                st.sound_volume_update()
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'main'
                    st.sound_button_clicked.play()
            pygame.display.update()
    def credit(self):
        run = True
        text_0 = Text((400, 190), 'Credit', 50, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 10), 'Reference', 25, (0, 0, 0))
        text_2 = Text((400, text_1.rect.bottom + 10), '1) Mattgriffi (2017) Bullet-hell-shooter [Source code]. https://github.com/mattgriffi/bullet-hell-shooter', 12, (0,0,0))
        text_3 = Text((400, text_2.rect.bottom + 10), '2) Clear Code. "Creating a health bar in pygame [Dark Souls style]." Youtube,Oct. 2, 2020 [Video file]. ', 12, (0,0,0))
        text_4 = Text((400, text_3.rect.bottom + 10), 'Available: https://www.youtube.com/watch?v=pUEZbUAMZYA&ab_channel=ClearCode. [Accessed: Apr. 13, 2022]', 12, (0,0,0))
        text_5 = Text((400, text_4.rect.bottom + 10), '3) Clear Code. "Creating an animated button in Pygame." Youtube, Jul. 4, 2021 [Video file]. ', 12, (0,0,0))
        text_6 = Text((400, text_5.rect.bottom + 10), 'Available: https://www.youtube.com/watch?v=8SzTzvrWaAA&t=1365s&ab_channel=ClearCode. [Accessed: Apr. 13, 2022]', 12, (0,0,0))
        text_7 = Text((400, text_6.rect.bottom + 30), 'Source of materials used', 25, (0,0,0))
        text_8 = Text((400, text_7.rect.bottom + 10), '1) Font: https://www.fontspace.com/haeres-letter-font-f53961', 12, (0,0,0))
        text_9 = Text((400, text_8.rect.bottom + 10), '2) xDeviruchi. 8-bit fantasy and adventure [music source]. https://xdeviruchi.itch.io/8-bit-fantasy-adventure-music-pack', 12, (0,0,0))
        text_10 = Text((400, text_9.rect.bottom + 10), '3) Sound: https://www.fesliyanstudios.com/sound-effects-search.php?q=throw', 12, (0,0,0))
        text_11 = Text((400, text_10.rect.bottom + 10), '          https://www.fesliyanstudios.com/sound-effects-search.php?q=coin', 12, (0,0,0))
        text_12 = Text((400, text_11.rect.bottom + 50), 'Final year project of PKPD, CL09, Group7, 2021-2022', 20, (0,0,0))
        text_13 = Text((400, text_12.rect.bottom + 10), 'Project supervisor: Mr. Tim Lau', 20, (0,0,0))

        button_back = Animated_button('back', 2, (50, 575), (66, 40))
        screen = Page.screen_credit.screen
        st.sound_button_clicked.play()
        while run:
            click = st.check_event()
            Page.screen_credit.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            text_3.draw(screen)
            text_4.draw(screen)
            text_5.draw(screen)
            text_6.draw(screen)
            text_7.draw(screen)
            text_8.draw(screen)
            text_9.draw(screen)
            text_10.draw(screen)
            text_11.draw(screen)
            text_12.draw(screen)
            text_13.draw(screen)
            button_back.draw(screen)
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'main'
                    st.sound_button_clicked.play()
            pygame.display.update()
    def insaves(self):
        run = True
        text_0 = Text((400, 190), 'Your Save', 30, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'Point own: %d' % st.user_point, 15, (0, 0, 0))
        button_starts = Animated_button('starts', 2, (st.win_width/2, 300), (126, 75))
        button_shop = Animated_button('shop', 2, (st.win_width/2, 400), (126, 75))
        button_your_player = Animated_button('your_player', 2, (st.win_width/2, 500), (126, 75))
        button_back = Animated_button('back', 2, (50, 575), (66,40))
        screen = Page.screen_insaves.screen
        st.sound_button_clicked.play()
        while run:
            click = st.check_event()
            Page.screen_insaves.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            button_starts.draw(screen)
            button_shop.draw(screen)
            button_your_player.draw(screen)
            button_back.draw(screen)
            if button_starts.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_level'
            if button_shop.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop'
                    st.bgm_mainmenu.stop()
                    st.bgm_shop.play(loops=-1)
            if button_your_player.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'your_player'
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'main'
                    st.sound_button_clicked.play()
            pygame.display.update()
    def your_player(self):
        run = True
        # background display
        text_0 = Text((300, 190), 'Your Player', 30, (0, 0, 0))
        text_1 = Text((60, 210), 'Category', 16, (0, 0, 0))
        inventary_rect = pygame.Rect((120, 177), (360, 411))
        detail_rect = pygame.Rect((480, 177), (304, 411))
        # category buttons
        button_skin = Animated_button('skin', 2, (60, 275), (80,50))
        button_pattern = Animated_button('pattern', 2, (60, button_skin.rect.bottom + 50), (80,50))
        button_skill = Animated_button('skill', 2, (60, button_pattern.rect.bottom + 50), (80,50))
        button_attribute = Animated_button('attribute', 2, (60, button_skill.rect.bottom + 50), (80,50))
        # skin items
        skin_list = []
        skin_list.append(Your_player_skin((210, 280), (80, 80), 'skin', 'green.png', (100, 30), st.upgrades['Skin'], 'green'))
        skin_list.append(Your_player_skin((390, 280), (80, 80), 'skin', 'orange.png', (100, 30), st.upgrades['Skin'], 'orange'))
        skin_list.append(Your_player_skin((210, 485), (80, 80), 'skin', 'red.png', (100, 30), st.upgrades['Skin'], 'red'))
        skin_list.append(Your_player_skin((390, 485), (80, 80), 'skin', 'yellow.png', (100, 30), st.upgrades['Skin'], 'yellow'))
        # pattern items
        pattern_list = []
        pattern_list.append(Your_player_pattern((210, 280), (80, 80), 'pattern', 'multi_shot.png', (100, 30), st.upgrades['Multi shot']))
        pattern_list.append(Your_player_pattern((390, 280), (80, 80), 'pattern', 'extra_bullet.png', (100, 30), st.upgrades['Bullet number']))
        # skill items
        skill_list =[]
        skill_list.append(Your_player_skill((210, 280), (80, 80), 'skill', 'barrier.png', (100, 30), st.upgrades['Barrier']))
        skill_list.append(Your_player_skill((390, 280), (80, 80), 'skill', 'dash.png', (100, 30), st.upgrades['Dash']))
        skill_list.append(Your_player_skill((210, 485), (80, 80), 'skill', 'grenade.png', (100, 30), st.upgrades['Grenade']))
        skill_list.append(Your_player_skill((390, 485), (80, 80), 'skill', 'laser.png', (100, 30), st.upgrades['Laser']))
        # attribute
        attribute_list = []
        attribute_list.append(Your_player_attribute((210, 280), (80, 80), 'attribute', 'attact_damage_upgrade.png', (100, 30), st.upgrades['Attack damage']))
        attribute_list.append(Your_player_attribute((390, 280), (80, 80), 'attribute', 'attact_frequency_upgrade.png', (100, 30), st.upgrades['Attack frequency']))
        attribute_list.append(Your_player_attribute((210, 485), (80, 80), 'attribute', 'attact_velocity_upgrade.png', (100, 30), st.upgrades['Bullet velocity']))
        attribute_list.append(Your_player_attribute((390, 485), (80, 80), 'attribute', 'health_upgrade.png', (100, 30), st.upgrades['Max health']))
        # others
        button_back = Animated_button('back', 2, (50, 575), (66, 40))
        screen = Page.screen_your_player.screen
        st.sound_button_clicked.play()
        item_display = ''
        item_detail_draw = None
        while run:
            click = st.check_event()
            Page.screen_your_player.draw()
            pygame.draw.rect(screen, (255, 178, 102), inventary_rect)
            pygame.draw.rect(screen, (153,255,153), detail_rect)
            button_back.draw(screen)
            text_0.draw(screen)
            text_1.draw(screen)
            button_skin.draw(screen)
            button_pattern.draw(screen)
            button_skill.draw(screen)
            button_attribute.draw(screen)
            if item_display == 'skin':
                for skin in skin_list:
                    skin.draw(screen)
                    text_0 = Text((300, 190), "Select skin", 30, (0, 0, 0))
                    if skin.button.top_rect.collidepoint(st.get_mouse_pos()):
                        if click:
                            skin.display_detail(screen)
                            item_detail_draw = skin
                            st.sound_button_clicked.play()
            elif item_display == 'pattern':
                for pattern in pattern_list:
                    pattern.draw(screen)
                    text_0 = Text((300, 190), "Select pattern", 30, (0, 0, 0))
                    if pattern.button.top_rect.collidepoint(st.get_mouse_pos()):
                        if click:
                            pattern.display_detail(screen)
                            item_detail_draw = pattern
                            st.sound_button_clicked.play()
            elif item_display == 'skill':
                for skill in skill_list:
                    skill.draw(screen)
                    text_0 = Text((300, 190), "Select skill", 30, (0, 0, 0))
                    if skill.button.top_rect.collidepoint(st.get_mouse_pos()):
                        if click:
                            skill.display_detail(screen)
                            item_detail_draw = skill
                            st.sound_button_clicked.play()
            elif item_display == 'attribute':
                for attribute in attribute_list:
                    attribute.draw(screen)
                    text_0 = Text((300, 190), "Select attribute", 30, (0, 0, 0))
                    if attribute.button.top_rect.collidepoint(st.get_mouse_pos()):
                        if click:
                            attribute.display_detail(screen)
                            item_detail_draw = attribute
                            st.sound_button_clicked.play()
            else:
                text_0 = Text((300, 190), 'Your Player', 30, (0, 0, 0))
            if button_skin.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    item_display = 'skin'
                    item_detail_draw = None
                    st.sound_button_clicked.play()
            if button_pattern.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    item_display = 'pattern'
                    item_detail_draw = None
                    st.sound_button_clicked.play()
            if button_skill.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    item_display = 'skill'
                    item_detail_draw = None
                    st.sound_button_clicked.play()
            if button_attribute.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    item_display = 'attribute'
                    item_detail_draw = None
                    st.sound_button_clicked.play()
            try:
                item_detail_draw.display_detail(screen)
            except:
                pass


            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'insaves'
            pygame.display.update()
    def start_level(self):
        run = True
        text_0 = Text((400, 190), 'Select a level', 30, (0, 0, 0))
        button_stage_1 = Button((st.win_width * 1 / 3, text_0.rect.bottom + 50), (54.8, 30), "button_stage_1.png")
        button_stage_2 = Button((st.win_width * 1 / 3, button_stage_1.rect.bottom + 40), (54.8, 30), "button_stage_2.png")
        button_stage_3 = Button((st.win_width * 1 / 3, button_stage_2.rect.bottom + 40), (54.8, 30), "button_stage_3.png")
        button_stage_4 = Button((st.win_width * 1 / 3, button_stage_3.rect.bottom + 40), (54.8, 30), "button_stage_4.png")
        button_stage_5 = Button((st.win_width * 1 / 3, button_stage_4.rect.bottom + 40), (54.8, 30), "button_stage_5.png")
        button_stage_6 = Button((st.win_width * 2 / 3, text_0.rect.bottom + 50), (54.8, 30), "button_stage_6.png")
        button_stage_7 = Button((st.win_width * 2 / 3, button_stage_6.rect.bottom + 40), (54.8, 30), "button_stage_7.png")
        button_stage_8 = Button((st.win_width * 2 / 3, button_stage_7.rect.bottom + 40), (54.8, 30), "button_stage_8.png")
        button_stage_9 = Button((st.win_width * 2 / 3, button_stage_8.rect.bottom + 40), (54.8, 30), "button_stage_9.png")
        button_stage_10 = Button((st.win_width * 2 / 3, button_stage_9.rect.bottom + 40), (54.8, 30), "button_stage_10.png")
        button_back = Animated_button('back', 2, (50, 575), (66, 40))
        screen = Page.screen_stage.screen
        st.sound_button_clicked.play()
        while run:
            click = st.check_event()
            Page.screen_stage.draw()
            text_0.draw(screen)
            button_stage_1.draw(screen)
            button_stage_2.draw(screen)
            button_stage_3.draw(screen)
            button_stage_4.draw(screen)
            button_stage_5.draw(screen)
            button_stage_6.draw(screen)
            button_stage_7.draw(screen)
            button_stage_8.draw(screen)
            button_stage_9.draw(screen)
            button_stage_10.draw(screen)
            button_back.draw(screen)
            if button_stage_1.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 1
            if button_stage_2.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 2

            if button_stage_3.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 3

            if button_stage_4.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 4

            if button_stage_5.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 5

            if button_stage_6.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 6

            if button_stage_7.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 7

            if button_stage_8.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 8

            if button_stage_9.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 9

            if button_stage_10.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
                    self.selected_level = 10
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'insaves'
            pygame.display.update()
    def start_difficulty(self):
        run = True
        text_0 = Text((400, 190), 'Select a difficulty', 30, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'Level selected: %d' % self.selected_level, 15, (255, 0, 0))
        button_easy = Animated_button('easy', 2, (400, text_1.rect.bottom + 50), (126, 75))
        button_normal = Animated_button('normal', 2, (400, button_easy.rect.bottom + 50), (126, 75))
        button_hard = Animated_button('hard', 2, (400, button_normal.rect.bottom + 50), (126, 75))
        button_back = Animated_button('back', 2, (50, 575), (66,40))
        screen = Page.screen_start_difficulty.screen
        st.sound_button_clicked.play()
        while run:
            click = st.check_event()
            Page.screen_insaves.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            button_easy.draw(screen)
            button_normal.draw(screen)
            button_hard.draw(screen)
            button_back.draw(screen)
            if button_easy.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'level_confirm'
                    self.selected_diff = 0
            if button_normal.rect.collidepoint(st.get_mouse_pos()):  # normal is clicked
                if click:
                    run = False
                    self.state = 'level_confirm'
                    self.selected_diff = 1
            if button_hard.rect.collidepoint(st.get_mouse_pos()):  # hard is clicked
                if click:
                    run = False
                    self.state = 'level_confirm'
                    self.selected_diff = 2
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_level'
            pygame.display.update()
    def level_confirm(self):
        run = True
        st.sound_button_clicked.play()
        text_0 = Text((400, 240), 'Are you ready?', 50, (255, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 50), 'Level: <%d>' % self.selected_level, 30, (255, 128, 0))
        text_2 = Text((400, text_1.rect.bottom + 20), 'Difficulty: <%s>' % st.menu_difficulty_blit(self.selected_diff), 30, (255, 255, 0))
        screen = Page.screen_start_confirm.screen
        button_yes = Animated_button('yes', 2, (200, text_2.rect.bottom + 100), (75, 135))
        button_no = Animated_button('no', 2, (600, text_2.rect.bottom + 100), (75, 135))
        while run:
            click = st.check_event()
            Page.screen_start_confirm.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            button_yes.draw(screen)
            button_no.draw(screen)
            if button_yes.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'gameplay'
                    st.sound_button_clicked.play()
                    st.bgm_mainmenu.stop()
            if button_no.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'start_difficulty'
            pygame.display.update()
    # gameplay screen
    def gameplay(self):
        run = True
        st.difficulty = self.selected_diff
        st.stage = self.selected_level
        if self.selected_level == 1:
            level = Level_1(Page.screen_gameplay1)
            st.bgm_s1.play(loops=-1)
        if self.selected_level == 2:
            level = Level_2(Page.screen_gameplay2)
            st.bgm_s2.play(loops=-1)
        if self.selected_level == 3:
            level = Level_3(Page.screen_gameplay3)
            st.bgm_s3.play(loops=-1)
        if self.selected_level == 4:
            level = Level_4(Page.screen_gameplay4)
            st.bgm_s4.play(loops=-1)
        if self.selected_level == 5:
            level = Level_5(Page.screen_gameplay5)
            st.bgm_s5.play(loops=-1)
        if self.selected_level == 6:
            level = Level_6(Page.screen_gameplay6)
            st.bgm_s6.play(loops=-1)
        if self.selected_level == 7:
            level = Level_7(Page.screen_gameplay7)
            st.bgm_s7.play(loops=-1)
        if self.selected_level == 8:
            level = Level_8(Page.screen_gameplay8)
            st.bgm_s8.play(loops=-1)
        if self.selected_level == 9:
            level = Level_9(Page.screen_gameplay9)
            st.bgm_s9.play(loops=-1)
        if self.selected_level == 10:
            level = Level_10(Page.screen_gameplay10)
            st.bgm_s10.play(loops=-1)
        st.gameplay_is_on = True

        while run:
            if level.game_status:
                self.level_win = level.run()
            else:
                level.game_status = True
                st.update_user_point_stage()
                st.point_earned = st.point
                st.set_point(0)
                st.gameplay_is_on = False
                self.state = 'gameover'
                break
            pygame.display.update()
    # gameover screen
    def gameover(self):
        run = True
        screen = Page.screen_gameover.screen
        Page.screen_gameover.is_win = self.level_win
        text_0 = Text((400, st.win_height * 2 / 5),'You have earned [%d] point!'%st.point_earned, 30, (0,0,0))
        text_1 = Text((400, text_0.rect.bottom + 20),'Point: [%d] --> [%d]'%
                      (st.user_point-st.point_earned,st.user_point), 30, (0,0,0))
        if self.level_win:
            st.bgm_mission_complete.play(loops=-1)
        else:
            st.bgm_gameover.play(loops=-1)
        while run:
            click = st.check_event()
            Page.screen_gameover.draw()
            Page.screen_gameover.change_state()
            if self.level_win:
                Page.button_complete.draw(screen)
                Page.button_menu.draw(screen)
                Page.button_again.draw(screen)
                Page.button_next.draw(screen)
                text_0.draw(screen)
                text_1.draw(screen)
                if Page.button_menu.rect.collidepoint(st.get_mouse_pos()):
                    if click:
                        run = False
                        self.state = 'main'
                        st.sound_button_clicked.play()
                        st.bgm_mainmenu.play(loops=-1)
                        st.bgm_gameover.stop()
                        st.bgm_mission_complete.stop()
                if Page.button_again.rect.collidepoint(st.get_mouse_pos()):
                    if click:
                        run = False
                        self.state = 'gameplay'
                        st.sound_button_clicked.play()
                        st.bgm_gameover.stop()
                        st.bgm_mission_complete.stop()
                if Page.button_next.rect.collidepoint(st.get_mouse_pos()):
                    if click:
                        run = False
                        self.state = 'gameplay'
                        if self.selected_level != st.total_level:
                            self.selected_level = self.selected_level + 1
                        st.sound_button_clicked.play()
                        st.bgm_gameover.stop()
                        st.bgm_mission_complete.stop()
            else:
                Page.button_gameover.draw(screen)
                Page.button_menu.draw(screen)
                Page.button_again.draw(screen)
                text_0.draw(screen)
                text_1.draw(screen)
                if Page.button_menu.rect.collidepoint(st.get_mouse_pos()):
                    if click:
                        run = False
                        self.state = 'main'
                        st.sound_button_clicked.play()
                        st.bgm_mainmenu.play(loops=-1)
                        st.bgm_gameover.stop()
                        st.bgm_mission_complete.stop()
                if Page.button_again.rect.collidepoint(st.get_mouse_pos()):
                    if click:
                        run = False
                        self.state = 'gameplay'
                        st.sound_button_clicked.play()
                        st.bgm_gameover.stop()
                        st.bgm_mission_complete.stop()
            pygame.display.update()
    # shop screen
    def shop(self):
        run = True
        st.sound_button_clicked.play()
        text_0 = Text((400, 190), 'Shop', 50, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'What do you want to buy?', 30, (0, 0, 0))
        text_2 = Text((400, text_1.rect.bottom + 20), 'Point own: %d' % st.user_point, 15, (0, 0, 0))
        button_skin = Animated_button('skin', 2, (200, text_2.rect.bottom + 40), (120,75))
        button_pattern = Animated_button('pattern', 2, (600, text_2.rect.bottom + 40), (120,75))
        button_skill = Animated_button('skill', 2, (200, button_skin.rect.bottom + 100), (120,75))
        button_attribute = Animated_button('attribute', 2, (600, button_skin.rect.bottom + 100), (120,75))
        button_back = Animated_button('back', 2, (50, 575), (66,40))
        screen = Page.screen_stage.screen
        while run:
            click = st.check_event()
            Page.screen_shop.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            button_skin.draw(screen)
            button_pattern.draw(screen)
            button_skill.draw(screen)
            button_attribute.draw(screen)
            button_back.draw(screen)
            if button_skin.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin'
            if button_pattern.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_shoot'
            if button_skill.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill'
            if button_attribute.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute'
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'insaves'
                    st.bgm_shop.stop()
                    st.bgm_mainmenu.play(loops=-1)
            pygame.display.update()
    # skin screen
    def shop_skin(self):
        run = True
        st.sound_button_clicked.play()
        text_0 = Text((395, 190), "Let's dress your player!", 30, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'Point own: %d' % st.user_point, 15, (0, 0, 0))
        text_2 = Text((250, text_0.y + 40), 'Green boy', 14, (0, 0, 0))
        text_3 = Text((540, text_0.y + 40), 'Orange boy', 14, (0, 0, 0))
        image_1 = Image((250, text_2.rect.bottom + 50), 100, 100, 'skin', 'green.png')
        image_2 = Image((540, text_3.rect.bottom + 50), 100, 100, 'skin', 'orange.png')
        button_buy1 = Button_text('Buy', (250, image_1.rect.bottom + 20), 150, 30)
        button_buy2 = Button_text('Buy', (540, image_2.rect.bottom + 20), 150, 30)
        text_4 = Text((250, button_buy1.top_rect.bottom + 40), 'Red boy', 14, (0, 0, 0))
        text_5 = Text((540, button_buy2.top_rect.bottom + 40), 'Yellow boy', 14, (0, 0, 0))
        image_3 = Image((250, text_4.rect.bottom + 50), 100, 100, 'skin', 'red.png')
        image_4 = Image((540, text_5.rect.bottom + 50), 100, 100, 'skin', 'yellow.png')
        button_buy3 = Button_text('Buy', (250, image_3.rect.bottom + 20), 150, 30)
        button_buy4 = Button_text('Buy', (540, image_4.rect.bottom + 20), 150, 30)
        button_back = Animated_button('back', 2, (50, 575), (66, 40))
        screen = Page.screen_shop_skin.screen
        while run:
            click = st.check_event()
            Page.screen_shop_skin.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            text_3.draw(screen)
            text_4.draw(screen)
            text_5.draw(screen)
            image_1.draw(screen)
            image_2.draw(screen)
            image_3.draw(screen)
            image_4.draw(screen)
            button_buy1.draw(screen)
            button_buy2.draw(screen)
            button_buy3.draw(screen)
            button_buy4.draw(screen)
            button_back.draw(screen)
            if button_buy1.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin_confirm'
                    self.item_chose = "item_skin_green"
            if button_buy2.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin_confirm'
                    self.item_chose = "item_skin_orange"
            if button_buy3.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin_confirm'
                    self.item_chose = "item_skin_red"
            if button_buy4.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin_confirm'
                    self.item_chose = "item_skin_yellow"
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop'
            pygame.display.update()
    # shooting pattern screen
    def shop_shoot(self):
        run = True
        st.sound_button_clicked.play()
        text_0 = Text((395, 190), "Upgrade your player's shooting form", 30, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'Point own: %d' % st.user_point, 15, (0, 0, 0))
        text_2 = Text((250, text_0.y + 40), 'Multi shooting', 14, (0, 0, 0))
        text_3 = Text((540, text_0.y + 40), 'Extra bullet', 14, (0, 0, 0))
        image_multi_shot = Image((250, text_2.rect.bottom + 50), 100, 100, 'pattern',
                                            'multi_shot.png')
        image_extra_bullet = Image((540, text_3.rect.bottom + 50), 100, 100, 'pattern',
                                               'extra_bullet.png')
        button_buy1 = Button_text('Buy', (250, image_multi_shot.rect.bottom + 20), 150, 30)
        button_buy2 = Button_text('Buy', (540, image_extra_bullet.rect.bottom + 20), 150, 30)
        button_back = Animated_button('back', 2, (50, 575), (66,40))
        screen = Page.screen_shop_skill.screen
        while run:
            click = st.check_event()
            Page.screen_shop_shoot.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            text_3.draw(screen)
            button_buy1.draw(screen)
            button_buy2.draw(screen)
            image_multi_shot.draw(screen)
            image_extra_bullet.draw(screen)
            button_back.draw(screen)
            if button_buy1.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_shoot_confirm'
                    self.item_chose = "item_pattern_multi_shot"
            if button_buy2.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_shoot_confirm'
                    self.item_chose = "item_pattern_bullet_number"
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop'
            pygame.display.update()
    # skill screen
    def shop_skill(self):
        run = True
        st.sound_button_clicked.play()
        text_0 = Text((395, 190), "Upgrade your player's skill", 30, (0, 0, 0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'Point own: %d' % st.user_point, 15, (0, 0, 0))
        text_2 = Text((250, text_0.y + 40), 'Barrier', 14, (0, 0, 0))
        text_3 = Text((540, text_0.y + 40), 'Dash', 14, (0, 0, 0))
        image_barrier = Image((250, text_2.rect.bottom + 50), 100, 100, 'skill', 'barrier.png')
        image_dash = Image((540, text_3.rect.bottom + 50), 100, 100, 'skill', 'dash.png')
        button_buy1 = Button_text('Buy', (250, image_barrier.rect.bottom + 20), 150, 30)
        button_buy2 = Button_text('Buy', (540, image_dash.rect.bottom + 20), 150, 30)
        text_4 = Text((250, button_buy1.top_rect.bottom + 40), 'Grenade', 14, (0, 0, 0))
        text_5 = Text((540, button_buy2.top_rect.bottom + 40), 'Laser', 14, (0, 0, 0))
        image_grenade = Image((250, text_4.rect.bottom + 50), 100, 100, 'skill', 'grenade.png')
        image_laser = Image((540, text_5.rect.bottom + 50), 100, 100, 'skill', 'laser.png')
        button_buy3 = Button_text('Buy', (250, image_grenade.rect.bottom + 20), 150, 30)
        button_buy4 = Button_text('Buy', (540, image_laser.rect.bottom + 20), 150, 30)
        screen = Page.screen_shop_skill.screen
        button_back = Animated_button('back', 2, (50, 575), (66,40))
        while run:
            click = st.check_event()
            Page.screen_shop_skill.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            text_3.draw(screen)
            text_4.draw(screen)
            text_5.draw(screen)
            image_barrier.draw(screen)
            image_dash.draw(screen)
            image_grenade.draw(screen)
            image_laser.draw(screen)
            button_buy1.draw(screen)
            button_buy2.draw(screen)
            button_buy3.draw(screen)
            button_buy4.draw(screen)
            button_back.draw(screen)
            if button_buy1.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill_confirm'
                    self.item_chose = "item_skill_barrier"
            if button_buy2.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill_confirm'
                    self.item_chose = "item_skill_dash"
            if button_buy3.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill_confirm'
                    self.item_chose = "item_skill_grenade"
            if button_buy4.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill_confirm'
                    self.item_chose = "item_skill_laser"
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop'
            pygame.display.update()
    # attribute screen
    def shop_attribute(self):
        st.sound_button_clicked.play()
        text_0 = Text((395, 190), "Upgrade your player's attribute", 30, (0,0,0))
        text_1 = Text((400, text_0.rect.bottom + 20), 'Point own: %d' % st.user_point, 15, (0, 0, 0))
        text_2 = Text((250, text_0.y + 40), 'Attack damage', 14, (0,0,0))
        text_3 = Text((540, text_0.y + 40), 'Attack frequency', 14, (0,0,0))
        image_attack_damage_upgrade = Image((250, text_2.rect.bottom + 50), 100, 100, 'attribute', 'attact_damage_upgrade.png')
        image_attack_frequency_upgrade = Image((540, text_3.rect.bottom + 50), 100, 100, 'attribute', 'attact_frequency_upgrade.png')
        button_buy1 = Button_text('Buy', (250, image_attack_damage_upgrade.rect.bottom+20), 150, 30)
        button_buy2 = Button_text('Buy', (540, image_attack_frequency_upgrade.rect.bottom+20), 150, 30)
        text_4 = Text((250, button_buy1.top_rect.bottom + 40), 'Bullet velocity', 14, (0, 0, 0))
        text_5 = Text((540, button_buy2.top_rect.bottom + 40), 'Max health', 14, (0, 0, 0))
        image_attack_velocity_upgrade = Image((250, text_4.rect.bottom + 50), 100, 100, 'attribute', 'attact_velocity_upgrade.png')
        image_health_upgrade = Image((540, text_5.rect.bottom + 50), 100, 100, 'attribute', 'health_upgrade.png')
        button_buy3 = Button_text('Buy', (250, image_attack_velocity_upgrade.rect.bottom+20), 150, 30)
        button_buy4 = Button_text('Buy', (540, image_health_upgrade.rect.bottom+20), 150, 30)
        button_back = Animated_button('back', 2, (50, 575), (66,40))
        screen = Page.screen_shop_attribute.screen
        run = True
        while run:
            click = st.check_event()
            Page.screen_shop_attribute.draw()
            text_0.draw(screen)
            text_1.draw(screen)
            text_2.draw(screen)
            text_3.draw(screen)
            text_4.draw(screen)
            text_5.draw(screen)
            button_buy1.draw(screen)
            button_buy2.draw(screen)
            button_buy3.draw(screen)
            button_buy4.draw(screen)
            button_back.draw(screen)
            image_attack_damage_upgrade.draw(screen)
            image_attack_velocity_upgrade.draw(screen)
            image_attack_frequency_upgrade.draw(screen)
            image_health_upgrade.draw(screen)
            if button_buy1.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute_confirm'
                    self.item_chose = "item_att_attack_damage"
            if button_buy2.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute_confirm'
                    self.item_chose = "item_att_attack_frequency"
            if button_buy3.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute_confirm'
                    self.item_chose = "item_att_attack_velocity"
            if button_buy4.top_rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute_confirm'
                    self.item_chose = "item_att_health"
            if button_back.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop'
            pygame.display.update()
    # skin buy confirmation screen
    def shop_skin_confirm(self):
        run = True
        st.sound_button_clicked.play()
        screen = Page.screen_shop_skin_confirm.screen
        self.item_skin_red = Skin((400, 200), st.upgrades['Skin'])
        self.item_skin_green = Skin((400, 200), st.upgrades['Skin'])
        self.item_skin_orange = Skin((400, 200), st.upgrades['Skin'])
        self.item_skin_yellow = Skin((400, 200), st.upgrades['Skin'])
        self.item_skin_red.check_if_skin_is_brought('red')
        self.item_skin_green.check_if_skin_is_brought('green')
        self.item_skin_orange.check_if_skin_is_brought('orange')
        self.item_skin_yellow.check_if_skin_is_brought('yellow')
        button_yes = Animated_button('yes', 2, (550, 500), (50, 84.6))
        button_no = Animated_button('no', 2, (625, 500), (50, 84.6))
        while run:
            click = st.check_event()
            Page.screen_shop_skin_confirm.draw()
            button_yes.draw(screen)
            button_no.draw(screen)
            self.shop_item_manager().detail_display(screen)
            if button_yes.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin'
                    self.shop_item_manager().upgrade()
            if button_no.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skin'
            pygame.display.update()
    # shooting pattern buy confirmation screen
    def shop_shoot_confirm(self):
        run = True
        st.sound_button_clicked.play()
        screen = Page.screen_shop_shoot_confirm.screen
        self.item_pattern_multi_shot = Pattern((400, 200), st.upgrades['Multi shot'])
        self.item_pattern_bullet_number = Pattern((400, 200), st.upgrades['Bullet number'])
        button_yes = Animated_button('yes', 2, (550, 500), (60, 101.52))
        button_no = Animated_button('no', 2, (625, 500), (60, 101.52))
        while run:
            click = st.check_event()
            Page.screen_shop_shoot_confirm.draw()
            button_yes.draw(screen)
            button_no.draw(screen)
            self.shop_item_manager().detail_display(screen)
            if button_yes.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_shoot'
                    self.shop_item_manager().upgrade()
            if button_no.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_shoot'
            pygame.display.update()
    # skill buy confirmation screen
    def shop_skill_confirm(self):
        run = True
        st.sound_button_clicked.play()
        self.item_skill_barrier = Barrier((400, 200), st.upgrades['Barrier'])
        self.item_skill_dash = Dash((400, 200), st.upgrades['Dash'])
        self.item_skill_grenade = Grenade((400, 200), st.upgrades['Grenade'])
        self.item_skill_laser = Laser((400, 200), st.upgrades['Laser'])
        button_yes = Animated_button('yes', 2, (550, 500), (60, 101.52))
        button_no = Animated_button('no', 2, (625, 500), (60, 101.52))
        screen = Page.screen_shop_skill_confirm.screen
        while run:
            click = st.check_event()
            Page.screen_shop_skill_confirm.draw()
            button_yes.draw(screen)
            button_no.draw(screen)
            self.shop_item_manager().detail_display(screen)
            if button_yes.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill'
                    self.shop_item_manager().upgrade()
            if button_no.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_skill'
            pygame.display.update()
    # attribute buy confirmation screen
    def shop_attribute_confirm(self):
        run = True
        st.sound_button_clicked.play()
        self.item_att_attack_damage = Attribute((400, 200), st.upgrades['Attack damage'])
        self.item_att_attack_frequency = Attribute((400, 200), st.upgrades['Attack frequency'])
        self.item_att_attack_velocity = Attribute((400, 200), st.upgrades['Bullet velocity'])
        self.item_att_health = Attribute((400, 200), st.upgrades['Max health'])
        button_yes = Animated_button('yes', 2, (550, 500), (60, 101.52))
        button_no = Animated_button('no', 2, (625, 500), (60, 101.52))
        screen = Page.screen_shop_attribute_confirm.screen
        while run:
            click = st.check_event()
            Page.screen_shop_attribute_confirm.draw()
            button_yes.draw(screen)
            button_no.draw(screen)
            self.shop_item_manager().detail_display(screen)
            if button_yes.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute'
                    self.shop_item_manager().upgrade()
            if button_no.rect.collidepoint(st.get_mouse_pos()):
                if click:
                    run = False
                    self.state = 'shop_attribute'
            pygame.display.update()
    def page_manager(self):
        if self.state == 'initialize_page':
            self.initialize_page()
        elif self.state == 'main':
            self.main()
        elif self.state == 'insaves':
            self.insaves()
        elif self.state == 'setting':
            self.setting()
        elif self.state == 'credit':
            self.credit()
        elif self.state == 'start_difficulty':
            self.start_difficulty()
        elif self.state == 'your_player':
            self.your_player()
        elif self.state == 'start_level':
            self.start_level()
        elif self.state == 'level_confirm':
            self.level_confirm()
        elif self.state == 'gameplay':
            self.gameplay()
        elif self.state == 'gameover':
            self.gameover()
        elif self.state == 'shop':
            self.shop()
        elif self.state == 'shop_skin':
            self.shop_skin()
        elif self.state == 'shop_shoot':
            self.shop_shoot()
        elif self.state == 'shop_skill':
            self.shop_skill()
        elif self.state == 'shop_attribute':
            self.shop_attribute()
        elif self.state == 'shop_skin_confirm':
            self.shop_skin_confirm()
        elif self.state == 'shop_shoot_confirm':
            self.shop_shoot_confirm()
        elif self.state == 'shop_skill_confirm':
            self.shop_skill_confirm()
        elif self.state == 'shop_attribute_confirm':
            self.shop_attribute_confirm()
    def shop_item_manager(self):
        # skin
        if self.item_chose == "item_skin_red":
            return self.item_skin_red
        elif self.item_chose == "item_skin_green":
            return self.item_skin_green
        elif self.item_chose == "item_skin_orange":
            return self.item_skin_orange
        elif self.item_chose == "item_skin_yellow":
            return self.item_skin_yellow
        # shooting pattern
        elif self.item_chose == "item_pattern_multi_shot":
            return self.item_pattern_multi_shot
        elif self.item_chose == "item_pattern_bullet_number":
            return self.item_pattern_bullet_number
        # skill
        elif self.item_chose == "item_skill_dash":
            return self.item_skill_dash
        elif self.item_chose == "item_skill_barrier":
            return self.item_skill_barrier
        elif self.item_chose == "item_skill_grenade":
            return self.item_skill_grenade
        elif self.item_chose == "item_skill_laser":
            return self.item_skill_laser
        # attribute
        elif self.item_chose == "item_att_health":
            return self.item_att_health
        elif self.item_chose == "item_att_attack_damage":
            return self.item_att_attack_damage
        elif self.item_chose == "item_att_attack_frequency":
            return self.item_att_attack_frequency
        elif self.item_chose == "item_att_attack_velocity":
            return self.item_att_attack_velocity
    def run(self):
        self.page_manager()