import sys
import pygame
from pygame.locals import *
import os, time

class InteractionButton:
    def __init__(self):
        self.window_surface = pygame.display.set_mode((1340, 720))
        self.inventory_background, self.inventory_background_x, self.inventory_background_y = 'images/7_inventory_obj/inventory_background.png', 0, 0
        self.inventory_main, self.inventory_main_x, self.inventory_main_y = 'images/7_inventory_obj/inventory_main.png', 132,63

        self.x_button, self.x_button_x, self.x_button_y = 'images/5_book_obj/x_button.png', 1180, 76
        self.x_button_width, self.x_button_height = 104, 104
        self.back_button, self.back_button_x, self.back_button_y = 'images/4_interaction_obj/back_button.png', 20, 626
        self.back_button_width, self.back_button_height = 80, 8

        self.chur, self.chur_x, self.chur_y = 'images/7_inventory_obj/chur.png', 253, 259
        self.chur_button_x, self.chur_button_y, self.chur_button_width, self.chur_button_height = 253, 491, 234, 73

        self.fishing_rod, self.fishing_rod_x, self.fishing_rod_y = 'images/7_inventory_obj/fishing_rod.png', 253, 259
        self.fishing_rod_button_x, self.fishing_rod_button_y, self.fishing_rod_button_width, self.fishing_rod_button_height = 253, 491, 234, 73

        self.mouse_cursor = 'images/999_ect/cat_cursor.png'
        pygame.mouse.set_visible(False)

    def background_music(self, mp3_file='sounds/cat_interaction.ogg'):
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def feed_chur(self, file_dir='images/4_interaction_obj/feed_chur', mp3_file='sounds/interaction_start.ogg'):
        img_names = os.listdir(file_dir)
        all_imgs = {}
        self.background_music(mp3_file)
        for i, img in enumerate(img_names):
            all_imgs[img] = pygame.image.load('{}/{}'.format(file_dir, img))
            self.window_surface.blit(all_imgs[img], (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)

    def play_fishing_rod(self, file_dir='images/4_interaction_obj/play_fishing_rod'):
        img_names = os.listdir(file_dir)
        all_imgs = {}
        for i, img in enumerate(img_names):
            all_imgs[img] = pygame.image.load('{}/{}'.format(file_dir, img))
            self.window_surface.blit(all_imgs[img], (0, 0))
            pygame.time.delay(1000)
            pygame.display.update()

    def show_feed_inventory(self):
        inventory_obj_list = {}
        inventory_obj_list['background'] = pygame.image.load(self.inventory_background), (self.inventory_background_x, self.inventory_background_y)
        inventory_obj_list['inventory_main'] = pygame.image.load(self.inventory_main), (self.inventory_main_x, self.inventory_main_y)
        inventory_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        inventory_obj_list['chur'] = pygame.image.load(self.chur), (self.chur_x, self.chur_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                inventory_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in inventory_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width) and \
                        (self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.chur_button_x <= mouse_x <= self.chur_button_x+self.chur_button_width) and \
                        (self.chur_button_y <= mouse_y <= self.chur_button_y+self.chur_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.feed_chur()
                        no_event = False

    def show_play_inventory(self):
        inventory_obj_list = {}
        inventory_obj_list['background'] = pygame.image.load(self.inventory_background), (self.inventory_background_x, self.inventory_background_y)
        inventory_obj_list['inventory_main'] = pygame.image.load(self.inventory_main), (self.inventory_main_x, self.inventory_main_y)
        inventory_obj_list['back_button'] = pygame.image.load(self.back_button), (self.back_button_x, self.back_button_y)
        inventory_obj_list['fishing_rod'] = pygame.image.load(self.fishing_rod), (self.fishing_rod_x, self.fishing_rod_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                inventory_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in inventory_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.back_button_x <= mouse_x <= self.back_button_x+self.back_button_width) and \
                        (self.back_button_y <= mouse_y <= self.back_button_y+self.back_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.fishing_rod_button_x <= mouse_x <= self.fishing_rod_button_x+self.fishing_rod_button_width) and \
                        (self.fishing_rod_button_y <= mouse_y <= self.fishing_rod_button_y+self.fishing_rod_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.play_fishing_rod()
                        no_event = False
