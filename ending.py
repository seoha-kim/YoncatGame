import pygame
from pygame.locals import *
import os, sys, time

class Ending:
    def __init__(self):
        self.obj_list = {}
        self.window_surface = pygame.display.set_mode((1340, 720))
        self.file_dir = 'images/9_ending'
        pygame.mouse.set_visible(False)

    def background_music(self, mp3_file):
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def ending_movie(self, mp3_file='sounds/ending.ogg'):
        img_names = os.listdir(self.file_dir)
        img_names = [img for img in img_names if img.endswith(".png")]
        img_names.sort()
        all_imgs = {}
        self.background_music(mp3_file)
        for i, img in enumerate(img_names):
            all_imgs[img] = pygame.image.load('{}/{}'.format(self.file_dir, img))
            self.window_surface.blit(all_imgs[img], (0, 0))
            pygame.time.delay(88)
            pygame.display.update()
            if i == len(img_names) - 1:
                self.obj_list['background'] = all_imgs[img], (0, 0)
        pygame.quit()
        sys.exit()
