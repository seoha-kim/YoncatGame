import sys
import pygame
from pygame.locals import *

class Shop:
    def __init__(self):
        self.window_surface = pygame.display.set_mode((1340, 720))
        self.shop_background, self.shop_background_x, self.shop_background_y = 'images/6_shop_obj/shop_background.png', 0, 0

        self.shop_food, self.shop_food_x, self.shop_food_y = 'images/6_shop_obj/shop/shop_food.png', 0, -1
        self.shop_snack, self.shop_snack_x, self.shop_snack_y = 'images/6_shop_obj/shop/shop_snack.png', 0, 0
        self.shop_toy, self.shop_toy_x, self.shop_toy_y = 'images/6_shop_obj/shop/shop_toy.png', 0, 0
        self.shop_ect, self.shop_ect_x, self.shop_ect_y = 'images/6_shop_obj/shop/shop_ect.png', 0, 0

        self.button_food_x, self.button_food_y, self.button_food_width, self.button_food_height = 114, 212, 118, 80
        self.button_snack_x, self.button_snack_y, self.button_snack_width, self.button_snack_height = 114, 316, 118, 80
        self.button_toy_x, self.button_toy_y, self.button_toy_width, self.button_toy_height = 114, 420, 118, 80
        self.button_ect_x, self.button_ect_y, self.button_ect_width, self.button_ect_height = 114, 524, 118,80

        self.coin_20, self.coin_100 = 'images/6_shop_obj/coin_20.png', 'images/6_shop_obj/coin_100.png'
        self.coin_480, self.coin_520 = 'images/6_shop_obj/coin_480.png', 'images/6_shop_obj/coin_520.png'
        self.coin_amount, self.coin_x, self.coin_y = '100', 926, 589

        self.x_button, self.x_button_x, self.x_button_y = 'images/6_shop_obj/x_button.png', 1180, 76
        self.x_button_width, self.x_button_height = 104, 104

        self.chur_x, self.chur_y, self.chur_width , self.chur_height = 554, 235, 236, 175
        self.chur_popup, self.chur_popup_x, self.chur_popup_y = 'images/6_shop_obj/chur.png', 132, 62
        self.fishing_rod_x, self.fishing_rod_y, self.fishing_rod_width, self.fishing_rod_height = 293, 235, 236, 765
        self.fishing_rod_popup, self.fishing_rod_popup_x, self.fishing_rod_popup_y = 'images/6_shop_obj/fishing_rod.png', 132, 62

        self.popup_back_button, self.popup_back_button_x, self.popup_back_button_y = 'images/6_shop_obj/back_button.png',  56, 605
        self.popup_back_button_width, self.popup_back_button_height = 104, 104
        self.popup_buy, self.popup_buy_x, self.popup_buy_y = 'images/6_shop_obj/buy_button.png', 831, 533
        self.popup_buy_width, self.popup_buy_height = 265, 90

        self.buy_complete, self.buy_complete_x, self.buy_complete_y =  'images/6_shop_obj/buy_complete.png', 332, 164
        self.buy_no_coin, self.buy_no_coin_x, self.buy_no_coin_y = 'images/6_shop_obj/buy_no_coin.png', 332, 164
        self.popup_x_button_x, self.popup_x_button_y, self.popup_x_button_width, self.popup_x_button_height = 907, 280, 72, 72

        self.mouse_cursor = 'images/999_ect/cat_cursor.png'
        pygame.mouse.set_visible(False)

    def show_chur_popup(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['popup_main'] = pygame.image.load(self.chur_popup), (self.chur_popup_x, self.chur_popup_y)
        shop_obj_list['back_button'] = pygame.image.load(self.popup_back_button), (self.popup_back_button_x, self.popup_back_button_y)
        shop_obj_list['buy_button'] = pygame.image.load(self.popup_buy), (self.popup_buy_x, self.popup_buy_y)
        for obj, (x, y) in shop_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.popup_back_button_x <= mouse_x <= self.popup_back_button_x+self.popup_back_button_width) and \
                        (self.popup_back_button_y <= mouse_y <= self.popup_back_button_y + self.popup_back_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.show_snack()

                if (self.popup_buy_x <= mouse_x <= self.popup_buy_x+self.popup_buy_width) and \
                        (self.popup_buy_y <= mouse_y <= self.popup_buy_y + self.popup_buy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.coin_amount = '20'
                        self.chur_buy_complete()

    def chur_buy_complete(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['popup_main'] = pygame.image.load(self.chur_popup), (self.chur_popup_x, self.chur_popup_y)
        shop_obj_list['back_button'] = pygame.image.load(self.popup_back_button), (self.popup_back_button_x, self.popup_back_button_y)
        shop_obj_list['buy_button'] = pygame.image.load(self.popup_buy), (self.popup_buy_x, self.popup_buy_y)
        shop_obj_list['buy_complete'] = pygame.image.load(self.buy_complete), (self.buy_complete_x, self.buy_complete_y)
        for obj, (x, y) in shop_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.popup_x_button_x <= mouse_x <= self.popup_x_button_x+self.popup_x_button_width) and \
                        (self.popup_x_button_y <= mouse_y <= self.popup_x_button_y + self.popup_x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.show_chur_popup()

    def show_fishing_rod_popup(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['popup_main'] = pygame.image.load(self.fishing_rod_popup), (self.fishing_rod_popup_x, self.fishing_rod_popup_y)
        shop_obj_list['back_button'] = pygame.image.load(self.popup_back_button), (self.popup_back_button_x, self.popup_back_button_y)
        shop_obj_list['buy_button'] = pygame.image.load(self.popup_buy), (self.popup_buy_x, self.popup_buy_y)
        for obj, (x, y) in shop_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.popup_back_button_x <= mouse_x <= self.popup_back_button_x+self.popup_back_button_width) and \
                        (self.popup_back_button_y <= mouse_y <= self.popup_back_button_y + self.popup_back_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.show_snack()

                if (self.popup_buy_x <= mouse_x <= self.popup_buy_x+self.popup_buy_width) and \
                        (self.popup_buy_y <= mouse_y <= self.popup_buy_y + self.popup_buy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        if self.coin_amount == '20':
                            self.fishing_rod_buy_fail()
                        if self.coin_amount == '520':
                            self.coin_amount = '480'
                            self.fishing_rod_buy_complete()


    def fishing_rod_buy_fail(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['popup_main'] = pygame.image.load(self.fishing_rod_popup), (self.fishing_rod_popup_x, self.fishing_rod_popup_y)
        shop_obj_list['back_button'] = pygame.image.load(self.popup_back_button), (self.popup_back_button_x, self.popup_back_button_y)
        shop_obj_list['buy_button'] = pygame.image.load(self.popup_buy), (self.popup_buy_x, self.popup_buy_y)
        shop_obj_list['buy_fail'] = pygame.image.load(self.buy_no_coin), (self.buy_no_coin_x, self.buy_no_coin_y)
        for obj, (x, y) in shop_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.popup_x_button_x <= mouse_x <= self.popup_x_button_x+self.popup_x_button_width) and \
                        (self.popup_x_button_y <= mouse_y <= self.popup_x_button_y + self.popup_x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.show_fishing_rod_popup()

    def fishing_rod_buy_complete(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['popup_main'] = pygame.image.load(self.fishing_rod_popup), (self.fishing_rod_popup_x, self.fishing_rod_popup_y)
        shop_obj_list['back_button'] = pygame.image.load(self.popup_back_button), (self.popup_back_button_x, self.popup_back_button_y)
        shop_obj_list['buy_button'] = pygame.image.load(self.popup_buy), (self.popup_buy_x, self.popup_buy_y)
        shop_obj_list['buy_complete'] = pygame.image.load(self.buy_complete), (self.buy_complete_x, self.buy_complete_y)
        for obj, (x, y) in shop_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.popup_x_button_x <= mouse_x <= self.popup_x_button_x+self.popup_x_button_width) and \
                        (self.popup_x_button_y <= mouse_y <= self.popup_x_button_y + self.popup_x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False
                        self.show_fishing_rod_popup()

    def show_food(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['shop_food'] = pygame.image.load(self.shop_food), (self.shop_food_x, self.shop_food_y)
        shop_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        if self.coin_amount=='20':
            shop_obj_list['shop'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
        if self.coin_amount=='100':
            shop_obj_list['shop'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
        if self.coin_amount=='480':
            shop_obj_list['shop'] = pygame.image.load(self.coin_480), (self.coin_x, self.coin_y)
        if self.coin_amount=='520':
            shop_obj_list['shop'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width) and \
                        (self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.button_food_x <= mouse_x <= self.button_food_x+self.button_food_width) and \
                        (self.button_food_y <= mouse_y <= self.button_food_y+self.button_food_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_food()
                        no_event = False

                if (self.button_snack_x <= mouse_x <= self.button_snack_x+self.button_snack_width) and \
                        (self.button_snack_y <= mouse_y <= self.button_snack_y+self.button_snack_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_snack()
                        no_event = False

                if (self.button_toy_x <= mouse_x <= self.button_toy_x+self.button_toy_width) and \
                        (self.button_toy_y <= mouse_y <= self.button_toy_y+self.button_toy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_toy()
                        no_event = False

                if (self.button_ect_x <= mouse_x <= self.button_ect_x+self.button_ect_width) and \
                        (self.button_ect_y <= mouse_y <= self.button_ect_y+self.button_ect_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_ect()
                        no_event = False

    def show_snack(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['shop_snack'] = pygame.image.load(self.shop_snack), (self.shop_snack_x, self.shop_snack_y)
        shop_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        if self.coin_amount=='20':
            shop_obj_list['shop'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
        if self.coin_amount=='100':
            shop_obj_list['shop'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
        if self.coin_amount=='480':
            shop_obj_list['shop'] = pygame.image.load(self.coin_480), (self.coin_x, self.coin_y)
        if self.coin_amount=='520':
            shop_obj_list['shop'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width) and \
                        (self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.button_food_x <= mouse_x <= self.button_food_x+self.button_food_width) and \
                        (self.button_food_y <= mouse_y <= self.button_food_y+self.button_food_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_food()
                        no_event = False

                if (self.button_snack_x <= mouse_x <= self.button_snack_x+self.button_snack_width) and \
                        (self.button_snack_y <= mouse_y <= self.button_snack_y+self.button_snack_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_snack()
                        no_event = False

                if (self.button_toy_x <= mouse_x <= self.button_toy_x+self.button_toy_width) and \
                        (self.button_toy_y <= mouse_y <= self.button_toy_y+self.button_toy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_toy()
                        no_event = False

                if (self.button_ect_x <= mouse_x <= self.button_ect_x+self.button_ect_width) and \
                        (self.button_ect_y <= mouse_y <= self.button_ect_y+self.button_ect_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_ect()
                        no_event = False

                if (self.chur_x <= mouse_x <= self.chur_x+self.chur_width) and \
                        (self.chur_y <= mouse_y <= self.chur_y+self.chur_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_chur_popup()
                        no_event = False

    def show_toy(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['shop_toy'] = pygame.image.load(self.shop_toy), (self.shop_toy_x, self.shop_toy_y)
        shop_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        if self.coin_amount=='20':
            shop_obj_list['shop'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
        if self.coin_amount=='100':
            shop_obj_list['shop'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
        if self.coin_amount=='480':
            shop_obj_list['shop'] = pygame.image.load(self.coin_480), (self.coin_x, self.coin_y)
        if self.coin_amount=='520':
            shop_obj_list['shop'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width) and \
                        (self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.button_food_x <= mouse_x <= self.button_food_x+self.button_food_width) and \
                        (self.button_food_y <= mouse_y <= self.button_food_y+self.button_food_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_food()
                        no_event = False

                if (self.button_snack_x <= mouse_x <= self.button_snack_x+self.button_snack_width) and \
                        (self.button_snack_y <= mouse_y <= self.button_snack_y+self.button_snack_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_snack()
                        no_event = False

                if (self.button_toy_x <= mouse_x <= self.button_toy_x+self.button_toy_width) and \
                        (self.button_toy_y <= mouse_y <= self.button_toy_y+self.button_toy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_toy()
                        no_event = False

                if (self.button_ect_x <= mouse_x <= self.button_ect_x+self.button_ect_width) and \
                        (self.button_ect_y <= mouse_y <= self.button_ect_y+self.button_ect_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_ect()
                        no_event = False

                if (self.fishing_rod_x <= mouse_x <= self.fishing_rod_x+self.fishing_rod_width) and \
                        (self.fishing_rod_y <= mouse_y <= self.fishing_rod_y+self.fishing_rod_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_fishing_rod_popup()
                        no_event = False

    def show_ect(self):
        shop_obj_list = {}
        shop_obj_list['background'] = pygame.image.load(self.shop_background), (self.shop_background_x, self.shop_background_y)
        shop_obj_list['shop_ect'] = pygame.image.load(self.shop_ect), (self.shop_ect_x, self.shop_ect_y)
        shop_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)
        if self.coin_amount=='20':
            shop_obj_list['shop'] = pygame.image.load(self.coin_20), (self.coin_x, self.coin_y)
        if self.coin_amount=='100':
            shop_obj_list['shop'] = pygame.image.load(self.coin_100), (self.coin_x, self.coin_y)
        if self.coin_amount=='480':
            shop_obj_list['shop'] = pygame.image.load(self.coin_480), (self.coin_x, self.coin_y)
        if self.coin_amount=='520':
            shop_obj_list['shop'] = pygame.image.load(self.coin_520), (self.coin_x, self.coin_y)
        no_event = True
        while no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                shop_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in shop_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width) and \
                        (self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        no_event = False

                if (self.button_food_x <= mouse_x <= self.button_food_x+self.button_food_width) and \
                        (self.button_food_y <= mouse_y <= self.button_food_y+self.button_food_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_food()
                        no_event = False

                if (self.button_snack_x <= mouse_x <= self.button_snack_x+self.button_snack_width) and \
                        (self.button_snack_y <= mouse_y <= self.button_snack_y+self.button_snack_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_snack()
                        no_event = False

                if (self.button_toy_x <= mouse_x <= self.button_toy_x+self.button_toy_width) and \
                        (self.button_toy_y <= mouse_y <= self.button_toy_y+self.button_toy_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_toy()
                        no_event = False

                if (self.button_ect_x <= mouse_x <= self.button_ect_x+self.button_ect_width) and \
                        (self.button_ect_y <= mouse_y <= self.button_ect_y+self.button_ect_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_ect()
                        no_event = False
