from catbook import Catbook
from shop import Shop
from coin import Coin
from ending import Ending
from interaction_button import InteractionButton

import sys, os, time
import pygame
from pygame.locals import *

class Interaction:
    def __init__(self, cat='kakku'):
        self.obj_list = {}
        self.window_surface = pygame.display.set_mode((1340, 720))

        self.background, self.background_x, self.background_y = 'images/4_interaction_obj/background_cat/interaction_background.png', 0, 0
        self.cat_background, self.cat_background_x , self.cat_background_y = 'images/4_interaction_obj/background_cat/{}_background.png'.format(cat), 684, 159
        self.cat, self.cat_x, self.cat_y = 'images/4_interaction_obj/background_cat/kakku.png',711, 77
        self.cat_closed_eye, self.cat_closed_eye_x, self.cat_closed_eye_y = 'images/4_interaction_obj/background_cat/kakku_closed_eye.png', 711, 77

        self.catbook, self.catbook_x, self.catbook_y = 'images/4_interaction_obj/book.png', 2,19
        self.catbook_width, self.catbook_height = 102, 72
        self.shop, self.shop_x, self.shop_y = 'images/4_interaction_obj/shop.png', 100, 31
        self.shop_width, self.shop_height = 53, 46

        self.coin_20, self.coin_100 = 'images/4_interaction_obj/coin_20.png', 'images/4_interaction_obj/coin_100.png'
        self.coin_480, self.coin_520 = 'images/4_interaction_obj/coin_480.png', 'images/4_interaction_obj/coin_520.png'
        self.coin_x, self.coin_y, self.coin_width, self.coin_height = 1065, 34, 143, 43
        self.inventory, self.inventory_x, self.inventory_y = 'images/4_interaction_obj/inventory.png', 1219, 19

        self.affection, self.affection_x, self.affection_y = 'images/4_interaction_obj/affection.png', 26, 115
        self.affection_increase = 'images/4_interaction_obj/affection_increase.png'
        self.affection_increase_2 = 'images/4_interaction_obj/affection_increase_2.png'

        self.chat, self.chat_x, self.chat_y = 'images/4_interaction_obj/chat.png', 170, 497
        self.chat_after_chur = 'images/4_interaction_obj/chat_after_chur.png'
        self.chat_after_fishing_rod = 'images/4_interaction_obj/chat_after_fishing_rod.png'

        self.chat_button, self.chat_button_x, self.chat_button_y = 'images/4_interaction_obj/button/chat_button.png', 182, 518
        self.feed_button, self.feed_button_x, self.feed_button_y = 'images/4_interaction_obj/button/feed_button.png', 442, 518
        self.pat_button, self.pat_button_x, self.pat_button_y = 'images/4_interaction_obj/button/pat_button.png', 700, 518
        self.play_button, self.play_button_x, self.play_button_y = 'images/4_interaction_obj/button/play_button.png', 965, 518
        self.back_button, self.back_button_x, self.back_button_y = 'images/4_interaction_obj/back_button.png', 20, 626
        self.interaction_button_width, self.interaction_button_height = 197, 173
        self.back_button_width, self.back_button_height = 80, 80

        self.show_catbook = Catbook()
        self.show_shop = Shop()
        self.show_coin = Coin()
        self.show_ending = Ending()
        self.show_interaction = InteractionButton()

        self.coin_amount = '100'
        self.mouse_cursor = 'images/999_ect/cat_cursor.png'
        pygame.mouse.set_visible(False)

    def background_music(self, mp3_file='sounds/cat_interaction.ogg'):
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def remove_obj(self, obj_name):
        del self.obj_list[obj_name]
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

    def basic_show(self):
        self.background_music()
        self.obj_list['background'] = pygame.image.load(self.background), (self.background_x, self.background_y)
        self.obj_list['cat_background'] = pygame.image.load(self.cat_background), (self.cat_background_x, self.cat_background_y)
        self.obj_list['cat'] = pygame.image.load(self.cat), (self.cat_x, self.cat_y)

        self.obj_list['catbook'] = pygame.image.load(self.catbook), (self.catbook_x, self.catbook_y)
        self.obj_list['shop'] = pygame.image.load(self.shop), (self.shop_x, self.shop_y)
        self.obj_list['inventory'] = pygame.image.load(self.inventory), (self.inventory_x, self.inventory_y)
        self.obj_list['affection'] = pygame.image.load(self.affection), (self.affection_x, self.affection_y)
        self.obj_list['coin'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)

        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

    def chat_show(self):
        pygame.time.delay(1000)
        self.obj_list['chat'] = pygame.image.load(self.chat), (self.chat_x, self.chat_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        pygame.time.delay(1000)
        self.remove_obj('chat')
        pygame.time.delay(500)

    def chur_affection_update(self):
        self.obj_list['background'] = pygame.image.load(self.background), (self.background_x, self.background_y)
        self.obj_list['cat_background'] = pygame.image.load(self.cat_background), (
        self.cat_background_x, self.cat_background_y)
        self.obj_list['cat'] = pygame.image.load(self.cat_closed_eye), (self.cat_closed_eye_x, self.cat_closed_eye_y)

        self.obj_list['catbook'] = pygame.image.load(self.catbook), (self.catbook_x, self.catbook_y)
        self.obj_list['shop'] = pygame.image.load(self.shop), (self.shop_x, self.shop_y)
        self.obj_list['inventory'] = pygame.image.load(self.inventory), (self.inventory_x, self.inventory_y)
        self.obj_list['affection'] = pygame.image.load(self.affection_increase), (self.affection_x, self.affection_y)
        self.obj_list['coin'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
        pygame.time.delay(500)
        self.obj_list['chat'] = pygame.image.load(self.chat_after_chur), (self.chat_x, self.chat_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        pygame.time.delay(1000)
        self.remove_obj('chat')
        self.obj_list['cat'] = pygame.image.load(self.cat), (self.cat_x, self.cat_y)
        pygame.time.delay(500)

    def fishing_rod_affection_update(self):
        self.obj_list['background'] = pygame.image.load(self.background), (self.background_x, self.background_y)
        self.obj_list['cat_background'] = pygame.image.load(self.cat_background), (
        self.cat_background_x, self.cat_background_y)
        self.obj_list['cat'] = pygame.image.load(self.cat_closed_eye), (self.cat_closed_eye_x, self.cat_closed_eye_y)

        self.obj_list['catbook'] = pygame.image.load(self.catbook), (self.catbook_x, self.catbook_y)
        self.obj_list['shop'] = pygame.image.load(self.shop), (self.shop_x, self.shop_y)
        self.obj_list['inventory'] = pygame.image.load(self.inventory), (self.inventory_x, self.inventory_y)
        self.obj_list['affection'] = pygame.image.load(self.affection_increase_2), (self.affection_x, self.affection_y)
        self.obj_list['coin'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
        pygame.time.delay(500)
        self.obj_list['chat'] = pygame.image.load(self.chat_after_fishing_rod), (self.chat_x, self.chat_y)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        pygame.time.delay(1000)
        self.remove_obj('chat')
        self.obj_list['cat'] = pygame.image.load(self.cat), (self.cat_x, self.cat_y)
        pygame.time.delay(500)

    def interaction_choice(self):
        self.obj_list['chat_button'] = pygame.image.load(self.chat_button), (self.chat_button_x, self.chat_button_y)
        self.obj_list['feed_button'] = pygame.image.load(self.feed_button), (self.feed_button_x, self.feed_button_y)
        self.obj_list['pat_button'] = pygame.image.load(self.pat_button), (self.pat_button_x, self.pat_button_y)
        self.obj_list['play_button'] = pygame.image.load(self.play_button), (self.play_button_x, self.play_button_y)
        self.obj_list['back_button'] = pygame.image.load(self.back_button), (self.back_button_x, self.back_button_y)
        no_event = True
        while no_event:
            if self.coin_amount == '20':
                self.obj_list['coin'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
            if self.coin_amount == '100':
                self.obj_list['coin'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
            if self.coin_amount == '480':
                self.obj_list['coin'] = pygame.image.load(self.coin_480), (self.coin_x, self.coin_y)
            if self.coin_amount == '520':
                self.obj_list['coin'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in self.obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # start chat
                    if (self.chat_button_x <= mouse_x <= self.chat_button_x+self.interaction_button_width) and \
                            (self.chat_button_y <= mouse_y <= self.chat_button_y + self.interaction_button_height):
                        self.interaction_choice()

                    # start feed
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (self.feed_button_x <= mouse_x <= self.feed_button_x + self.interaction_button_width) and \
                                (self.feed_button_y <= mouse_y <= self.feed_button_y + self.interaction_button_height):
                            no_event = False
                            self.show_interaction.show_feed_inventory()
                            self.chur_affection_update()
                            self.obj_list['affection'] = pygame.image.load(self.affection_increase), (self.affection_x, self.affection_y)
                            self.interaction_choice()

                    # start pat
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (self.pat_button_x <= mouse_x <= self.pat_button_x + self.interaction_button_width) and \
                                (self.pat_button_y <= mouse_y <= self.pat_button_y + self.interaction_button_height):
                            self.interaction_choice()

                    # start play
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (self.play_button_x <= mouse_x <= self.play_button_x + self.interaction_button_width) and \
                                (self.play_button_y <= mouse_y <= self.play_button_y + self.interaction_button_height):
                            no_event = False
                            self.show_interaction.show_play_inventory()
                            self.fishing_rod_affection_update()
                            self.obj_list['affection'] = pygame.image.load(self.affection_increase_2), (self.affection_x, self.affection_y)
                            self.interaction_choice()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (self.back_button_x <= mouse_x <= self.back_button_x + self.back_button_width) and \
                                (self.back_button_y <= mouse_y <= self.back_button_y + self.back_button_height):
                            no_event = False
                            self.show_ending.ending_movie()

                    # show catbook
                    if (self.catbook_x <= mouse_x <= self.catbook_x + self.catbook_width) \
                            and (self.catbook_y <= mouse_y <= self.catbook_y + self.catbook_height):
                        self.show_catbook.show_catbook()

                    # show shop
                    if (self.shop_x <= mouse_x <= self.shop_x + self.shop_width) \
                            and (self.shop_y <= mouse_y <= self.shop_y + self.shop_height):
                        self.show_shop.coin_amount = self.coin_amount
                        self.show_shop.show_food()
                        self.coin_amount = self.show_shop.coin_amount

                    # show coin shop
                    if (self.coin_x <= mouse_x <= self.coin_x+self.coin_width) and \
                            (self.coin_y <= mouse_y <= self.coin_y+self.coin_height):
                        self.show_coin.show_coin()
                        if self.show_coin.coin_amount == '20':
                            self.coin_amount = '20'
                        if self.show_coin.coin_amount == '520':
                            self.coin_amount = '520'
                        pygame.display.update()
                        self.interaction_choice()
