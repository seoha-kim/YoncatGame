import sys
import pygame
from pygame.locals import *

class Coin:
    def __init__(self):
        self.window_surface = pygame.display.set_mode((1340, 720))
        self.coin_background, self.coin_background_x, self.coin_background_y = 'images/8_coin_obj/coin_background.png', 0, 0
        self.coin_main, self.coin_main_x, self.coin_main_y = 'images/8_coin_obj/buy_coin.png', 131,106
        self.coin_buy_x, self.coin_buy_y, self.coin_buy_width, self.coin_buy_height = 553, 488, 234, 73
        self.coin_20, self.coin_520= 'images/8_coin_obj/coin_20.png', 'images/8_coin_obj/coin_520.png'
        self.coin_amount, self.coin_x, self.coin_y = '20', 999, 174

        self.x_button, self.x_button_x, self.x_button_y = 'images/8_coin_obj/x_button.png', 1180, 76
        self.x_button_width, self.x_button_height = 104, 104

        self.popup, self.popup_x, self.popup_y = 'images/8_coin_obj/pop_up.png', 321, 58
        self.popup_x_button_x, self.popup_x_button_y, self.popup_x_button_width, self.popup_x_button_height = 889, 203, 72, 72
        self.popup_yes_x, self.popup_yes_y, self.popup_yes_width, self.popup_yes_height = 584, 531, 180, 87

        self.mouse_cursor = 'images/999_ect/cat_cursor.png'
        pygame.mouse.set_visible(False)

    def show_popup(self):
        coin_obj_list = {}
        coin_obj_list['background'] = pygame.image.load(self.coin_background), (self.coin_background_x, self.coin_background_y)
        coin_obj_list['coin_main'] = pygame.image.load(self.coin_main), (self.coin_main_x, self.coin_main_y)
        coin_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        coin_obj_list['popup'] = pygame.image.load(self.popup), (self.popup_x, self.popup_y)
        if self.coin_amount=='20':
            coin_obj_list['coin'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
        elif self.coin_amount=='520':
            coin_obj_list['coin'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)

        for obj, (x, y) in coin_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                coin_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in coin_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.popup_x_button_x <= mouse_x <= self.popup_x_button_x+self.popup_x_button_width) and \
                        (self.popup_x_button_y <= mouse_y <= self.popup_x_button_y + self.popup_x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.show_coin()

                if (self.popup_yes_x <= mouse_x <= self.popup_yes_x+self.popup_yes_width) and \
                        (self.popup_yes_y <= mouse_y <= self.popup_yes_y + self.popup_yes_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.coin_amount = '520'
                        self.show_coin()

    def show_coin(self):
        coin_obj_list = {}
        coin_obj_list['background'] = pygame.image.load(self.coin_background), (self.coin_background_x, self.coin_background_y)
        coin_obj_list['coin_main'] = pygame.image.load(self.coin_main), (self.coin_main_x, self.coin_main_y)
        coin_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        if self.coin_amount=='20':
            coin_obj_list['coin'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
        elif self.coin_amount=='520':
            coin_obj_list['coin'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                coin_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in coin_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width) and \
                        (self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.coin_buy_x <= mouse_x <= self.coin_buy_x+self.coin_buy_width) and \
                        (self.coin_buy_y <= mouse_y <= self.coin_buy_y+self.coin_buy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_popup()
                        no_event = False
