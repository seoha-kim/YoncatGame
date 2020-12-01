import pygame
from pygame.locals import *
import os, sys


class Intro:
    def __init__(self):
        self.obj_list = {}
        self.window_surface = pygame.display.set_mode((1340, 720))
        self.character = None

        self.file_dir = 'images/1_intro_movie'
        self.notice_img='images/2_intro_obj/notice_box.png'
        self.start_img='images/2_intro_obj/start_button.png'

        self.choice_img = 'images/2_intro_obj/character_choice.png'
        self.male_img = 'images/2_intro_obj/character_choice_male.png'
        self.female_img = 'images/2_intro_obj/character_choice_female.png'

        self.mouse_cursor = 'images/999_ect/cat_cursor.png'

    def background_music(self, mp3_file):
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def opening_movie(self, mp3_file='sounds/intro.ogg'):
        img_names = os.listdir(self.file_dir)
        img_names = [img for img in img_names if img.endswith(".png")]
        img_names.sort()
        all_imgs = {}
        self.background_music(mp3_file)
        for i, img in enumerate(img_names):
            img_file = os.path.join(self.file_dir, img)
            all_imgs[img] = pygame.image.load(img_file)
            self.window_surface.blit(all_imgs[img], (0, 0))
            pygame.time.delay(85)
            pygame.display.update()
            if i == len(img_names) - 1:
                self.obj_list['background'] = all_imgs[img], (0, 0)
        pygame.event.pump()

    def notice_box(self, x=245, y=177):
        self.obj_list['notice_box'] = pygame.image.load(self.notice_img), (x, y)
        for obj, (x,y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
        pygame.time.delay(2000)
        self.remove_obj('notice_box')

    def start_button(self, x=537, y=614):
        self.obj_list['start_button'] = pygame.image.load(self.start_img), (x, y)
        width, height = self.obj_list['start_button'][0].get_size()
        not_click = True
        while not_click:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if x <= mouse_x <= x+width and y <= mouse_y <= y + height:
                        pygame.time.delay(500)
                        not_click = False

                coord = pygame.mouse.get_pos()
                self.obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), coord
                for obj, (x, y) in self.obj_list.values():
                    self.window_surface.blit(obj, (x, y))
                pygame.display.update()

    def choice_screen(self, ):
        self.background_music(mp3_file='sounds/character_choice.ogg')
        global character
        self.obj_list = {}
        self.obj_list['background'] = pygame.image.load(self.choice_img), (0, 0)
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()

        male_x, male_y = 225, 350; female_x, female_y = 778 ,350
        male_width, male_height, female_width, female_height = 340, 300, 340, 300
        male_img = pygame.image.load(self.male_img); female_img = pygame.image.load(self.female_img)
        not_click = True
        while not_click:
            for event in pygame.event.get():
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if male_x <= mouse_x <= male_x+male_width and male_y <= mouse_y <= male_y+male_height:
                    self.obj_list['background'] = male_img, (0, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.character = 'male'
                        self.background_music('sounds/choice_complete.ogg')
                        not_click = False
                        pygame.time.delay(800)

                if female_x <= mouse_x <= female_x+female_width and female_y <= mouse_y <= female_y+female_height:
                    self.obj_list['background'] = female_img, (0, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.character = 'female'
                        self.background_music('sounds/choice_complete.ogg')
                        not_click = False
                        pygame.time.delay(800)

                coord = pygame.mouse.get_pos()
                self.obj_list['mouse_cursor'] = pygame.image.load(self.mouse_cursor), coord
                for obj, (x, y) in self.obj_list.values():
                    self.window_surface.blit(obj, (x, y))

                pygame.time.delay(10)
                pygame.display.update()


    def remove_obj(self, obj_name):
        del self.obj_list[obj_name]
        for obj, (x, y) in self.obj_list.values():
            self.window_surface.blit(obj, (x, y))
        pygame.display.update()
