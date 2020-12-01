import sys
import pygame
from pygame.locals import *

class Catbook:
    def __init__(self):
        self.window_surface = pygame.display.set_mode((1340, 720))
        self.catbook_background, self.catbook_background_x, self.catbook_background_y = 'images/5_book_obj/background.png', 0, 0
        self.catbook_main, self.catbook_main_x, self.catbook_main_y = 'images/5_book_obj/catbook.png', 161, 62

        self.x_button, self.x_button_x, self.x_button_y = 'images/5_book_obj/x_button.png', 1180, 76
        self.x_button_width, self.x_button_height = 104, 104

        self.leon, self.leon_x, self.leon_y = 'images/5_book_obj/face/leon.png', 339, 265
        self.ban_nyang, self.ban_nyang_x, self.ban_nyang_y = 'images/5_book_obj/face/ban_nyang.png', 478, 265
        self.kakku, self.kakku_x, self.kakku_y = 'images/5_book_obj/face/kakku.png', 615, 265
        self.cat_mark_width , self.cat_mark_height = 113, 107

        self.explain_x_button_x, self.explain_x_button_y = 1098, 38
        self.explain_leon, self.explain_leon_x, self.explain_leon_y = 'images/5_book_obj/explain/leon.png', 101, 27
        self.explain_ban_nyang, self.explain_ban_nyang_x, self.explain_ban_nyang_y = 'images/5_book_obj/explain/ban_nyang.png', 101, 27
        self.explain_kakku, self.explain_kakku_x, self.explain_kakku_y = 'images/5_book_obj/explain/kakku.png', 101, 27

        self.mouse_cursor = 'images/999_ect/cat_cursor.png'
        pygame.mouse.set_visible(False)

    def show_explain(self, cat):
        explain_obj_list = {}
        explain_obj_list['background'] = pygame.image.load(self.catbook_background), (self.catbook_background_x, self.catbook_background_y)
        if cat == 'leon':
            explain_obj_list['cat'] = pygame.image.load(self.explain_leon), (self.explain_leon_x, self.explain_leon_y)
        if cat == 'ban_nyang':
            explain_obj_list['cat'] = pygame.image.load(self.explain_ban_nyang), (self.explain_ban_nyang_x, self.explain_ban_nyang_y)
        if cat == 'kakku':
            explain_obj_list['cat'] = pygame.image.load(self.explain_kakku), (self.explain_kakku_x, self.explain_kakku_y)
        explain_obj_list['x_button'] = pygame.image.load(self.x_button), (self.explain_x_button_x, self.explain_x_button_y)
        for obj, (x, y) in explain_obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        explain_no_event = True
        while explain_no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                explain_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in explain_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if (self.explain_x_button_x <= mouse_x <= self.explain_x_button_x + self.x_button_width) and \
                    (self.explain_x_button_y <= mouse_y <= self.explain_x_button_y + self.x_button_height):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        explain_no_event = False
                        self.show_catbook()

    def show_catbook(self):
        catbook_obj_list = {}
        catbook_obj_list['background'] = pygame.image.load(self.catbook_background), (self.catbook_background_x, self.catbook_background_y)
        catbook_obj_list['catbook_main'] = pygame.image.load(self.catbook_main), (self.catbook_main_x, self.catbook_main_y)
        catbook_obj_list['x_button'] = pygame.image.load(self.x_button), (self.x_button_x, self.x_button_y)

        catbook_obj_list['leon'] = pygame.image.load(self.leon), (self.leon_x, self.leon_y)
        catbook_obj_list['ban_nyang'] = pygame.image.load(self.ban_nyang), (self.ban_nyang_x, self.ban_nyang_y)
        catbook_obj_list['kakku'] = pygame.image.load(self.kakku), (self.kakku_x, self.kakku_y)
        catbook_no_event = True
        while catbook_no_event:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                catbook_obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), (mouse_x, mouse_y)
                for obj, (x, y) in catbook_obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

                if self.x_button_x <= mouse_x <= self.x_button_x+self.x_button_width and self.x_button_y <= mouse_y <= self.x_button_y+self.x_button_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        catbook_no_event = False

                if self.leon_x <= mouse_x <= self.leon_x+self.cat_mark_width and self.leon_y <= mouse_y <= self.leon_y+self.cat_mark_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_explain(cat='leon')
                        catbook_no_event = False

                if self.ban_nyang_x <= mouse_x <= self.ban_nyang_x + self.cat_mark_width and self.ban_nyang_y <= mouse_y <= self.ban_nyang_y + self.cat_mark_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_explain(cat='ban_nyang')
                        catbook_no_event = False

                if self.kakku_x <= mouse_x <= self.kakku_x + self.cat_mark_width and self.kakku_y <= mouse_y <= self.kakku_y + self.cat_mark_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_explain(cat='kakku')
                        catbook_no_event = False
